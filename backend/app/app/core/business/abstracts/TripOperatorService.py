import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.models.TripOperator import TripOperator

class TripOperatorService:
    def __init__(self, tripOperatorRepository):
        self.tripOperatorRepository = tripOperatorRepository

    def receive_request(self):
        pass

    def send_request(self):
        pass

    def assign_trip_to_driver(self):
        pass

    def track_trip(self):
        pass

