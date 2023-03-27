import os
import sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import FastAPI
from app.app.db.base import Base
from app.app.api.api_v1.endpoints.UserController import getUsers
