import os
import sys
from dotenv import load_dotenv
load_dotenv()
FILE_PATH = os.environ["FILE_PATH"]
sys.path.append(FILE_PATH)

from typing import List
from app.app.models.User import User

class UserRepository:
    def __init__(self,):
        pass

    def getAllUsers(self) -> List[User]:
        return [ { "id": 0, "firstName": "David", "lastName": "Smart", "username": "david@example.com", "age": 18}, {"id": 1, "firstName": "Samuel", "lastName": "Kaleb", "username": "kaleb@example.com", "age": 20}]

