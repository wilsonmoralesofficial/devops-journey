from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Prueba 2 CI/CD"}

@app.get("/salud")
def salud():
    return {"estado": "ok"}