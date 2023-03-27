import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Integer

class Bill(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    contract_id = Column(Integer, nullable=False)
    amount_loaded = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)
    distance_travelled = Column(Integer, nullable=False)
    time_taken = Column(Integer, nullable=False)
