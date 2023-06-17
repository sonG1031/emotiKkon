from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def make_emotikkon(kakao_request: dict):
    print(kakao_request)

    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "테스트 응답"
                    }
                }
            ]
        }
    }