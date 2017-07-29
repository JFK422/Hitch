import qtawesome as qta
import random, sys, os
from projectHandling import startupData
from components.Misc import projectItem
from components.Menu import menuActions
from PyQt5 import QtGui, QtCore, QtWidgets

#Menu widget placed in the stack of vLPart

class Introduction(QtWidgets.QWidget):
    vLastProjects = None
    selectedProject = ""
    selectedProjectName = ""
    selectedFolder = ""
    infoName = None
    infoPath = None
    infoTabOpen = True
    def __init__(self):
        super(Introduction, self).__init__()
        greetings = ["Hello Old Friend", 
                            "M' Lady", 
                            "Copy pasted Pseudocode", 
                            "Written in the language of snakes", 
                            "Has hidden ASCII art in the code", 
                            "The stylesheets consists mostly of linebreak } linebreak" ]
        self.setGeometry(50,50,700,500)
        self.setWindowTitle("Hitch")

        mainLay = QtWidgets.QVBoxLayout()
        mainLay.setAlignment(QtCore.Qt.AlignTop)
        mainLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        mainLay.setSpacing(0)

        titleLay = QtWidgets.QVBoxLayout()
        titleLay.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        titleLay.setContentsMargins(QtCore.QMargins(0,10,0,15))
        titleLayWid = QtWidgets.QWidget()
        titleLayWid.setObjectName("titlebar")
        titleLayWid.setLayout(titleLay)
        mainLay.addWidget(titleLayWid)

        hBottom = QtWidgets.QHBoxLayout()
        hBottom.setAlignment(QtCore.Qt.AlignTop)
        hBottom.setSpacing(5)
        hBottom.setContentsMargins(QtCore.QMargins(5,5,5,5))
        wBottom = QtWidgets.QWidget()
        wBottom.setLayout(hBottom)

        Introduction.vLastProjects = QtWidgets.QVBoxLayout()
        Introduction.vLastProjects.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        Introduction.vLastProjects.setContentsMargins(QtCore.QMargins(10,10,10,10))
        wLastProjects = QtWidgets.QWidget()
        wLastProjects.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding))
        wLastProjects.setMinimumWidth(170)
        wLastProjects.setObjectName("lastProjects")
        wLastProjects.setLayout(Introduction.vLastProjects)
        hBottom.addWidget(wLastProjects)

        self.sCenter = QtWidgets.QStackedLayout()
        self.sCenter.setAlignment(QtCore.Qt.AlignTop)
        wCenter = QtWidgets.QWidget()
        wCenter.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred))
        wCenter.setObjectName("lastProjects")
        wCenter.setLayout(self.sCenter)

        vInfo = QtWidgets.QVBoxLayout()
        vInfo.setAlignment(QtCore.Qt.AlignTop)
        wInfo = QtWidgets.QWidget()
        wInfo.setLayout(vInfo)
        self.sCenter.addWidget(wInfo)

        Introduction.infoName = QtWidgets.QLabel("")
        Introduction.infoName.setObjectName("infoText")
        Introduction.infoPath = QtWidgets.QLabel("")

        Introduction.infoPath.setObjectName("infoText")
        Introduction.infoPath.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding))
        Introduction.infoPath.setWordWrap(True)
        Introduction.infoPath.setAlignment(QtCore.Qt.AlignTop)

        vInfo.addWidget(Introduction.infoName)
        vInfo.addWidget(Introduction.infoPath)

        hBottom.addWidget(wCenter)

        hLaunch = QtWidgets.QVBoxLayout()
        hLaunch.setContentsMargins(QtCore.QMargins(10,10,10,10))
        wLaunch = QtWidgets.QWidget()
        wLaunch.setLayout(hLaunch)
        wLaunch.setObjectName("lastProjectsLaunch")

        #add the last opened projects as items
        for i in range(len(startupData.Data.lastProjNames)):
            projItem = projectItem.LastProjItem()
            projItem.setup(text = startupData.Data.lastProjNames[i], path = startupData.Data.lastProjects[i])
            Introduction.vLastProjects.addWidget(projItem)

        launchBtn = QtWidgets.QPushButton("Launch")
        launchBtn.setObjectName("launchProject")
        launchBtn.clicked.connect(lambda:menuActions.MenuAction.launchProject(self))
        hLaunch.addWidget(launchBtn)
        hBottom.addWidget(wLaunch)

        openBtn = QtWidgets.QPushButton("Open")
        openBtn.clicked.connect(lambda:menuActions.MenuAction.openProject(self))
        hLaunch.addWidget(openBtn)

        self.createBtn = QtWidgets.QPushButton("Create")
        self.createBtn.clicked.connect(lambda:Introduction.switchTab(self))
        hLaunch.addWidget(self.createBtn)

        gCreate = QtWidgets.QGridLayout()
        gCreate.setAlignment(QtCore.Qt.AlignTop)
        wCreate = QtWidgets.QWidget()
        wCreate.setLayout(gCreate)

        vBackLay = QtWidgets.QVBoxLayout()
        vBackLay.setAlignment(QtCore.Qt.AlignTop)
        wBackLay = QtWidgets.QWidget()
        wBackLay.setLayout(vBackLay)
        vBackLay.addWidget(wCreate)
        self.sCenter.addWidget(wBackLay)

        #Stuff for the tab on creating a new project
        nameLabel = QtWidgets.QLabel("Name: ")
        nameLabel.setObjectName("infoText")

        self.nameEdit = QtWidgets.QLineEdit()
        self.nameEdit.setObjectName("projectTextEdit")
        self.nameEdit.textChanged.connect(lambda:Introduction.appendProjectName(self))

        pathLabel = QtWidgets.QLabel("Path: ")
        pathLabel.setObjectName("infoText")

        self.pathEdit = QtWidgets.QLineEdit()
        self.pathEdit.setObjectName("projectTextEdit")
        self.pathEdit.textChanged.connect(lambda:Introduction.appendProjectName(self))
        
        folder = qta.icon("fa.folder", color="#f9f9f9")
        pathSelect = QtWidgets.QPushButton(folder, "")
        pathSelect.setIconSize(QtCore.QSize(20, 20))
        pathSelect.setMaximumSize(QtCore.QSize(30, 30))
        pathSelect.clicked.connect(lambda:menuActions.MenuAction.selectProjectFolder(self))
        pathSelect.setObjectName("launchProject")

        self.createSubfolder = QtWidgets.QCheckBox("Create in subfolder")
        self.createSubfolder.setObjectName("createSubfolder")
        self.createSubfolder.clicked.connect(lambda:Introduction.appendProjectName(self))

        infoLabel = QtWidgets.QLabel("Press launch to create the Project.")
        infoLabel.setObjectName("infoTextCreate")

        gCreate.addWidget(nameLabel, 0, 0)
        gCreate.addWidget(self.nameEdit, 0, 1)
        gCreate.addWidget(pathLabel, 1, 0)
        gCreate.addWidget(self.pathEdit, 1, 1)
        gCreate.addWidget(pathSelect, 1, 2)
        vBackLay.addWidget(self.createSubfolder)
        vBackLay.addWidget(infoLabel)

        title = QtWidgets.QLabel("Hitch")
        title.setObjectName("titleText")
        titleLay.addWidget(title)

        motd = QtWidgets.QHBoxLayout()
        motd.setAlignment(QtCore.Qt.AlignCenter)
        motd.setContentsMargins(QtCore.QMargins(0,0,0,10))
        motdw = QtWidgets.QWidget()
        motdw.setObjectName("titlebar")
        motdw.setLayout(motd)
        mainLay.addWidget(motdw)

        label = QtWidgets.QLabel(greetings[random.randint(0, len(greetings) - 1)])
        label.setObjectName("greetText")
        motd.addWidget(label)

        mainLay.addWidget(wBottom)

        #fix later that the motd gets bigger and smaller over time
        """
        size = ["font-size: 40px;", "font-size: 35px;"]
        anim = QtCore.QPropertyAnimation(self, 'stlyesheet')
        state = [QtCore.QState(), QtCore.QState()]
        state[0].assignProperty(self, "stylesheet", size[0])
        state[1].assignProperty(self, "stylesheet", size[1])
        state[0].addTransition(state[0].propertiesAssigned, state[1])
        state[1].addTransition(state[1].propertiesAssigned, state[0])

        self.machine = QtCore.QStateMachine()
        self.machine.addDefaultAnimation(anim)
        self.machine.addState(state[0])
        self.machine.addState(state[1])
        self.machine.setInitialState(state[0])
        self.machine.start()
        """

        self.setLayout(mainLay)

    def selectProject(self):
        if Introduction.infoTabOpen:
            for i in range(Introduction.vLastProjects.count()):
                Introduction.vLastProjects.itemAt(i).widget().setStyleSheet("background-color: #0084a8;")
            Introduction.selectedProject = self.path
            Introduction.selectedProjectName = self.name
            self.setStyleSheet("background-color: #006986;")

            Introduction.setProjectInfo(self, "fromList")

    def setProjectInfo(self, place):
        if place == "fromList":
            Introduction.infoName.setVisible(True)
            Introduction.infoName.setText("Name: {0}".format(Introduction.selectedProjectName))
            Introduction.infoPath.setText("Path: {0}".format(Introduction.selectedProject))
        
        elif place == "fromFile":
            Introduction.infoName.setVisible(False)
            print(Introduction.selectedProject)
            Introduction.infoPath.setText("Path: {0}".format(Introduction.selectedProject))
            print(Introduction.infoPath.text())

        elif place == "fromCreate":
            self.pathEdit.setText(Introduction.selectedFolder)

    def appendProjectName(self):
        Introduction.selectedProjectName = self.nameEdit.text()
        Introduction.selectedFolder = self.pathEdit.text()
        if self.createSubfolder.isChecked() and Introduction.selectedFolder != "":
            self.pathEdit.setText(Introduction.selectedFolder + self.nameEdit.text() + "/")

    def switchTab(self):
        if Introduction.infoTabOpen:
            self.sCenter.setCurrentIndex(1)
            self.createBtn.setText("Info")
            Introduction.appendProjectName(self)
            Introduction.infoTabOpen = False
        else:
            self.sCenter.setCurrentIndex(0)
            self.createBtn.setText("Create")
            Introduction.infoTabOpen = True

#For executing this file standalone
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #Set the main styling of the app
    with open("../appearance/style/stylesheet.css") as f:
        theme = f.read()
    app.setStyleSheet(theme)
    gui = Introduction()
    gui.show()
    app.exec_()