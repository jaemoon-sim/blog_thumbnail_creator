#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import random
import sys

class ThumbnailCreator():
    def __init__(self, texts):
        fnt = ImageFont.truetype("./font.ttf", encoding="UTF-8", size=40)
        texts = [" "]+texts+[" "]
        print(texts) 
        totH = 0
        maxW = -1
        for s in texts:
            (w,h) = fnt.getsize(s)
            if w > maxW:
                maxW = w
            totH += h

        #  while fnt.getsize(texts[0])[0] < maxW:
            #  texts[0] += " "

        totH += 10*(len(texts)-2)
        self.im = Image.new("RGB", (maxW, totH))
       
        (w,h) = self.im.size
        pxs = self.im.load()
        color1 = randomColor()
        color2 = randomColor()
        for y in range(h):
            r = ((h-y) * color2[0] + y * color1[0]) / h
            g = ((h-y) * color2[1] + y * color1[1]) / h
            b = ((h-y) * color2[2] + y * color1[2]) / h
            for x in range(w):
                pxs[x,y] = (int(r), int(g), int(b))
        
        draw = ImageDraw.Draw(self.im)
        draw.multiline_text((0,0), "\n".join(texts), font=fnt, fill=(255, 255, 255), align="left", spacing=10)

    def show(self):
        self.im.show()

    def save(self, path):
        self.im.save(path, "JPEG")

def randomColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

