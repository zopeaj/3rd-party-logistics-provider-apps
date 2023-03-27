import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.models.Driver import Driver
from app.crud.repository.DriverRepository import DriverRepository

class DriverService:
    def __init__(self, driverRepository):
        self.driverRepository = driverRepository

    def receive_trip_details(self):
        pass

    def proceed(self):
        pass

    def cancel(self):
        pass
