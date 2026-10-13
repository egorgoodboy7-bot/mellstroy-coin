from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Разрешаем серверу отдавать абсолютно любые файлы из папки проекта (картинки, html и т.д.)
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/mellstroy.png")
def get_image():
    return FileResponse("mellstroy.png")