from pathlib import Path

class Data:
    def __init__(self):
        print("workareaData; Data; init: INIT_CALLED")
    
    def readTemp(self):
        print("workareaData; Data; readTemp: Reading temp files")
        emptyList = []

        if Data.fileExists(self):        
            openFiles = open("../Data/Temp/openFiles.tmp", "r")
            tTempData = openFiles.read()
            lTempData = OpenFiles.split(";")
            return lTempData

        else: 
            return emptyList

    def storeTemp(self, type, data=""):
        print("workareaData; Data; storeTemp: Storing temp files")

        Data.fileExists(self)

        #Variables for the temp file which stores all currently open files
        openFiles = open("../Data/Temp/openFiles.tmp", "r+")
        tOpenFiles = openFiles.read()
        unsavedFiles = open("../Data/Temp/unsavedFiles.tmp", "r+")
        tUnsavedFiles = unsavedFiles.read()

        if type == "openFilesAdd":
            tOpenFiles += data
            openFiles.write(tOpenFiles)

        elif type == "openFilesRemove":
            currentOF = tOpenFiles.split(";")
            currentOF.remove(data)
            newOpenFiles = ""
            for i in range(len(currentOF)):
                newOpenFiles += currentOF[i]
            openFiles.write(newOpenFiles)
        
        elif type == "truncateTemp":
            truncTemp = open("../Data/Temp/openFiles.tmp", "w+")
            truncTemp.close()

        elif type == "compMode":
            self.compMode = data

        elif type == "unsavedFilesAdd":
            tUnsavedFiles += data
            unsavedFiles.write(tUnsavedFiles)


    def fileExists(self):
        tempOFPresent = Path("../Data/Temp/openFiles.tmp")
        tempUFPresent = Path("../Data/Temp/unsavedFiles.tmp")
        if tempOFPresent.is_file() and tempUFPresent:
            return True

        elif not(tempOFPresent.is_file()):
            print("workareaData; Data; fileExists: Temp open files not found, Creating it")
            #tempFile = open("../Data/Temp/openFiles.tmp", "w+")
            #tempFile.close()
            return False

        elif not(tempUFPresent.is_file()):
            print("workareaData; Data; fileExists: Temp unsaved files not found, Creating it")
            tempFile = open("../Data/Temp/unsavedFiles.tmp", "w+")
            tempFile.close()
            return False