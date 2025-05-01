import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) #Path to app folder
load_dotenv(os.path.join(BASE_DIR, '.env'), override=True) #Load .env

class Config:
    SQL_ALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')