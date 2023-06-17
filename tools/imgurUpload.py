from core.security import CLIENT_ID, CLIENT_SECRET
import requests
import os

async def upload_imgur(path):
    url = f"https://api.imgur.com/3/image?client_id={CLIENT_ID}"

    with open(path, 'rb') as fin:
        r = requests.post(url, files={"image": fin})

    os.remove(path)

    link = r.json()["data"]["link"]
    return link

