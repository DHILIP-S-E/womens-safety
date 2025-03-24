import json
import boto3
from typing import Dict, Any, Optional
from datetime import datetime
from aws_lambda_powertools.logging import Logger

logger = Logger()
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

def format_dynamodb_response(response: Dict[str, Any]) -> list:
    """Format DynamoDB response by removing DynamoDB data types."""
    items = response.get('Items', [])
    return [
        {k: (v.get('S') or v.get('N') or v.get('BOOL') or v.get('L') or v.get('M'))
         for k, v in item.items()}
        for item in items
    ]

def send_emergency_alert(message: str, phone_number: str, topic_arn: str) -> bool:
    """Send emergency SMS alert using AWS SNS."""
    try:
        sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject='Emergency Alert',
            MessageAttributes={
                'SMS': {
                    'DataType': 'String',
                    'StringValue': 'Transactional'
                }
            }
        )
        logger.info(f"Emergency alert sent successfully to {phone_number}")
        return True
    except Exception as e:
        logger.error(f"Failed to send emergency alert: {str(e)}")
        return False

def validate_phone_number(phone: str) -> bool:
    """Validate phone number format."""
    import re
    pattern = r'^\+?1?\d{9,15}$'
    return bool(re.match(pattern, phone))

def get_resource_by_id(table_name: str, resource_id: str) -> Optional[Dict[str, Any]]:
    """Get a resource from DynamoDB by its ID."""
    try:
        table = dynamodb.Table(table_name)
        response = table.get_item(Key={'id': resource_id})
        return response.get('Item')
    except Exception as e:
        logger.error(f"Error fetching resource from {table_name}: {str(e)}")
        return None

def create_resource(table_name: str, item: Dict[str, Any]) -> bool:
    """Create a new resource in DynamoDB."""
    try:
        table = dynamodb.Table(table_name)
        item['created_at'] = datetime.utcnow().isoformat()
        item['updated_at'] = item['created_at']
        table.put_item(Item=item)
        return True
    except Exception as e:
        logger.error(f"Error creating resource in {table_name}: {str(e)}")
        return False

def update_resource(table_name: str, resource_id: str, updates: Dict[str, Any]) -> bool:
    """Update an existing resource in DynamoDB."""
    try:
        table = dynamodb.Table(table_name)
        updates['updated_at'] = datetime.utcnow().isoformat()
        update_expression = "SET " + ", ".join(f"#{k} = :{k}" for k in updates.keys())
        expression_attribute_names = {f"#{k}": k for k in updates.keys()}
        expression_attribute_values = {f":{k}": v for k, v in updates.items()}
        
        table.update_item(
            Key={'id': resource_id},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )
        return True
    except Exception as e:
        logger.error(f"Error updating resource in {table_name}: {str(e)}")
        return False