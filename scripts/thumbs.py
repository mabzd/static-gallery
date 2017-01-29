import os
import sys
from PIL import Image

def print_immediate(str):
    print(str)
    sys.stdout.flush()

def PIL_thumb(root, file):
    im = Image.open(os.path.join(root, file))
    im.thumbnail((450, 1000), Image.ANTIALIAS)
    im.save(os.path.join(root, 'thumb', file.lower()), "JPEG")

def process_files(path):
    print_immediate('processing directory ' + path)
    excludedDirs = ['thumb']
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in excludedDirs]
        files[:] = [f for f in files if f.endswith(('.jpg', '.JPG'))]
        for file in files:
            print_immediate('Processing file ' + file)
            PIL_thumb(root, file)
            print_immediate('Processed file ' + file)

scriptFilePath = os.path.abspath(__file__)
scriptDirPath = os.path.dirname(scriptFilePath)
os.chdir(scriptDirPath)

process_files("../galeria/olej-na-plotnie")
