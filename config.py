import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Flask Configuration
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# AWS Configuration
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# DynamoDB Tables
LEGAL_RESOURCES_TABLE = os.getenv('LEGAL_RESOURCES_TABLE', 'legal_resources')
NGO_DIRECTORY_TABLE = os.getenv('NGO_DIRECTORY_TABLE', 'ngo_directory')
HOSPITALS_TABLE = os.getenv('HOSPITALS_TABLE', 'hospitals')

# SNS Configuration
SNS_TOPIC_ARN = os.getenv('SNS_TOPIC_ARN')
EMERGENCY_PHONE_NUMBER = os.getenv('EMERGENCY_PHONE_NUMBER', '911')

# Application Configuration
APP_NAME = 'WomenSafe Hub'
CONTACT_EMAIL = os.getenv('CONTACT_EMAIL', 'support@womensafehub.org')
SUPPORT_PHONE = os.getenv('SUPPORT_PHONE', '1-800-SAFE-HUB')

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Cache Configuration
CACHE_TYPE = 'simple'
CACHE_DEFAULT_TIMEOUT = 300  # 5 minutes

# Security Configuration
SESSION_COOKIE_SECURE = True
REMEMBER_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
REMEMBER_COOKIE_HTTPONLY = True