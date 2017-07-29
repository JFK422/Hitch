from pathlib import Path
from components import create
import os

class Data:
    compMode = None
    lastProjects = None
    lastProjNames = None

    def __init__(self):
        print("workareaData; Data; init: INIT_CALLED")
    
    def readTemp(self):
        print("workareaData; Data; readTemp: Reading temp files")

        Data.fileExists(self)
        tempFile = open("./Data/Temp/EditorTemp.tmp", "r+")
        tmpFileText = tempFile.read()
        listOfTemp = tmpFileText.split(":")
        Data.compMode = listOfTemp[0]
        Data.lastProjects = listOfTemp[1].split(";")
        Data.lastProjNames = listOfTemp[2].split(";")
        tempFile.close()

    def storeTemp(self, type, data="", filename = ""):
        print("workareaData; Data; storeTemp: Storing temp files")

        if type == "compMode":
            Data.compMode = data

        elif type == "lastProjects":
                Data.lastProjects.insert(data, 0)
                Data.lastProjNames.insert(filename, 0)

                if len(Data.lastProjects) > 6 or len(Data.lastProjNames) > 6:
                    Data.lastProjects.pop(7)
                    Data.lastProjNames.pop(7)
            
        Data.saveTemp(self)

    def saveTemp(self):
        tempSave = ""
        tempSave += Data.compMode
        tempSave += ":"
        for i in range(len(Data.lastProjects)):
            tempSave += Data.lastProjects[i]
            tempSave += ";"
        tempSave += ":"
        for i in range(len(Data.lastProjNames)):
            tempSave += Data.lastProjNames[i]
            tempSave += ";"
        
        tempFile = open("./Data/Temp/EditorTemp.tmp", "w+")
        tempFile.write(tempSave)
        tempFile.close()

    def fileExists(self):
        if not(os.path.isfile("./Data/Temp/EditorTemp.tmp")):
            unpresentFile = open("./Data/Temp/EditorTemp.tmp", "w+")
            unpresentFile.write("::")
            unpresentFile.close()

    def createFileTabs(self):
        print("workareaData; Data; createFileTabs: Creating editor tabs from open files")