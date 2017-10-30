import os
from PIL import Image
import numpy

class TestImport(object):
    """description of class"""
    def __init__(self):
        self.datas = []
    def initialByImage(self, dir):
        for filename in os.listdir(dir):
                imgPath = os.path.join(dir, filename)
                img = Image.open(imgPath)
                img = img.convert('L').resize((28,28))
                width, height = img.size
                img = numpy.asarray(img, dtype='float64') / 256
                temp = img.reshape(1, height * width)[0]
                self.datas.append(temp)
        self.dataSize = len(self.datas)

