import boto3
import logging
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dynamodb = boto3.resource('dynamodb')

def create_legal_resources_table():
    """Create legal_resources table."""
    try:
        table = dynamodb.create_table(
            TableName='legal_resources',
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName='legal_resources')
        logger.info("Created legal_resources table")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            logger.info("legal_resources table already exists")
        else:
            logger.error(f"Error creating legal_resources table: {str(e)}")
            raise

def create_hospitals_table():
    """Create hospitals table."""
    try:
        table = dynamodb.create_table(
            TableName='hospitals',
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName='hospitals')
        logger.info("Created hospitals table")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            logger.info("hospitals table already exists")
        else:
            logger.error(f"Error creating hospitals table: {str(e)}")
            raise

def create_ngo_directory_table():
    """Create ngo_directory table."""
    try:
        table = dynamodb.create_table(
            TableName='ngo_directory',
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName='ngo_directory')
        logger.info("Created ngo_directory table")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            logger.info("ngo_directory table already exists")
        else:
            logger.error(f"Error creating ngo_directory table: {str(e)}")
            raise

def main():
    """Create all required DynamoDB tables."""
    create_legal_resources_table()
    create_hospitals_table()
    create_ngo_directory_table()

if __name__ == '__main__':
    main()