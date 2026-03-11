from fastapi import FastAPI

app = FastAPI()


@app.get("/contact")
def read_root():
    return {"Hello": "World"}

