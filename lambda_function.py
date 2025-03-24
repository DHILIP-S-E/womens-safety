import json
import os
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
import boto3

# Initialize Logger
logger = Logger()
app = APIGatewayRestResolver()
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# DynamoDB tables
LEGAL_RESOURCES_TABLE = os.environ.get('LEGAL_RESOURCES_TABLE', 'legal_resources')
NGO_DIRECTORY_TABLE = os.environ.get('NGO_DIRECTORY_TABLE', 'ngo_directory')
HOSPITALS_TABLE = os.environ.get('HOSPITALS_TABLE', 'hospitals')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')

@app.get("/api/legal-resources")
def get_legal_resources():
    try:
        table = dynamodb.Table(LEGAL_RESOURCES_TABLE)
        response = table.scan()
        return {"statusCode": 200, "body": response.get('Items', [])}
    except Exception as e:
        logger.error(f"Error fetching legal resources: {str(e)}")
        return {"statusCode": 500, "body": {"error": "Failed to fetch legal resources"}}

@app.get("/api/ngo-directory")
def get_ngo_directory():
    try:
        table = dynamodb.Table(NGO_DIRECTORY_TABLE)
        response = table.scan()
        return {"statusCode": 200, "body": response.get('Items', [])}
    except Exception as e:
        logger.error(f"Error fetching NGO directory: {str(e)}")
        return {"statusCode": 500, "body": {"error": "Failed to fetch NGO directory"}}

@app.get("/api/hospitals")
def get_hospitals():
    try:
        table = dynamodb.Table(HOSPITALS_TABLE)
        response = table.scan()
        return {"statusCode": 200, "body": response.get('Items', [])}
    except Exception as e:
        logger.error(f"Error fetching hospitals: {str(e)}")
        return {"statusCode": 500, "body": {"error": "Failed to fetch hospitals"}}

@app.post("/api/send-emergency-sms")
def send_emergency_sms():
    try:
        message = "Emergency Alert: Immediate assistance required!"
        
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject='Emergency Alert',
            MessageAttributes={
                'SMS': {
                    'DataType': 'String',
                    'StringValue': 'Transactional'
                }
            }
        )
        return {"statusCode": 200, "body": {"message": "Emergency alert sent successfully"}}
    except Exception as e:
        logger.error(f"Error sending emergency SMS: {str(e)}")
        return {"statusCode": 500, "body": {"error": "Failed to send emergency alert"}}

@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
def handler(event: dict, context: LambdaContext) -> dict:
    """Main Lambda handler."""
    return app.resolve(event, context)