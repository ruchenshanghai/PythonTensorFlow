import os
import re
from PIL import Image
import numpy

class TestImport(object):
    """description of class"""
    def __init__(self):
        self.datas = []
    def initialByImage(self, dir):
        nameList = []
        for filename in os.listdir(dir):
            nameList.append(filename)
        newList = sorted(nameList,key = lambda i:int(re.match(r'(\d+)',i).group()))
        #print(newList)
        index = 0
        length = len(newList)
        while (index < length):
                imgPath = os.path.join(dir, newList[index])
                #print(imgPath)
                img = Image.open(imgPath)
                img = img.convert('L').resize((28,28))
                width, height = img.size
                img = numpy.asarray(img, dtype='float64') / 256
                temp = img.reshape(1, 28 * 28)[0]
                self.datas.append(temp)
                index += 1

        #for filename in nameList:
        #        imgPath = os.path.join(dir, filename)
        #        print(imgPath)
        #        img = Image.open(imgPath)
        #        img = img.convert('L').resize((28,28))
        #        width, height = img.size
        #        img = numpy.asarray(img, dtype='float64') / 256
        #        temp = img.reshape(1, 28 * 28)[0]
        #        self.datas.append(temp)
        self.dataSize = len(self.datas)

