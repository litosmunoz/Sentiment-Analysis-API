import sqlalchemy as alch
import os
from dotenv import load_dotenv

load_dotenv()

# Establishing connection
password = os.getenv('sqlpassword')
dbName = "tweets"
connectionData = f"mysql+pymysql://root:{password}@127.0.0.1/{dbName}"
engine = alch.create_engine(connectionData)