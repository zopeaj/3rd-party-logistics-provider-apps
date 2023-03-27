import os
import sys
from dontenv import load_dotenv
load_dotenv()
path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import FastAPI
