import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_legal_resources(client):
    """Test retrieving legal resources"""
    response = client.get('/api/legal-resources')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_get_hospitals(client):
    """Test retrieving hospitals"""
    response = client.get('/api/hospitals')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_get_ngo_directory(client):
    """Test retrieving NGO directory"""
    response = client.get('/api/ngo-directory')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_send_emergency_sms_duplicate(client):
    response = client.post('/api/send-emergency-sms-duplicate')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
