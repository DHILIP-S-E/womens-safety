# WomenSafe Hub API Documentation

## Base URL

```
https://api.womensafehub.org
```

## Authentication

Currently, the API endpoints are public and do not require authentication.

## Endpoints

### Legal Resources

#### GET /api/legal-resources

Retrieves a list of available legal resources.

**Response**
```json
{
    "Items": [
        {
            "id": "string",
            "name": "string",
            "description": "string",
            "contact": "string",
            "hours": "string",
            "website": "string",
            "services": ["string"],
            "created_at": "string",
            "updated_at": "string"
        }
    ]
}
```

### Hospitals

#### GET /api/hospitals

Retrieves a list of available hospitals.

**Response**
```json
{
    "Items": [
        {
            "id": "string",
            "name": "string",
            "description": "string",
            "emergency_contact": "string",
            "address": "string",
            "is_24_7": "boolean",
            "services": ["string"],
            "latitude": "number",
            "longitude": "number",
            "created_at": "string",
            "updated_at": "string"
        }
    ]
}
```

### NGO Directory

#### GET /api/ngo-directory

Retrieves a list of available NGOs.

**Response**
```json
{
    "Items": [
        {
            "id": "string",
            "name": "string",
            "description": "string",
            "services": ["string"],
            "contact": "string",
            "phone": "string",
            "hours": "string",
            "address": "string",
            "website": "string",
            "created_at": "string",
            "updated_at": "string"
        }
    ]
}
```

### Emergency SMS

#### POST /api/send-emergency-sms

Sends an emergency SMS alert.

**Request**
- No request body required

**Response**
```json
{
    "message": "Emergency alert sent successfully"
}
```

## Error Responses

All endpoints may return the following error response:

```json
{
    "error": "Error message description"
}
```

HTTP Status Codes:
- 200: Success
- 400: Bad Request
- 500: Internal Server Error