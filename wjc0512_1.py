#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random#随机产生伪造随机数

def rndChar():
    return chr(random.randint(65, 90))#返回一个数值为N,N的范围为65<=N<90中的一个随机数

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))#创建一张图片
#image = Image.new('RGB', (240, 60), (255, 255, 255))

font = ImageFont.truetype('Arial.ttf', 36)#创建Font的对象，用于验证码文字中的输出

draw = ImageDraw.Draw(image)#先定义ImageDraw.Draw函数，这样后续调用方法的时候就可以简写了

#要绘制每一个像素的颜色，所以所以颜色填充长跟宽的高度都要循环填充一遍
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

#输出文字：输出文字的坐标轴，输出的文字，文字的类型，文字的颜色
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
