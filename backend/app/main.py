# backend/app/main.py

from fastapi import FastAPI

app = FastAPI(
    title="Empathetic Counselor API"
)

@app.get("/")
def root():
    return {"message": "API Running"}