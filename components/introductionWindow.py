import qtawesome as qta
import colorama as clr
import random, sys, os
from projectHandling import startupData
from components.Misc import projectItem
from components.Menu import menuActions
from PyQt5 import QtGui, QtCore, QtWidgets

#Menu shown on startup used to select a project

class Introduction(QtWidgets.QWidget):
    #Variables for some recursion, idk how to do it otherwise!
    vLastProjects = None
    selectedProject = ""
    infoName = None
    infoPath = None
    infoTabOpen = True
    createBtn = None
    nameEdit = None
    
    #Init the window
    def __init__(self):
        super(Introduction, self).__init__()
        #Add your own motd here!
        motdVar = ["Hello Old Friend", 
                            "M' Lady", 
                            "Copy pasted Pseudocode", 
                            "Written in the language of snakes", 
                            "Has hidden ASCII art in the code", 
                            "The stylesheets consists mostly of linebreak } linebreak",
                            "This is my jam!",
                            "Digital Hug ༼つ ◕_◕ ༽つ",
                            "Full of stale memes",
                            "ಠ_ಠ",
                            "Insert cool phrase about programming here!"]
        self.setGeometry(50,50,1000,500)
        self.setWindowTitle("Hitch")

        #Create the layouts and their backbone widgets
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

        Introduction.sCenter = QtWidgets.QStackedLayout()
        Introduction.sCenter.setAlignment(QtCore.Qt.AlignTop)
        wCenter = QtWidgets.QWidget()
        wCenter.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred))
        wCenter.setObjectName("lastProjects")
        wCenter.setLayout(Introduction.sCenter)

        vInfo = QtWidgets.QVBoxLayout()
        vInfo.setAlignment(QtCore.Qt.AlignTop)
        wInfo = QtWidgets.QWidget()
        wInfo.setLayout(vInfo)
        Introduction.sCenter.addWidget(wInfo)

        #Create the windows widgets
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

        Introduction.addProjects(self)

        launchBtn = QtWidgets.QPushButton("Launch")
        launchBtn.setObjectName("launchProject")
        launchBtn.clicked.connect(lambda:menuActions.MenuAction.launchProject(self))
        hLaunch.addWidget(launchBtn)
        hBottom.addWidget(wLaunch)

        openBtn = QtWidgets.QPushButton("Open")
        openBtn.clicked.connect(lambda:menuActions.MenuAction.openProjectFromFile(self))
        hLaunch.addWidget(openBtn)

        Introduction.createBtn = QtWidgets.QPushButton("Create")
        Introduction.createBtn.clicked.connect(lambda:Introduction.switchTab(self))
        hLaunch.addWidget(Introduction.createBtn)

        gCreate = QtWidgets.QGridLayout()
        gCreate.setAlignment(QtCore.Qt.AlignTop)
        wCreate = QtWidgets.QWidget()
        wCreate.setLayout(gCreate)

        vBackLay = QtWidgets.QVBoxLayout()
        vBackLay.setAlignment(QtCore.Qt.AlignTop)
        vBackLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        wBackLay = QtWidgets.QWidget()
        wBackLay.setLayout(vBackLay)
        vBackLay.addWidget(wCreate)
        Introduction.sCenter.addWidget(wBackLay)

        #Stuff for the tab on creating a new project
        nameLabel = QtWidgets.QLabel("Name: ")
        nameLabel.setObjectName("infoText")

        Introduction.nameEdit = QtWidgets.QLineEdit()
        Introduction.nameEdit.setObjectName("projectTextEdit")
        Introduction.nameEdit.setMaximumWidth(200)

        pathLabel = QtWidgets.QLabel("Path: ")
        pathLabel.setObjectName("infoText")

        Introduction.pathEdit = QtWidgets.QLineEdit()
        Introduction.pathEdit.setObjectName("projectTextEdit")
        
        folder = qta.icon("fa.folder", color="#f9f9f9")
        pathSelect = QtWidgets.QPushButton(folder, "")
        pathSelect.setIconSize(QtCore.QSize(20, 20))
        pathSelect.setMaximumSize(QtCore.QSize(30, 30))
        pathSelect.clicked.connect(lambda:menuActions.MenuAction.selectProjectFolder(self))
        pathSelect.setObjectName("launchProject")

        infoLabel = QtWidgets.QLabel("Press launch to create the Project.")
        infoLabel.setObjectName("infoTextCreate")

        #Stitch everything together
        gCreate.addWidget(nameLabel, 0, 1)
        gCreate.addWidget(Introduction.nameEdit, 1, 1)
        gCreate.addWidget(pathLabel, 0, 0)
        gCreate.addWidget(Introduction.pathEdit, 1, 0)
        gCreate.addWidget(pathSelect, 1, 2)
        gCreate.addWidget(infoLabel, 3, 0)

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

        label = QtWidgets.QLabel(motdVar[random.randint(0, len(motdVar) - 1)])
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
    
    #Called when a item in the last projects list is clicked
    def selectProject(self):
        #Switch to last projects tab when button is clicked on creation tab.
        if not(Introduction.infoTabOpen):
            Introduction.sCenter.setCurrentIndex(0)
            Introduction.createBtn.setText("Create")
            Introduction.infoTabOpen = True
        
        #Manage the buttons colours and update the text
        for i in range(Introduction.vLastProjects.count()):
            Introduction.vLastProjects.itemAt(i).widget().setStyleSheet("background-color: #0084a8;")
        data = [self.name, self.path]
        self.setStyleSheet("background-color: #006986;")
        Introduction.setProjectInfo(self, "fromList", data)

    #Set the projects textedit and such to the data variable. Place defines what to set.
    def setProjectInfo(self, place, data):
        if place == "fromList":
            Introduction.infoName.setVisible(True)
            Introduction.infoName.setText("Name: {0}".format(data[0]))
            Introduction.infoPath.setText("Path: {0}".format(data[1]))
            Introduction.selectedProject = data[1]
            print("introductionWindow; Introduction; setProjectInfo: Selected Project:{0}".format(data[1]))
        
        elif place == "fromFile":
            Introduction.infoName.setVisible(True)
            Introduction.infoName.setText("Name: {0}".format(os.path.splitext(os.path.basename(data))[0]))
            Introduction.infoPath.setText("Path: {0}".format(data))
            Introduction.selectedProject = data
            print("introductionWindow; Introduction; setProjectInfo: Selected Project from:{0} to open".format(data))

        elif place == "fromCreate":
            print("introductionWindow; Introduction; setProjectInfo: Selected Project Creation Folder:{0}".format(data))
            Introduction.pathEdit.setText(data)
        
        else:
            print(clr.Fore.RED + "introductionWindow; Introduction; setProjectInfo: Error setting the selected projects info!" + clr.Style.RESET_ALL)

    #Switch betwen the create and open project tabs
    def switchTab(self):
        if Introduction.infoTabOpen:
            Introduction.sCenter.setCurrentIndex(1)
            Introduction.createBtn.setText("Last\nProjects")
            Introduction.infoTabOpen = False
        else:
            Introduction.sCenter.setCurrentIndex(0)
            Introduction.createBtn.setText("Create")
            Introduction.infoTabOpen = True

    def projNotFound(self, place):
        rmvDialog = QtWidgets.QMessageBox()
        rmvDialog.setWindowTitle("Remove Project?")
        rmvDialog.setText("This project can't be found anymore at {0}\n should it be removed from the list?".format(place))
        rmvDialog.setStandardButtons(QtWidgets.QMessageBox.Yes)
        rmvDialog.addButton(QtWidgets.QMessageBox.No)
        rmvDialog.setDefaultButton(QtWidgets.QMessageBox.Yes)
        if(rmvDialog.exec() == QtWidgets.QMessageBox.Yes):
            Introduction.removeProject(self, place)
    
    def removeProject(self, path):
        startupData.Data.removeItem(self, path)
        Introduction.addProjects(self)

    def addProjects(self):
        #Clearing of the projects list
        for i in reversed(range(Introduction.vLastProjects.count())):
            Introduction.vLastProjects.itemAt(i).widget().setParent(None)

        #Add the last opened projects as items
        for i in range(startupData.Data.lengthOfDB(self)):
            try:
                fileTest = open(startupData.Data.readDB(self, i)[2], "r")
                projItem = projectItem.LastProjItem()
                projItem.setup(name = startupData.Data.readDB(self, i)[1], path = startupData.Data.readDB(self, i)[2], itemIndex = i, colour = False)
                Introduction.vLastProjects.addWidget(projItem)
            except:
                projItem = projectItem.LastProjItem()
                projItem.setup(name = startupData.Data.readDB(self, i)[1], path = startupData.Data.readDB(self, i)[2], itemIndex = i, colour = True)
                Introduction.vLastProjects.addWidget(projItem)
                print(clr.Fore.YELLOW + "introductionWindow; Introduction; __init__: Error finding project path!" + clr.Style.RESET_ALL)


#For executing this file standalone
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    #Set the main styling of dis window aswell
    with open("../appearance/style/stylesheet.css") as f:
        theme = f.read()
    app.setStyleSheet(theme)
    gui = Introduction()
    gui.show()
    app.exec_()