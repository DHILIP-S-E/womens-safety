# WomenSafe Hub

A minimal AWS-based women's safety hub providing essential resources and emergency assistance.

## Features

- Legal & Self-Defense Resources
- Instant Legal Help via Emergency SMS
- Emergency Medical Assistance
- Safe House & NGO Directory

## Technical Stack

- Frontend: Static HTML + CSS
- Backend: AWS Lambda with Python/Flask
- Database: Amazon DynamoDB
- Messaging: AWS SNS
- Hosting: AWS S3 Static Website Hosting

## Setup Instructions

1. Deploy Infrastructure
```bash
cd infrastructure/terraform
terraform init
terraform apply
```

2. Update Configuration
- Set your AWS credentials
- Update SNS Topic ARN in app.py
- Update S3 bucket name in terraform config

3. Deploy Frontend
```bash
aws s3 sync static/ s3://womensafe-hub-static
```

4. Deploy Backend
```bash
zip -r lambda_function.zip app.py
aws lambda update-function-code --function-name womensafe-hub-api --zip-file fileb://lambda_function.zip
```

## Emergency Features

- "Call Lawyer" button - Sends immediate SMS to legal help
- "Call Ambulance" button - Triggers emergency medical alerts
- Quick access to NGO and shelter contacts

## Security & Privacy

- All data stored in DynamoDB is encrypted at rest
- HTTPS-only access to website
- Emergency contacts are pre-verified