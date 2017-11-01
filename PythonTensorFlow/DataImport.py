import os
from PIL import Image
import numpy
import random

class DataImport(object):
    """description of class"""

    def __init__(self):
        self.datas = []

    def initialByImage(self, path, labelCount, trainPercent):
        self.labelCount = labelCount
        self.trainPercent = trainPercent

        for dir in os.listdir(path):
            for filename in os.listdir(os.path.join(path, dir)):
                imgPath = os.path.join(os.path.join(path, dir), filename)
                # print(imgPath)
                img = Image.open(imgPath)
                img = img.convert('L').resize((28,28))
                width, height = img.size
                img = numpy.asarray(img, dtype='float64') / 256
                temp = img.reshape(1, height * width)[0]
                temp = numpy.hstack((dir, temp))
                self.datas.append(temp)
        self.dataSize = len(self.datas)
        #self.generateTrainAndValidate()

    def generateTrainAndValidate(self):
        random.shuffle(self.datas)
        self.inputs = []
        self.outputs = []
        for index in range(self.dataSize):
            tempOut = [0 for x in range(0, self.labelCount)]
            for num in range(self.labelCount):
                if ((num + 1) == self.datas[index][0]):
                    tempOut[num] = 1
            self.outputs.append(tempOut)
            self.inputs.append((self.datas[index])[1:])
        self.trainSize = int(self.dataSize * self.trainPercent)
        self.trainInputs = [];
        self.trainOutputs = [];
        self.trainCursor = 0;
        # train validate
        for index in range(self.trainSize):
            self.trainInputs.append(self.inputs[index])
            self.trainOutputs.append(self.outputs[index])

        self.validateInputs = [];
        self.validateOutputs = [];
        self.validateSize = self.dataSize - self.trainSize;
        for index in range(self.validateSize):
            self.validateInputs.append(self.inputs[index + self.trainSize])
            self.validateOutputs.append(self.outputs[index + self.trainSize])
        #print(self.dataSize)
        #print(self.trainSize)
        #print(self.validateSize)

    def generateTrain(self):
        random.shuffle(self.datas)
        self.inputs = []
        self.outputs = []
        for index in range(self.dataSize):
            tempOut = [0 for x in range(0, self.labelCount)]
            for num in range(self.labelCount):
                if ((num + 1) == self.datas[index][0]):
                    tempOut[num] = 1
            self.outputs.append(tempOut)
            self.inputs.append((self.datas[index])[1:])
        return [self.inputs, self.outputs]

    def saveDataToLocal(self, path):
        file = open(path, 'w+')
        print(self.dataSize, file=file)
        for index in range(self.dataSize):
            print(len(self.datas[index]), file=file)
            for num in range(len(self.datas[index])):
                print(self.datas[index][num], file=file)
        file.close()

    def initialByTemp(self, path, labelCount, trainPercent):
        self.labelCount = labelCount
        self.trainPercent = trainPercent
        file = open(path, 'r')
        self.dataSize = int(float(file.readline()))
        for index in range(self.dataSize):
            tempLength = int(float(file.readline()))
            tempArray = []
            for num in range(tempLength):
                tempArray.append(float(file.readline()))
            self.datas.append(tempArray)
        file.close()

        self.generateTrainAndValidate()

    def next_batch(self, batch_size):
        resultArray = [[], []]
        step = 0
        while (step < batch_size and self.trainCursor < self.trainSize) :
            resultArray[0].append(self.trainInputs[self.trainCursor])
            resultArray[1].append(self.trainOutputs[self.trainCursor])
            step += 1
            self.trainCursor += 1
            if self.trainCursor == self.trainSize  :
                self.trainCursor = 0
        return resultArray

    #def getValidationInput(self):
    #    return self.validateInputs

    #def getValidateOutput(self):
    #    return self.validateOutputs
