import qtawesome as qta
import random, sys, os
from projectHandling import workareaData
from components.Misc import projectItem
from components.Menu import menuActions
from PyQt5 import QtGui, QtCore, QtWidgets

#Menu widget placed in the stack of vLPart

class Introduction(QtWidgets.QWidget):
    vLastProjects = None
    selectedProject = None
    selectedProjectName = None
    infoName = None
    infoPath = None
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

        vInfo = QtWidgets.QVBoxLayout()
        vInfo.setAlignment(QtCore.Qt.AlignTop)
        wInfo = QtWidgets.QWidget()
        wInfo.setLayout(vInfo)
        wInfo.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred))
        wInfo.setObjectName("lastProjects")
        Introduction.infoName = QtWidgets.QLabel("")
        Introduction.infoName.setObjectName("infoText")
        Introduction.infoPath = QtWidgets.QLabel("")
        Introduction.infoPath.setObjectName("infoText")
        Introduction.infoPath.setWordWrap(True)
        vInfo.addWidget(Introduction.infoName)
        vInfo.addWidget(Introduction.infoPath)

        hBottom.addWidget(wInfo)

        hLaunch = QtWidgets.QVBoxLayout()
        #hLaunch.setAlignment(QtCore.Qt.AlignCenter)
        hLaunch.setContentsMargins(QtCore.QMargins(10,10,10,10))
        #hLaunch.setSpacing(15)
        wLaunch = QtWidgets.QWidget()
        wLaunch.setLayout(hLaunch)
        wLaunch.setObjectName("lastProjectsLaunch")

        #add the last opened projects as items
        for i in range(len(workareaData.Data.lastProjects)):
            projItem = projectItem.LastProjItem()
            projItem.setup(text = workareaData.Data.lastProjNames[i], path = workareaData.Data.lastProjects[i])
            Introduction.vLastProjects.addWidget(projItem)

        launchBtn = QtWidgets.QPushButton("Launch")
        launchBtn.setObjectName("launchProject")
        hLaunch.addWidget(launchBtn)
        hBottom.addWidget(wLaunch)

        openBtn = QtWidgets.QPushButton("Open")
        openBtn.clicked.connect(lambda:menuActions.MenuAction.openProject(self))
        hLaunch.addWidget(openBtn)

        createBtn = QtWidgets.QPushButton("Create")
        hLaunch.addWidget(createBtn)

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

    def selectProject(self, path):
        for i in range(Introduction.vLastProjects.count()):
            wid = Introduction.vLastProjects.itemAt(i).widget()
            wid.setStyleSheet("background-color: #0084a8;")
        self.setStyleSheet("background-color: #006986;")
        Introduction.selectedProject = self.path
        Introduction.selectedProjectName = self.name

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