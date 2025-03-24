# WomenSafe Hub Setup Guide

## Prerequisites

- Python 3.8 or higher
- AWS Account with appropriate permissions
- Node.js 14+ (for frontend development)
- Docker (optional, for containerization)

## Local Development Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/womensafe-hub.git
cd womensafe-hub
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run the development server
```bash
flask run --debug
```

## AWS Infrastructure Setup

1. Install and configure AWS CLI
```bash
aws configure
# Enter your AWS credentials
```

2. Deploy infrastructure using Terraform
```bash
cd infrastructure/terraform
terraform init
terraform plan
terraform apply
```

## Database Setup

1. Create DynamoDB tables
```bash
cd infrastructure/terraform
terraform apply -target=aws_dynamodb_table.legal_resources
terraform apply -target=aws_dynamodb_table.ngo_directory
terraform apply -target=aws_dynamodb_table.hospitals
```

2. Load initial data (optional)
```bash
python scripts/seed_data.py
```

## Lambda Function Deployment

1. Create Lambda deployment package
```bash
pip install -r requirements.txt -t lambda_package/
cd lambda_package
zip -r ../lambda_function.zip .
```

2. Deploy Lambda function
```bash
aws lambda update-function-code --function-name womensafe-hub-lambda --zip-file fileb://lambda_function.zip
```

## Testing

Run the test suite:
```bash
pytest
```

## Production Deployment

1. Build static assets
```bash
python scripts/build.py
```

2. Deploy to AWS
```bash
./scripts/deploy.sh production
```

## Monitoring

1. Set up CloudWatch monitoring
```bash
./scripts/setup_monitoring.sh
```

2. Configure alerting
```bash
./scripts/setup_alerts.sh
```

## Security Considerations

- Enable AWS WAF for API Gateway
- Configure appropriate IAM roles and policies
- Enable CloudTrail logging
- Set up regular security audits
- Monitor API usage and implement rate limiting