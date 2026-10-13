from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/mellstroy.png")
def get_image():
    return FileResponse("mellstroy1.png")