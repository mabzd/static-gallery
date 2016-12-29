#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import sys
import json

def category_decription(i):
    if i == 1:
        return u"Olej na płótnie"
    return u"Brak kategorii"

scriptFilePath = os.path.abspath(__file__)
scriptDirPath = os.path.dirname(scriptFilePath)
os.chdir(scriptDirPath)

with open(os.path.join(scriptDirPath, '..', 'api', 'paintings.json')) as file:    
    paintings = json.load(file)

for p in paintings:
    description = category_decription(p["category"]).encode('utf-8')
    size = "{0}cm x {1}cm".format(p["width"], p["height"])
    title = p["title"].encode('utf-8')

    print("<div class=\"tile img-tile\">")
    print("    <a href=\"galeria/olej-na-plotnie/{0}.jpg\" data-lightbox=\"{1}\">".format(p["number"], title))
    print("        <img src=\"galeria/olej-na-plotnie/thumb/{0}.jpg\" alt=\"{1}\" />".format(p["number"], title))
    print("    </a>")
    print("    <div class=\"label\">")
    print("        <h3>{0}</h3>".format(title))
    print("        <span class=\"description\">{0}, {1}</span>".format(description, size))
    print("    </div>")
    print("</div>")