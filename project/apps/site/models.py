from sqlalchemy import Column, Integer, String, DateTime
from project.database import Base

class Sensor(Base):
    __tablename__ = 'senseors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    created_at = Column(DateTime)
    created_by = Column(String(50))
    modified_at = Column(DateTime)
    modified_by = Column(String(50))

    def __init__(self, name=None, created_at=None, created_by=None, modified_at=None ,modified_by=None):
        self.name = name
        self.created_at = created_at
        self.created_by = created_by
        self.modified_at = modified_at
        self.modified_by = modified_by
