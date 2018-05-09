#验证码图片识别
#import tesserocr
from PIL import Image

image = Image.open("./a.png")

#将图片转化为灰度图像
image = image.convert("L")
image.save("b.png",None)

#做二值化的处理
threshold = 127
table=[]
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
image.save("c.png",None)

#result = tesserocr.image_to_text(image)

print(result)
