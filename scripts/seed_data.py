import boto3
import json
import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dynamodb = boto3.resource('dynamodb')

def load_seed_data(filename):
    """Load seed data from JSON file."""
    data_path = Path(__file__).parent / 'seed_data' / filename
    with open(data_path) as f:
        return json.load(f)

def seed_legal_resources():
    """Seed legal resources table with initial data."""
    table = dynamodb.Table('legal_resources')
    data = load_seed_data('legal_resources.json')
    
    for item in data:
        item['created_at'] = datetime.utcnow().isoformat()
        item['updated_at'] = item['created_at']
        try:
            table.put_item(Item=item)
            logger.info(f"Added legal resource: {item['name']}")
        except Exception as e:
            logger.error(f"Error adding legal resource {item['name']}: {str(e)}")

def seed_hospitals():
    """Seed hospitals table with initial data."""
    table = dynamodb.Table('hospitals')
    data = load_seed_data('hospitals.json')
    
    for item in data:
        item['created_at'] = datetime.utcnow().isoformat()
        item['updated_at'] = item['created_at']
        try:
            table.put_item(Item=item)
            logger.info(f"Added hospital: {item['name']}")
        except Exception as e:
            logger.error(f"Error adding hospital {item['name']}: {str(e)}")

def seed_ngo_directory():
    """Seed NGO directory table with initial data."""
    table = dynamodb.Table('ngo_directory')
    data = load_seed_data('ngo_directory.json')
    
    for item in data:
        item['created_at'] = datetime.utcnow().isoformat()
        item['updated_at'] = item['created_at']
        try:
            table.put_item(Item=item)
            logger.info(f"Added NGO: {item['name']}")
        except Exception as e:
            logger.error(f"Error adding NGO {item['name']}: {str(e)}")

def main():
    """Seed all tables with initial data."""
    seed_legal_resources()
    seed_hospitals()
    seed_ngo_directory()

if __name__ == '__main__':
    main()