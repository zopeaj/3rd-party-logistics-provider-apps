import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Integer, Date

class Contract(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    contract_type = Column(String, nullable=False)
    legal_terms = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    duration = Column(Integer, nullable=False)
    payment_method = Column(String, nullable=False)

