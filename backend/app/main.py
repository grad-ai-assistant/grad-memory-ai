from fastapi import FastAPI

app = FastAPI(title="Grad Memory AI Backend")

@app.get("/")
def root():
    return {"message": "Grad Memory AI backend running"}