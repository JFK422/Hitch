from pathlib import Path
import os

class Data:
    def __init__(self):
        print("workareaData; Data; init: INIT_CALLED")
    
    def readTemp(self):
        print("workareaData; Data; readTemp: Reading temp files")

        Data.fileExists(self)
        tempFile = open("./Data/Temp/EditorTemp.tmp", "r+")
        tmpFileText = tempFile.read()
        listOfTemp = tmpFileText.split(":")
        self.openFiles = listOfTemp[0]
        self.compileMode = listOfTemp[1]
        self.unsavedFiles = listOfTemp[2]
        self.selectedFile = listOfTemp[3]
        self.uncompiledFiles = listOfTemp[4]
        tempFile.close()


    def storeTemp(self, type, data=""):
        print("workareaData; Data; storeTemp: Storing temp files")

        if type == "openFilesAdd":
            if self.openFiles == []:
                self.openFiles.append(data)
            else:
                self.openFiles.append(";{0}".format(data))

        elif type == "openFilesRemove":
            self.openFiles.remove(data)

        elif type == "compMode":
            self.compileMode = data

        elif type == "unsavedFilesAdd":
            if self.unsavedFiles == []:
                self.unsavedFiles.append(data)
            else:
                self.unsavedFiles.append(";{0}".format(data))

        elif type == "unsavedFilesRemove":
            self.unsavedFiles.remove(data)

        elif type == "uncompiledFilesAdd":
            if self.uncompiledFiles == []:
                self.uncompiledFiles.append(data)
            else:
                self.uncompiledFiles.append(";{0}".format(data))

        elif type == "uncompiledFilesRemove":
            self.uncompiledFiles.remove(data)

        elif type == "selectedFile":
            self.selectedFile = data

    def saveTemp(self):
        tempSave = ""
        for i in range(len(self.openFiles)):
            tempSave += self.openFiles[i]
        tempSave += ":"
        tempSave += self.compileMode
        tempSave += ":"
        for j in range(len(self.unsavedFiles)):
            tempSave += self.unsavedFiles[j]
        tempSave += ":"
        tempSave += self.selectedFile
        tempSave += ":"
        for k in range(len(self.uncompiledFiles)):
            tempSave += self.uncompiledFiles[k]

        tempFile = open("./Data/Temp/EditorTemp.tmp", "w+")
        tempFile.write(tempSave)
        tempFile.close()



    def fileExists(self):
        if not(os.path.isfile("./Data/Temp/EditorTemp.tmp")):
            unpresentFile = open("./Data/Temp/EditorTemp.tmp", "w+")
            unpresentFile.write("::::")
            unpresentFile.close()