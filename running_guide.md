# How to Run the WomenSafe Hub Application

## Prerequisites
1. Make sure you have Python installed on your system
2. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

## Available Services
The application provides the following services:

1. Legal Resources API
   - Endpoint: `/api/legal-resources`
   - Method: GET
   - Description: Get information about legal resources and support

2. NGO Directory API
   - Endpoint: `/api/ngo-directory`
   - Method: GET
   - Description: Access directory of NGOs and support organizations

3. Hospitals API
   - Endpoint: `/api/hospitals`
   - Method: GET
   - Description: Get list of nearby hospitals and medical facilities

4. Emergency SMS Service
   - Endpoint: `/api/send-emergency-sms`
   - Method: POST
   - Description: Send emergency SMS alerts

## How to Start the Application

1. First, make sure you're in the project directory

2. Set up environment variables (if needed):
   Create a `.env` file with necessary configurations

3. Start the application:
   ```
   # Development mode
   flask run

   # Production mode
   gunicorn app:app
   ```

4. The application will start running on:
   - Development: http://localhost:5000
   - Production: Depending on your gunicorn configuration

## Testing the Services

You can test the endpoints using:
1. Web browser (for GET requests)
2. Postman or similar API testing tools
3. curl commands:
   ```
   # Get legal resources
   curl http://localhost:5000/api/legal-resources

   # Get NGO directory
   curl http://localhost:5000/api/ngo-directory

   # Get hospitals
   curl http://localhost:5000/api/hospitals

   # Send emergency SMS (POST request)
   curl -X POST http://localhost:5000/api/send-emergency-sms
   ```

## Troubleshooting

If you encounter any issues:
1. Make sure all dependencies are installed correctly
2. Check if the required environment variables are set
3. Look for error messages in the console
4. Ensure you're using the correct Python version