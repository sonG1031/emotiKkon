import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image

# 이미지 불러옴, PIL 포멧으로 변환
img = cv2.imread('meAndHyo.jpeg')
img_pil = Image.fromarray(img)

# 작업에 필요한 변수 세팅
scale = 100
font = ImageFont.truetype("Arita-buriM.otf", scale)
text = "송\n민\n섭"


# 텍스트 정렬 작업
draw = ImageDraw.Draw(img_pil)
_, _, w, h = draw.textbbox((0,0), text, font=font)



# 가로 가운데, 세로 가운데
# textX = (img.shape[1] - w) / 2
# textY = (img.shape[0] - h) / 2

# 가로 가운데, 세로 아래
# textX = (img.shape[1] - w) / 2
# textY = img.shape[0] - h

# 가로 가운데, 세로 위
# textX = (img.shape[1] - w) / 2
# textY = 0

# 가로 왼쪽, 세로 가운데
# textX = 0
# textY = (img.shape[0] - h) / 2

# 가로 왼쪽, 세로 아래
# textX = 0
# textY = img.shape[0] - h

# 가로 오른쪽, 세로 가운데
# textX = img.shape[1] - w
# textY = (img.shape[0] - h) / 2

# 가로 오른쪽, 세로 아래
# textX = img.shape[1] - w
# textY = img.shape[0] - h

# 가로 오른쪽, 세로 위
textX = img.shape[1] - w
textY = 0



# 텍스트 삽입
draw.text((textX, textY), text, (255,255,255), font=font)

# 다시 넘파이 배열로 변경
img = np.array(img_pil)

# 화면 띄우기
cv2.imshow('image', img)
cv2.waitKey()
