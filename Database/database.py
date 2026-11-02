import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return oracledb.Connection(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        service_name=os.getenv("DB_SERVICE")
    )