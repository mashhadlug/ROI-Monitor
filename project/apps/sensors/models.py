from sqlalchemy import Column, Integer, String, DateTime
from project.database import Base

class Sensor(Base):
    __tablename__ = 'sensors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    created_at = Column(DateTime)
    created_by = Column(String(50))
    modified_at = Column(DateTime)
    modified_by = Column(String(50))
    pin = Column(Integer)

    def __init__(self, name=None, created_at=None, created_by=None, modified_at=None ,modified_by=None, pin=None):
        self.name = name
        self.created_at = created_at
        self.created_by = created_by
        self.modified_at = modified_at
        self.modified_by = modified_by
        self.pin = pin

class Log(Base):
    __tablename__ = 'status_log'
    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer)
    created_at = Column(DateTime)
    change_from = Column(Integer)
    value = Column(Integer)

    def __init__(self, sensor_id=None, created_at=None, change_from=None, value=None):
        self.sensor_id = sensor_id
        self.created_at = created_at
        self.change_from = change_from
        self.value = value
