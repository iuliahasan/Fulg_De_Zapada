import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def init_pool():
    oracledb.create_pool(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        min=1,
        max=10,
        pool_alias="new_pool"
    )

def get_connection():
    return oracledb.connect(pool_alias="new_pool")

def release_connection(connection):
    if connection:
        connection.close()

def close_pool():
    try:
        pool = oracledb.get_pool("new_pool")

        if pool:
            pool.close()
            print("Pool inchis cu succes")
    except oracledb.Error:
        pass