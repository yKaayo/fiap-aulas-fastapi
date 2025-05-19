import oracledb
from dotenv import load_dotenv
import os

load_dotenv()

dsn = oracledb.makedsn("oracle.fiap.com.br", 1521, service_name="ORCL")
conn = oracledb.connect(user=os.getenv("DB_ORCL_USER"), password=os.getenv("DB_ORCL_PASSWORD"), dsn=dsn)

def create_user(username: str, email: str, password_hash: str):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO FASTAPI_CLASS_USER (USERNAME, EMAIL, PASSWORD_HASH)
        VALUES (:username, :email, :password_hash)
    """, [username, email, password_hash])
    conn.commit()
    cursor.close()

def get_user_by_username(username: str):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM FASTAPI_CLASS_USER WHERE USERNAME = :username", [username])
    result = cursor.fetchone()
    cursor.close()
    return result
