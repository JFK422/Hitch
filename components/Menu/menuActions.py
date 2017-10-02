from PyQt5 import QtGui, QtCore, QtWidgets
from components import introductionWindow
from projectHandling import startupData
from components import create
import colorama as clr
import os

class MenuAction:
    selecedProject = ""

    #Menu file tab
    def newFile(self):
        print("new file")

    def openFile(self):
        print("open file")

    #Open a file selector in oder to open a project. Afterwards add it to the list, requires launch to be clicked afterwards
    def openProjectFromFile(self):
        print("menuActions; MenuAction; openProjectFromFile: open project from file")
        self.filePath = QtWidgets.QFileDialog.getOpenFileName(self, "Open Project From File")
        if not(self.filePath[0] == ""):
            introductionWindow.Introduction.setProjectInfo(self, "fromFile", self.filePath[0])

    #Select the folder in which the project should be created
    def selectProjectFolder(self):
        print("selecting project folder")
        self.selectFilePath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder"))
        print(self.selectFilePath)
        if not(self.selectFilePath == ""):
            self.selectFilePath += "/"
            introductionWindow.Introduction.setProjectInfo(self, "fromCreate", self.selectFilePath)

    #Launch Button: Causes the project to be launched!
    def launchProject(self):
        print("menuActions; MenuAction; launchProject: Launching Project")
        intro = introductionWindow.Introduction
        #Check which tab was open and open the path.
        #Open one of the latest projects
        if intro.infoTabOpen:
            if intro.selectedProject != "":
                project = open(intro.selectedProject, "r+")
                name = os.path.splitext(os.path.basename(intro.selectedProject))[0]
                startupData.Data.insert(self, name, intro.selectedProject)
                project.close()
                create.CreateUI.openProject = intro.selectedProject
                create.CreateUI.openProjectInEditor(self)
                self.hide()
                #Add the project loading setup here later!

            else:
                print(clr.Fore.RED + "menuActions; MenuAction; launchProject: Error launching project! No name or path defined!")
                print(clr.Style.RESET_ALL)

        #Create a new project and open it
        else:
            name = intro.nameEdit.text()
            file = intro.pathEdit.text()
            if name != "" and file != "":
                #Add the new projet to the list of the latest projects
                try:
                    project = open(file + name + "/" + name + ".hth", "w+")
                    os.makedirs(file + name + "/Assets")
                    project.close()
                except:
                    os.makedirs(file + name + "/")
                    project = open(file + name + "/" + name + ".hth", "w+")
                    os.makedirs(file + name + "/Assets")
                startupData.Data.insert(self, name, file + name + "/" + name + ".hth")
                create.CreateUI.openProject = file + name + "/" + name + ".hth"
                project.write("name={0}\n".format(name))
                project.write("assets={0}\n".format(file + name + "/Assets/"))
                project.close()
                create.CreateUI.openProjectInEditor(self)
                self.hide()
                #Split with ', may be hard to see with some fonts!

            else:
                print(clr.Fore.RED + "menuActions; MenuAction; launchProject: Error launching project! No name or path defined!")
                print(clr.Style.RESET_ALL)

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