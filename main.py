from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def test():
    return {"msg": "test"}