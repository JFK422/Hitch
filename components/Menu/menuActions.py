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