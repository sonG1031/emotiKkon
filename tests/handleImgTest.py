import asyncio
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # tools.HandleImg 임포트 오류 해결
from tools.HandleImg import HandleImg


async def main():
    handler = HandleImg('힣', 'https://blog.kakaocdn.net/dn/dowIkh/btrdtJZG3Eh/74NuD1tiFw7QzhqxOZ2Po0/img.png')

    print(handler.align)
    img_pil = await handler.make_emotikkon(bg=True)

    img_pil.show()


if __name__ == "__main__":
    asyncio.run(main())

