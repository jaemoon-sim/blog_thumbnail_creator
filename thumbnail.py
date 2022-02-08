#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import random
import sys

class ThumbnailCreator():
    space_between_lines = 10
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

        totH += self.space_between_lines*(len(texts)-1)
        self.im = Image.new("RGB", (maxW, totH))
       
        upper_color = self.randomColor()
        lower_color = self.randomColor()
        self.gradation(upper_color, lower_color)
        draw = ImageDraw.Draw(self.im)
        draw.multiline_text((0,0), "\n".join(texts), font=fnt, fill=(255, 255, 255), 
                                align="left", spacing=self.space_between_lines)

    def show(self):
        self.im.show()

    def save(self, path):
        self.im.save(path, "JPEG")

    def randomColor(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def gradation(self, upper_color, lower_color):
        (w,h) = self.im.size
        pxs = self.im.load()
        for y in range(h):
            r = ((h-y) * lower_color[0] + y * upper_color[0]) / h
            g = ((h-y) * lower_color[1] + y * upper_color[1]) / h
            b = ((h-y) * lower_color[2] + y * upper_color[2]) / h
            for x in range(w):
                pxs[x,y] = (int(r), int(g), int(b))
