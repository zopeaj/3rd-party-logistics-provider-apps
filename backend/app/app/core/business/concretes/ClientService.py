import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

class ClientService:
    def __init__(self, userRepository):
        self.userRepository = userRepository

    def scan_bill(self):
        pass

