from components import create
import os
import colorama as clr

class Data:
    compMode = None
    lastProjects = None
    lastProjNames = None

    def __init__(self):
        print("workareaData; Data; init: INIT_CALLED")
    
    def readTemp(self):
        print("workareaData; Data; readTemp: Reading temp files")
        clr.init()

        #EditorTemp.tmp: Items seperated with doublepoints, then within those items, the items are sepereted by a semicolumn.
        #Compilemode:last;Project;Paths:last;Project;Names
        #Read the temp file and store it in variables.
        #Also check if it exists and create it if necessary.
        Data.fileExists(self)
        tempFile = open("./Data/Temp/EditorTemp.tmp", "r+")
        tmpFileText = tempFile.read()
        listOfTemp = tmpFileText.split(":")
        Data.compMode = listOfTemp[0]
        Data.lastProjects = listOfTemp[1].split(";")
        Data.lastProjNames = listOfTemp[2].split(";")
        tempFile.close()

    #Store the new temporary data in the designated variables, sorted by what needs to be updated.
    #Type can be compMode for updating the compile mode and lastProjects for updating the last opened projects.
    def storeTemp(self, type, data="", filename = ""):
        print("workareaData; Data; storeTemp: Storing temp files")

        if type == "compMode":
            Data.compMode = data

        elif type == "lastProjects":
                Data.lastProjects.insert(0, data)
                Data.lastProjNames.insert(0, filename)

                if len(Data.lastProjects) > 6 or len(Data.lastProjNames) > 6:
                    Data.lastProjects.pop(7)
                    Data.lastProjNames.pop(7)

        else:
            print(clr.Fore.RED + "workareaData; Data; readTemp: Error storing data!")
            print(clr.Style.RESET_ALL + "Clearing colour marking!")
            
        Data.saveTemp(self)

    def saveTemp(self):
        #Store the actual data to the temp file.
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
        #Check if the temp file exists and create it if not.
        if not(os.path.isfile("./Data/Temp/EditorTemp.tmp")):
            unpresentFile = open("./Data/Temp/EditorTemp.tmp", "w+")
            unpresentFile.write("::")
            unpresentFile.close()