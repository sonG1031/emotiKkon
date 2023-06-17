import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image


class HandleImg:
    # 작업에 필요한 변수 세팅
    __fontsize = 1
    __row_img_fraction = 0.8  # 이미지에 차지할 정도
    __col_img_fraction = 0.1
    __font_path = "../fonts/SUITE-SemiBold.ttf"
    __font = ImageFont.truetype(__font_path, __fontsize)
    __textX = 0
    __textY = 0

    def __init__(self, text, file, align: dict[str, str]=None):
        if align is None:
            self.align = {'row': 'center', 'col': 'bottom'}
        else:
            self.align = align
        self.text = text
        # self.file = file
        self.img_pil = Image.open(file)
        self.draw = ImageDraw.Draw(self.img_pil, 'RGBA')


    # 이 클래스의 main 함수같은 느낌
    async def make_emotikkon(self, bg: bool=False):
        await self.__set_fontsize()
        await self.__align_text()

        if bg:
            await self.__add_background()

        await self.__put_text()
        return self.img_pil

    # 1. 반응형 폰트 크기 설정
    async def __set_fontsize(self):
        row_end = self.__row_img_fraction * self.img_pil.size[0]
        col_end = self.__col_img_fraction * self.img_pil.size[1]
        jumpsize = 75
        while True:
            if self.__font.getbbox(self.text)[2] < row_end and self.__font.getbbox(self.text)[3] < col_end:
                self.__fontsize += jumpsize
            else:
                jumpsize = jumpsize // 2
                self.__fontsize -= jumpsize
            self.__font = ImageFont.truetype(self.__font_path, self.__fontsize)
            if jumpsize <= 1:
                break


    # 2. 텍스트 정렬 작업
    async def __align_text(self):
        _, _, w, h = self.draw.textbbox((0, 0), self.text, font=self.__font)  # 뒷배경을 채우기 위해 bbox 사용
        row_padding = self.img_pil.size[0] * 0.05
        col_padding = self.img_pil.size[1] * 0.05

        if self.align['row'] == 'center':
            self.__textX = (self.img_pil.size[0] - w) / 2
        elif self.align['row'] == 'right':
            self.__textX = self.img_pil.size[0] - w - row_padding
        elif self.align['row'] == 'left':
            self.__textX = 0 + row_padding

        if self.align['col'] == 'mid':
            self.__textY = (self.img_pil.size[1] - h) / 2
        elif self.align['col'] == 'bottom':
            self.__textY = self.img_pil.size[1] - h - col_padding
        elif self.align['col'] == 'top':
            self.__textY = 0


    # 텍스트 뒷배경 추가(텍스트 삽입보다 먼저 호출해야함!!)
    async def __add_background(self):
        box_color_RGBA = (0, 0, 0, 255)
        fill_color_RGBA = (0, 0, 0, 255)

        l, t, r, b = self.draw.textbbox((self.__textX, self.__textY), self.text, font=self.__font)  # (left,top,right,bottom)
        bbox_row_padding = r * 0.02
        bbox_col_padding = r * 0.02
        l = l - bbox_row_padding
        r = r + bbox_row_padding
        t = t - bbox_col_padding
        b = b + bbox_col_padding

        self.draw.rectangle((l, t, r, b), outline=box_color_RGBA, fill=fill_color_RGBA)

    # 마지막! 텍스트 삽입
    async def __put_text(self):
        self.draw.text((self.__textX, self.__textY), self.text, (255, 255, 255), font=self.__font)