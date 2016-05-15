#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

im = Image.open('thumbnail.jpg')

im2 = im.filter(ImageFilter.SHARPEN)
im2.save('detail.jpg', 'jpeg')