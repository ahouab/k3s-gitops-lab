from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "K3s GitOps Lab - FastAPI demo"}

@app.get("/version")
def read_version():
    return {"version": "v1"}
