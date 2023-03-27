import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Integer
from app.app.models.Driver import Driver
from app.app.models.Trip import Trip


class TripOperator(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    phone_no = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
    driver = Column(Driver)
    trip = Column(Trip)

    def requestDriver(self):
        pass

    def provideTripInformation(self):
        pass

    def trackTrip(self):
        pass

