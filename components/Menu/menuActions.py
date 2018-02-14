from PyQt5 import QtGui, QtCore, QtWidgets
from components import introductionWindow
from components.fileManager import directoryItem
from projectHandling import startupData
from components import create
import colorama as clr
import os

class MenuAction:
    #Menu file tab
    #Open a file selector in oder to open a project. Afterwards add it to the list, requires launch to be clicked afterwards
    def openProjectFromFile(self):
        print("menuActions; MenuAction; openProjectFromFile: open project from file")
        self.filePath = QtWidgets.QFileDialog.getOpenFileName(self, "Open Project From File", "/home", "Hitch project file (*.hthp)")
        if not(self.filePath[0] == ""):
            prjFile = open(self.filePath[0], "r")
            name = prjFile.read().split("\n")[0].split("=")[1]
            prjFile.close()
            startupData.Data.insert(self, name, self.filePath[0])
            introductionWindow.Introduction.crl.refreshCarousel(self)

    #Select the folder in which the project should be created
    def selectProjectFolder(self):
        print("menuActions; MenuAction; selectProjectFolder: selecting project folder")
        self.selectFilePath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder"))
        print(self.selectFilePath)
        if not(self.selectFilePath == ""):
            self.selectFilePath += "/"
            introductionWindow.Introduction.pathEdit.setText(self.selectFilePath)


    #Launch Button: Causes the project to be launched!
    def launchProject(self, prjSelectTabOpen, currentPos, prjPathList, prjNotFoundIndexList):
        print("menuActions; MenuAction; launchProject: Attempting to launch project")
        intro = introductionWindow.Introduction
        #Check which tab was open and open the path.
        #Open one of the latest projects
        if prjSelectTabOpen:
            #Open the project file and catch it if it cant be found in the designated path
            #try:
            project = open(prjPathList[currentPos], "r+")
            name = os.path.splitext(os.path.basename(prjPathList[currentPos]))[0]
            startupData.Data.insert(self, name, prjPathList[currentPos])
            project.close()
            create.CreateUI.openProject = prjPathList[currentPos]

            #Check if the assets path in the main project file is still correct
            #Get the assets path from the current file
            try:
                f = open(prjPathList[currentPos], "r")
                text = f.read()
                f.close()
                assetsDir = text.split("\n")[1].split("=")[1].split("/")
                assetsDir.pop(len(assetsDir)-1)
                prjDir = prjPathList[currentPos].split("/")
                print(assetsDir)
                print(prjDir)
                samePath = True
                for k in range(len(assetsDir)-1):
                    if not(assetsDir[k] == prjDir[k]):
                        samePath = False
            
                if samePath:
                    assetsDir.pop(0)
                    for n in range(len(assetsDir)):
                        create.CreateUI.prjAssetsDir += "/"
                        create.CreateUI.prjAssetsDir += assetsDir[n]
                    create.CreateUI.prjAssetsDir += "/"
                    create.CreateUI.currentDir = create.CreateUI.prjAssetsDir

                    create.CreateUI.openProjectInEditor(self, "refresh")
                    self.hide()
                    print(clr.Fore.GREEN + "menuActions; MenuAction; launchProject: Launched project at {0} sucessfully!".format(prjPathList[currentPos])+ clr.Style.RESET_ALL)
            
                else:
                    print(clr.Fore.RED + "menuActions; MenuAction; launchProject: Unable to launch project due to missmatch of project and assets path in project file! Please fix manually!" + clr.Style.RESET_ALL)
                    launchProject.showErrorDialog(self, "Unable to launch project due to missmatch of project\n and assets path in project file! Please fix manually!", "Path missmatch")
            
            except:
                print(clr.Fore.RED + "menuActions; MenuAction; launchProject: Error launching project! No project defined!" + clr.Style.RESET_ALL)
                introductionWindow.Introduction.projNotFound(self, prjPathList[currentPos])
            
        #Create a new project and open it
        else:
            name = intro.nameEdit.text()
            file = intro.pathEdit.text()
            if name != "" and file != "":
                #Add the new projet to the list of the latest projects
                try:
                    project = open(file + name + "/" + name + ".hthp", "w+")
                    os.makedirs(file + name + "/Assets")
                    mainFile = open(file + name + "/Assets/main" + ".hth", "w+")
                except:
                    os.makedirs(file + name + "/")
                    project = open(file + name + "/" + name + ".hthp", "w+")
                    os.makedirs(file + name + "/Assets")
                    mainFile = open(file + name + "/Assets/main" + ".hth", "w+")
                mainFile.close()
                os.makedirs(file + name + "/Resources")
                startupData.Data.insert(self, name, file + name + "/" + name + ".hthp")
                create.CreateUI.openProject = file + name + "/" + name + ".hthp"
                create.CreateUI.mainProjectFile = file + name + "/Assets/main" + ".hth"
                project.write("name={0}\n".format(name))
                project.write("assets={0}\n".format(file + name + "/Assets/"))
                project.write("mainFile={0}\n".format(file + name + "/Assets/main.hth"))
                project.write("projImg={0}".format(file + name + "/Resources/titleImg.jpg"))
                project.close()
                create.CreateUI.openProjectInEditor(self, "refresh")
                self.hide()
                print(clr.Fore.GREEN + "menuActions; MenuAction; launchProject: Created project at {0} sucessfully!".format(prjPathList[currentPos])+ clr.Style.RESET_ALL)

            else:
                print(clr.Fore.YELLOW + "menuActions; MenuAction; launchProject: Error launching project! No name or path defined!" + clr.Style.RESET_ALL)
                MenuAction.showErrorDialog(self, "Error! No name or path defined!", "No name or path defined!")

    def showErrorDialog(self, message, title):
        infoDialog = QtWidgets.QMessageBox()
        infoDialog.setWindowTitle(title)
        infoDialog.setText(message)
        infoDialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        dial = infoDialog.exec_()

    def saveFile(self, path):
        print("saving file @{0}".format(path))

    def saveAllFiles(self):
        print("save all files")

    def projectSettings(self):
        print("project settings")

    def editorSettings(self):
        print("editor settings")

    def switchProject(self):
        print("switch project")

    def createNewFile(self):
        print("menuActions; MenuAction; createnewFile: Creating new file!")
        create.CreateUI.openProjectInEditor(self, "create")
        #create.CreateUI.vFileExplorer.addWidget(item, Create.CreateUI.row, Create.CreateUI.index)