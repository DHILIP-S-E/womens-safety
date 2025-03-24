from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class LegalResource:
    id: str
    name: str
    description: str
    contact: str
    hours: str
    website: str
    services: List[str]
    created_at: datetime
    updated_at: datetime

@dataclass
class Hospital:
    id: str
    name: str
    description: str
    emergency_contact: str
    address: str
    is_24_7: bool
    services: List[str]
    latitude: float
    longitude: float
    created_at: datetime
    updated_at: datetime

@dataclass
class NGO:
    id: str
    name: str
    description: str
    services: List[str]
    contact: str
    phone: str
    hours: str
    address: str
    website: str
    created_at: datetime
    updated_at: datetime

@dataclass
class EmergencyContact:
    id: str
    name: str
    phone: str
    relationship: str
    is_primary: bool
    created_at: datetime
    updated_at: datetime