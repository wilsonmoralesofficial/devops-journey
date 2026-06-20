from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Prueba Kubernetes "}

@app.get("/salud")
def salud():
    return {"estado": "ok"}