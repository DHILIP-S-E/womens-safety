provider "aws" {
  region = "us-west-2"
}

# S3 bucket for static website hosting
resource "aws_s3_bucket" "website" {
  bucket = "your-unique-bucket-name"
}

resource "aws_s3_bucket_website_configuration" "website" {
  bucket = aws_s3_bucket.website.id

  index_document {
    suffix = "index.html"
  }
}

# ✅ DynamoDB Tables (Legal Resources, NGO Directory, Hospitals)
resource "aws_dynamodb_table" "legal_resources" {
  name           = "legal_resources"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

resource "aws_dynamodb_table" "ngo_directory" {
  name           = "ngo_directory"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

resource "aws_dynamodb_table" "hospitals" {
  name           = "hospitals"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

# ✅ SNS Topic for emergency alerts
resource "aws_sns_topic" "emergency_alerts" {
  name = "emergency-alerts"
}

# ✅ Lambda function for API
resource "aws_lambda_function" "api" {
  filename         = "../lambda_function.zip"
  function_name    = "womensafe-hub-api"
  role            = aws_iam_role.lambda_role.arn
  handler         = "app.lambda_handler"
  runtime         = "python3.9"

  environment {
    variables = {
      SNS_TOPIC_ARN = aws_sns_topic.emergency_alerts.arn
    }
  }
}

# ✅ IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "womensafe-hub-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}
