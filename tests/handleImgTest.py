import asyncio
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # schemas.HandleImg 임포트 오류 해결
from schemas.HandleImg import HandleImg


async def main():
    handler = HandleImg('흐규흐규', './testImg/moon.jpeg')

    print(handler.align)
    img_pil = await handler.make_emotikkon(bg=True)

    img_pil.show()


if __name__ == "__main__":
    asyncio.run(main())

