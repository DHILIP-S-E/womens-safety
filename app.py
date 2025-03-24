from flask import Flask, jsonify
from flask_cors import CORS  # Added CORS support
from aws_lambda_powertools import Logger
import boto3
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS
logger = Logger()

# Configure AWS region (Ensure AWS credentials are set in ENV)
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")  # Change as needed

# Initialize AWS Services
try:
    dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
    sns = boto3.client('sns', region_name=AWS_REGION)

    # Define DynamoDB Tables
    LEGAL_RESOURCES_TABLE = dynamodb.Table('legal_resources')
    NGO_DIRECTORY_TABLE = dynamodb.Table('ngo_directory')
    HOSPITALS_TABLE = dynamodb.Table('hospitals')

except Exception as e:
    logger.error(f"AWS Initialization Error: {str(e)}")
    dynamodb, sns = None, None  # Prevent breaking the app
# API to Fetch Hospitals
@app.route('/api/hospitals', methods=['GET'])
def get_hospitals():
    try:
        response = HOSPITALS_TABLE.scan()
        hospitals = response.get('Items', [])
        formatted_hospitals = [
            {
                'id': hospital.get('id', ''),
                'name': hospital.get('name', ''),
                'description': hospital.get('description', ''),
                'emergency_contact': hospital.get('emergency_contact', ''),
                'address': hospital.get('address', ''),
                'is_24_7': hospital.get('is_24_7', False),
                'services': hospital.get('services', [])
            }
            for hospital in hospitals
        ]
        return jsonify(formatted_hospitals)
    except Exception as e:
        logger.error(f"Error fetching hospitals: {str(e)}")
        return jsonify({'error': 'Failed to fetch hospitals'}), 500

# API to Fetch Legal Resources
@app.route('/api/legal-resources', methods=['GET'])
def get_legal_resources():
    if not dynamodb:
        return jsonify({'error': 'AWS Initialization Failed'}), 500
    try:
        response = LEGAL_RESOURCES_TABLE.scan()
        resources = response.get('Items', [])

        # Fix API Response Format
        formatted_resources = [
            {
                'id': resource.get('id', ''),
                'title': resource.get('title', 'No Title'),
                'description': resource.get('description', 'No Description'),
                'contact': resource.get('contact', 'Not Available'),
                'hours': resource.get('hours', 'Not Available'),
                'website': resource.get('website', '#')
            }
            for resource in resources
        ]

        return jsonify(formatted_resources)
    except Exception as e:
        logger.error(f"Error fetching legal resources: {str(e)}")
        return jsonify({'error': 'Failed to fetch legal resources'}), 500

# Legal Emergency Alert Route
@app.route('/api/send-emergency-sms', methods=['POST'])
def send_emergency_sms():
    try:
        message = "🚨 Legal Emergency Alert: Immediate legal assistance needed!"
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:730335218388:veilnet-alerts',
            Message=message,
            Subject='Legal Emergency Alert'
        )
        return jsonify({'message': 'Legal emergency alert sent successfully'})
    except Exception as e:
        logger.error(f"Error sending legal emergency SMS: {str(e)}")
        return jsonify({'error': 'Failed to send legal emergency alert'}), 500

# Medical Emergency Alert Route
@app.route('/api/send-medical-alert', methods=['POST'])
def send_medical_alert():
    try:
        message = "🚑 Medical Emergency Alert: Urgent medical help required!"
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:730335218388:veilnet-alerts',
            Message=message,
            Subject='Medical Emergency Alert'
        )
        return jsonify({'message': 'Medical emergency alert sent successfully'})
    except Exception as e:
        logger.error(f"Error sending medical emergency SMS: {str(e)}")
        return jsonify({'error': 'Failed to send medical emergency alert'}), 500

# Safety Emergency Alert Route
@app.route('/api/send-safety-alert', methods=['POST'])
def send_safety_alert():
    try:
        message = "⚠️ Safety Emergency Alert: Immediate safety assistance required!"
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:730335218388:veilnet-alerts',
            Message=message,
            Subject='Safety Emergency Alert'
        )
        return jsonify({'message': 'Safety emergency alert sent successfully'})
    except Exception as e:
        logger.error(f"Error sending safety emergency SMS: {str(e)}")
        return jsonify({'error': 'Failed to send safety emergency alert'}), 500

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
