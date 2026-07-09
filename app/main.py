from fastapi import FastAPI

app = FastAPI(title="item-from-image")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, world!"}
