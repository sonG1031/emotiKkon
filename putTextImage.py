import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image


# 테스트 입력
text = input("text: ")
row, col = input("row,col >>> ").split(',')

# 이미지 불러옴, PIL 포멧으로 변환
img = cv2.imread('testImg/moon.jpeg')
img_pil = Image.fromarray(img)

# 작업에 필요한 변수 세팅
fontsize = 1
row_img_fraction = 0.8 # 이미지에 차지할 정도
col_img_fraction = 0.2
font_path = "Arita-buriM.otf"

font = ImageFont.truetype(font_path, fontsize)
row_end = row_img_fraction * img_pil.size[0]
col_end = col_img_fraction * img_pil.size[1]
jumpsize = 75
while True:
    if font.getbbox(text)[2] < row_end and font.getbbox(text)[3] < col_end:
        fontsize += jumpsize
    else:
        jumpsize = jumpsize // 2
        fontsize -= jumpsize
    font = ImageFont.truetype(font_path, fontsize)
    if jumpsize <= 1:
        break
print(img_pil.size, font.getbbox(text))


# 텍스트 정렬 작업
draw = ImageDraw.Draw(img_pil)
_, _, w, h = draw.textbbox((0,0), text, font=font)
row_padding = img_pil.size[0] * 0.05
col_padding = img_pil.size[1] * 0.05

textX, textY = 0, 0
if row == 'center':
    textX = (img_pil.size[0] - w) / 2
elif row == 'right':
    textX = img_pil.size[0] - w - row_padding
elif row == 'left':
    textX = 0 + row_padding

if col == 'mid':
    textY = (img_pil.size[1] - h) / 2
elif col == 'bottom':
    textY = img_pil.size[1] - h - col_padding
elif col == 'top':
    textY = 0

print((textX, textY))
# 텍스트 삽입
draw.text((textX, textY), text, (255,255,255), font=font)

# 다시 넘파이 배열로 변경
img = np.array(img_pil)

# 화면 띄우기
cv2.imshow('image', img)
cv2.waitKey()
