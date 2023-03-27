import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import String, Column, Integer, Date

class Trip(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    bill_id = Column(Integer, nullable=False)
    no_of_drop_offs = Column(Integer, nullable=False)
    no_of_helpers = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    trip_type = Column(String, nullable=False)
    pick_up_location = Column(String, nullable=False)
    drop_off_location = Column(String, nullable=False)


