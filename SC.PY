import secrets
print(secrets.token_hex(32))  # Generates a 64-character secure key
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('hospitals')

response = table.scan()
print(response)
