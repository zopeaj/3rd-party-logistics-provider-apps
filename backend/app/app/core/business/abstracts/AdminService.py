import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

class AdminService:
    def __init__(self, userRepository):
        self.userRepository = userRepository

    def process_request_infor(self):
        pass

    def send_request_info_to_trip_operator(self):
        pass

