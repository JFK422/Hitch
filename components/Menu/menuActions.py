from PyQt5 import QtGui, QtCore, QtWidgets
from components import introductionWindow

class MenuAction:
    selecedProject = ""

    #Menu file tab
    def newFile(self):
        print("new file")

    def openFile(self):
        print("open file")

    def openProject(self):
        print("open project")
        self.filePath = QtWidgets.QFileDialog.getOpenFileName(self, "Open Project")
        if not(self.filePath[0] == ""):
            introductionWindow.Introduction.selectedProject = self.filePath[0]
            introductionWindow.Introduction.setProjectInfo(self, "fromFile")

    def selectProjectFolder(self):
        print("selecting project folder")
        self.selectFilePath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder"))
        if not(self.selectFilePath == ""):
            self.selectFilePath += "/"
            introductionWindow.Introduction.selectedFolder = self.selectFilePath
            introductionWindow.Introduction.setProjectInfo(self, "fromCreate")
            introductionWindow.Introduction.appendProjectName(self)

    def launchProject(self):
        print("launchingProject")
        intro = introductionWindow.Introduction

        if intro.infoTabOpen:
            if intro.selectedProject != "":
                project = open(intro.selectedProject, "r+")
                project.close()
        
        else:
            if intro.selectedFolder != "" and intro.selectedProjectName != "":
                name = intro.selectedProjectName
                file = intro.selectedFolder
                project = open(file + name + ".hth", "w+")
                project.close()

            else:
                print("Error")

    def saveFile(self):
        print("save file")

    def saveAllFiles(self):
        print("save all files")

    def projectSettings(self):
        print("project settings")

    def editorSettings(self):
        print("editor settings")

    def switchProject(self):
        print("switch project")