import pytest
from utils import (
    format_dynamodb_response,
    validate_phone_number,
    send_emergency_alert,
    get_resource_by_id,
    create_resource,
    update_resource
)
from unittest.mock import patch, MagicMock

def test_format_dynamodb_response():
    """Test DynamoDB response formatting"""
    mock_response = {
        'Items': [
            {
                'id': {'S': '1'},
                'name': {'S': 'Test Resource'},
                'is_active': {'BOOL': True},
                'count': {'N': '42'},
                'tags': {'L': [{'S': 'tag1'}, {'S': 'tag2'}]}
            }
        ]
    }
    result = format_dynamodb_response(mock_response)
    assert len(result) == 1
    assert result[0]['id'] == '1'
    assert result[0]['name'] == 'Test Resource'
    assert result[0]['is_active'] is True
    assert result[0]['count'] == '42'

def test_validate_phone_number():
    """Test phone number validation"""
    assert validate_phone_number('+1234567890') is True
    assert validate_phone_number('1234567890') is True
    assert validate_phone_number('123-456-7890') is False
    assert validate_phone_number('abcdefghij') is False

@patch('boto3.client')
def test_send_emergency_alert(mock_boto):
    """Test sending emergency alerts"""
    mock_sns = MagicMock()
    mock_boto.return_value = mock_sns
    
    result = send_emergency_alert(
        message="Test emergency",
        phone_number="+1234567890",
        topic_arn="arn:aws:sns:us-east-1:123456789012:emergency-alerts"
    )
    assert result is True
    mock_sns.publish.assert_called_once()

@patch('boto3.resource')
def test_get_resource_by_id(mock_boto):
    """Test retrieving a resource by ID"""
    mock_table = MagicMock()
    mock_boto.return_value.Table.return_value = mock_table
    mock_table.get_item.return_value = {'Item': {'id': '1', 'name': 'Test'}}
    
    result = get_resource_by_id('test_table', '1')
    assert result == {'id': '1', 'name': 'Test'}
    mock_table.get_item.assert_called_once()

@patch('boto3.resource')
def test_create_resource(mock_boto):
    """Test creating a new resource"""
    mock_table = MagicMock()
    mock_boto.return_value.Table.return_value = mock_table
    
    result = create_resource('test_table', {'id': '1', 'name': 'Test'})
    assert result is True
    mock_table.put_item.assert_called_once()

@patch('boto3.resource')
def test_update_resource(mock_boto):
    """Test updating an existing resource"""
    mock_table = MagicMock()
    mock_boto.return_value.Table.return_value = mock_table
    
    result = update_resource('test_table', '1', {'name': 'Updated'})
    assert result is True
    mock_table.update_item.assert_called_once()