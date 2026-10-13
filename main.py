from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            score INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

class TapData(BaseModel):
    clicks: int

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/api/tap")
def tap(data: TapData):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (user_id, score) VALUES (1, ?) ON CONFLICT(user_id) DO UPDATE SET score = score + ?",
        (data.clicks, data.clicks)
    )
    conn.commit()
    conn.close()
    return {"status": "ok"}