import os
import sys
from dotenv import load_dotenv


from sqlalchemy import Column, String, Integer
from app.app.db.base_class import Base

class Finance(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_no = Column(Integer, nullable=False)
    calculate_costs = Column(Integer, nullable=False)
    generate_bill = Column(String, nullable=False)
    validate_payments = Column(Integer, nullable=False)

    def calculate_costs(self):
        pass

    def generate_bill(self):
        pass

    def validate_payments(self):
        pass
