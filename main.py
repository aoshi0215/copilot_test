from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"hello world"}

@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"Hello {name}"}