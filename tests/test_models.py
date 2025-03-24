import pytest
from datetime import datetime
from models import LegalResource, Hospital, NGO, EmergencyContact

def test_legal_resource_creation():
    """Test LegalResource model creation"""
    resource = LegalResource(
        id="1",
        name="Legal Aid Society",
        description="Free legal services",
        contact="1-800-LEGAL-AID",
        hours="9AM-5PM",
        website="https://example.com",
        services=["Family Law", "Criminal Defense"],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    assert resource.id == "1"
    assert resource.name == "Legal Aid Society"
    assert len(resource.services) == 2

def test_hospital_creation():
    """Test Hospital model creation"""
    hospital = Hospital(
        id="1",
        name="City Hospital",
        description="Emergency medical services",
        emergency_contact="911",
        address="123 Main St",
        is_24_7=True,
        services=["Emergency", "Trauma Care"],
        latitude=40.7128,
        longitude=-74.0060,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    assert hospital.id == "1"
    assert hospital.is_24_7 is True
    assert len(hospital.services) == 2

def test_ngo_creation():
    """Test NGO model creation"""
    ngo = NGO(
        id="1",
        name="Women's Support Network",
        description="Support for women in need",
        services=["Counseling", "Shelter"],
        contact="support@wsn.org",
        phone="1-800-SUPPORT",
        hours="24/7",
        address="456 Help St",
        website="https://wsn.org",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    assert ngo.id == "1"
    assert ngo.name == "Women's Support Network"
    assert len(ngo.services) == 2

def test_emergency_contact_creation():
    """Test EmergencyContact model creation"""
    contact = EmergencyContact(
        id="1",
        name="Jane Doe",
        phone="1-234-567-8900",
        relationship="Sister",
        is_primary=True,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    assert contact.id == "1"
    assert contact.is_primary is True