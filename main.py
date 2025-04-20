from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

app = FastAPI()

# Database connection details
db_config = {
    "host": "prog8850-finalassignment-db",  # use the Docker service name
    "user": "root",
    "password": "password",
    "database": "students"
}

@app.get("/")
def root():
    return {"message": "Microfrontend is working with MySQL!"}

@app.get("/students")
def get_students():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        return {"students": result}
    except Error as e:
        return {"error": str(e)}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
