from fastapi import FastAPI
import mysql.connector
import os

app = FastAPI()

# AWS RDS MySQL connection details
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI on AWS Lambda with RDS!"}

@app.get("/test-db-connection/")
def test_db_connection():
    try:
        conn = get_db_connection()
        conn.close()
        return {"status": "Connection successful"}
    except Exception as e:
        return {"error": str(e)}    

# AWS Lambda handler
from mangum import Mangum
handler = Mangum(app)
