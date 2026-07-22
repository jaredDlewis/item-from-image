from fastapi import FastAPI

app = FastAPI(title="item-from-image")


@app.post("/image")
def read_root() -> dict[str, str]:
    # if Content-Type indicates raw image, conver to 
    # if Content-Type mentions base64, handle as base64
    return {"message": "Hello, world!"}
