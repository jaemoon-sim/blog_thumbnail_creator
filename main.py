#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request, send_file
from io import BytesIO
import thumbnail

app = Flask(__name__)

@app.route("/thumbnail")
def thumbnail_creator():
    title = request.args.get("title")
    tc = thumbnail.ThumbnailCreator(title.strip().split())
    img_io = BytesIO()
    tc.save(img_io)
    img_io.seek(0)
    return send_file(img_io, mimetype="image/jpeg")

if __name__=="__main__":
    app.run("0.0.0.0", port="8080")
