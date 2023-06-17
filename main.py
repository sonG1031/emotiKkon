from fastapi import FastAPI
from tools.HandleImg import HandleImg
from tools.imgurUpload import upload_imgur
from tools.kakaoUrl import kakaoUrlHandler

app = FastAPI()


@app.post("/")
async def make_emotikkon(kakao_request: dict):
    text = kakao_request['action']['params']['text']
    img_url = kakaoUrlHandler(kakao_request['action']['detailParams']['secureimage']['origin'])
    path = "./temp/" + text + '.jpg'

    handler = HandleImg(text, img_url)
    img = await handler.make_emotikkon(bg=True)
    img.save(path)

    res_url = await upload_imgur(path)

    return {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleImage": {
                    "imageUrl": res_url,
                    "altText": text + " 이모티꼰"
                }
            }
        ]
    }
}