import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    firstName = Column(String(15), nullable=False)
    lastName = Column(String(15), nullable=False)
    username = Column(String(15), nullable=False)
    age = Column(Integer, nullable=False)
