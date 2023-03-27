import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.models.Finance import Finance
from app.core.business.abstracts.UserService import UserService


class FinanceService:
    def __init__(self, userService):
        self.userService = userService

    def calculateCosts(self):
        pass

    def generateBill(self):
        pass

    def validatePayments(self):
        pass
