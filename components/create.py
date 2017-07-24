import sys, os, createWorkarea, compiler
import qtawesome as qta
from components.Misc import openFileTabWidget
from projectHandling import saveFiles as sf
from components.Menu import menuRunTab
from components.Menu import menuEditTab
from components.Menu import menuFileTab
from components.Menu import menuSettingsTab
from components.Menu import menuWindowTab
from projectHandling import workareaData as wd
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

#This is the main file which is used for creating the window.

class CreateUI:
    hOpenFilesLay = None
    def create(self):
        print("create; createUI; create: Creating the main window layout")
        print("create; createUI; create: Creating widgets")

        #Create icons
        compileStates = {"uncompiled" : "#a51946", "compiled" : "#4190ff", "error" : "#ffb041", "leftovers" : "#b041ff", "compiling" : "white"}
        self.toolbarIcons = [qta.icon("fa.minus", color="white"), 
                                    qta.icon("fa.times", color="white"), 
                                    qta.icon("fa.sliders", color="white"), 
                                    qta.icon("fa.arrows-alt", color="white"), 
                                    qta.icon("fa.file-text-o", color="white"),
                                    qta.icon("fa.pencil", color="white"),
                                    qta.icon("fa.square-o", color="white"),
                                    qta.icon("fa.play", color="white"),
                                    qta.icon("fa.gear", color=compileStates["compiling"]), #Later add a spin animation to this icon
                                    qta.icon("fa.gear", color=compileStates["uncompiled"]),
                                    qta.icon("fa.gear", color=compileStates["compiled"]),
                                    qta.icon("fa.gear", color=compileStates["error"]),
                                    qta.icon("fa.gear", color=compileStates["leftovers"]),
                                    qta.icon("fa.caret-down", color="white"),
                                    qta.icon("fa.floppy-o", color="white")]

        #Create window action buttons
        mini = QtWidgets.QPushButton(self.toolbarIcons[0], "", self)
        mini.setObjectName("minimize")
        mini.setMaximumSize(QtCore.QSize(30,30))
        mini.clicked.connect(self.minimize)

        quitBtn = QtWidgets.QPushButton(self.toolbarIcons[1], "", self)
        quitBtn.setObjectName("quitBtn")
        quitBtn.setMaximumSize(QtCore.QSize(30,30))
        quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        settings = QtWidgets.QPushButton(self.toolbarIcons[2], "", self)
        settings.setObjectName("settingsBtn")
        settings.setMaximumSize(QtCore.QSize(30,30))
        settings.clicked.connect(lambda:CreateUI.switchMenu(self, 3))

        maxim = QtWidgets.QPushButton(self.toolbarIcons[3], "", self)
        maxim.setObjectName("maxim")
        maxim.setMaximumSize(QtCore.QSize(30,30))
        maxim.clicked.connect(self.maximize)

        #Create Tool Buttons
        files = QtWidgets.QPushButton(self.toolbarIcons[4], "", self)
        files.setObjectName("tools")
        files.setMaximumSize(QtCore.QSize(30,30))
        files.clicked.connect(lambda:CreateUI.switchMenu(self, 2))

        edit = QtWidgets.QPushButton(self.toolbarIcons[5], "", self)
        edit.setObjectName("tools")
        edit.setMaximumSize(QtCore.QSize(30,30))
        edit.clicked.connect(lambda:CreateUI.switchMenu(self, 1))

        wind = QtWidgets.QPushButton(self.toolbarIcons[6], "", self)
        wind.setObjectName("tools")
        wind.setMaximumSize(QtCore.QSize(30,30))
        wind.clicked.connect(lambda:CreateUI.switchMenu(self, 4))

        tool = QtWidgets.QPushButton(self.toolbarIcons[7], "", self)
        tool.setObjectName("tools")
        tool.setMaximumSize(QtCore.QSize(30,30))
        tool.clicked.connect(lambda:CreateUI.switchMenu(self, 0))

        #Create app buttons and icons
        self.compileBtn = QtWidgets.QPushButton("", self)
        self.compileBtn.setObjectName("toolButtons")
        self.compileBtn.setMinimumSize(QtCore.QSize(50,50))
        self.compileBtn.setMaximumSize(QtCore.QSize(90,90))
        self.compileBtn.clicked.connect(lambda:compiler.compiler.compile(self))

        compMenu = QtWidgets.QMenu()
        compMenu.addAction("Compile All")
        compMenu.addAction("Compile Current")
        #compMenu.addAction("Package")

        modeBtn = QtWidgets.QPushButton("", self)
        modeBtn.setObjectName("toolButtons")
        modeBtn.setMenu(compMenu)
        modeBtn.setMaximumWidth(20)

        saveBtn = QtWidgets.QPushButton("", self)
        saveBtn.setObjectName("toolButtons")
        saveBtn.setMinimumSize(QtCore.QSize(50,50))
        saveBtn.setMaximumSize(QtCore.QSize(90,90))
        saveBtn.clicked.connect(lambda:sf.saveFiles.saveAFile(self, "filePath"))

        self.compileBtn.setIcon(self.toolbarIcons[12])
        self.compileBtn.setIconSize(QtCore.QSize(64, 64))
        modeBtn.setIcon(self.toolbarIcons[13])
        saveBtn.setIcon(self.toolbarIcons[14])
        saveBtn.setIconSize(QtCore.QSize(64, 64))

        """
        Audio Test (doesnt work!)
        url= QtCore.QUrl.fromLocalFile("./Tobu - Amplified.mp3")
        content= QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        """

        #Dialogs
        dial = QtWidgets.QMessageBox()

        #Empty Widgets
        wLPart = QtWidgets.QWidget()
        wLPart.setObjectName("leftEdit")

        wCPart = QtWidgets.QWidget()
        wCPart.setObjectName("centerEdit")

        wRPart = QtWidgets.QWidget()
        wRPart.setObjectName("rightEdit")

        wFileExplorer = QtWidgets.QWidget()
        wFileExplorer.setObjectName("fileExplorer")

        wOpenFiles = QtWidgets.QWidget()
        wOpenFiles.setObjectName("openFilesBar")

        wComp = QtWidgets.QWidget()
        #wComp.setObjectName("rightEdit")
        wComp.setMaximumSize(QtCore.QSize(110, 90))
        wComp.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))

        #Size
        wCPart.setMinimumWidth(500)
        wRPart.setMinimumWidth(300)
        wLPart.setMinimumWidth(300)

        wLPart.setMaximumWidth(400)
        wRPart.setMaximumWidth(400)
        wOpenFiles.setMaximumHeight(40)

        #Titlebar background
        cont = QtWidgets.QWidget(self)
        cont.setObjectName("titlebar")
        cont.setMinimumHeight(120)
        cont.setMaximumHeight(120)

        #Size Policy for layouts
        wCPart.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding))

        print("create; createUI; create: Creating layouts")
        #Layouts
        vMain = QtWidgets.QVBoxLayout() #Backbone lay, important because of the titlebar
        gCenter = QtWidgets.QGridLayout() #Central grid layout of the app beacuse every part is a widget not a layout
        vTB = QtWidgets.QHBoxLayout(cont) #Titlebar Layout
        vTabs = QtWidgets.QHBoxLayout() #Tabs Layout in the Titlebar
        winAc  = QtWidgets.QGridLayout() #Window actions layout (Top left buttons)
        tools = QtWidgets.QGridLayout() #Grid Layout for the tool actions in the titlebar
        self.vLPart = QtWidgets.QStackedLayout() #Left part of the editor
        self.vCPart = QtWidgets.QVBoxLayout() #Main layout of the editor
        self.vRPart = QtWidgets.QStackedLayout() #Right part of the editor
        CreateUI.hOpenFilesLay  = QtWidgets.QHBoxLayout() #Layout for the open files ontop of the editor
        self.vFileExplorer = QtWidgets.QVBoxLayout() #Layout for the file explorer
        hComp = QtWidgets.QHBoxLayout() #Layout for the dropdown and the compile button

        print("create; createUI; create: Seting layouts alignment and margins")
        #Alignment
        vMain.setAlignment(QtCore.Qt.AlignTop)
        winAc.setAlignment(QtCore.Qt.AlignRight)
        gCenter.setAlignment(QtCore.Qt.AlignTop)
        #self.vCPart.setAlignment(QtCore.Qt.AlignTop)
        CreateUI.hOpenFilesLay .setAlignment(QtCore.Qt.AlignLeft)
        hComp.setAlignment(QtCore.Qt.AlignLeft)

        #Margin
        vMain.setContentsMargins(QtCore.QMargins(0,0,0,0))
        winAc.setContentsMargins(QtCore.QMargins(0,0,0,0))
        gCenter.setContentsMargins(QtCore.QMargins(0,0,0,0))
        self.vCPart.setContentsMargins(QtCore.QMargins(0,0,0,0))
        CreateUI.hOpenFilesLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        winAc.setContentsMargins(QtCore.QMargins(10,23,20,23))
        vTB.setContentsMargins(QtCore.QMargins(20,0,0,0))
        tools.setContentsMargins(QtCore.QMargins(0,23,30,23))
        vTabs.setContentsMargins(QtCore.QMargins(0,0,0,0))
        hComp.setContentsMargins(QtCore.QMargins(0,0,10,0))

        #Stretch
        #vLPart.addStretch(1)
        #self.vCPart.addStretch(5)
        #vRPart.addStretch(1)

        #Adding the Widgets
        print("create; createUI; create: Adding the widgets to the layouts")
        vMain.addWidget(cont)

        winAc.addWidget(mini, 0, 0)
        winAc.addWidget(quitBtn, 0, 1)
        winAc.addWidget(maxim, 1, 0)
        winAc.addWidget(settings, 1, 1)

        tools.addWidget(files, 0, 0)
        tools.addWidget(edit, 0, 1)
        tools.addWidget(wind, 1, 0)
        tools.addWidget(tool, 1, 1)

        #Left side menu parts
        menuRun = menuRunTab.MenuRun()
        menuRun.setup()
        self.vLPart.addWidget(menuRun)

        menuEdit = menuEditTab.MenuEdit()
        menuEdit.setup()
        self.vLPart.addWidget(menuEdit)

        menuFile = menuFileTab.MenuFile()
        menuFile.setup()
        self.vLPart.addWidget(menuFile)

        menuSettings = menuSettingsTab.MenuSettings()
        menuSettings.setup()
        self.vLPart.addWidget(menuSettings)

        menuWindow = menuWindowTab.MenuWindow()
        menuWindow.setup()
        self.vLPart.addWidget(menuWindow)

        #Right side widgets
        self.vRPart.addWidget(wFileExplorer)
        wFileExplorer.setLayout(self.vFileExplorer)

        #Center part widgets
        self.vCPart.addWidget(wOpenFiles)
        wWorkarea = createWorkarea.createArea()
        self.vCPart.addWidget(wWorkarea)

        #Add the left, center and right widget layouts to a central grid
        gCenter.addWidget(wLPart, 0, 0)
        gCenter.addWidget(wCPart, 0, 1)
        gCenter.addWidget(wRPart, 0, 2)

        #Add toolbar buttons
        hComp.addWidget(self.compileBtn)
        hComp.addWidget(modeBtn)
        vTabs.addWidget(wComp)
        vTabs.addWidget(saveBtn)

        #adding the Layouts
        print("create; createUI; create: Adding the layouts to widgets")
        wLPart.setLayout(self.vLPart)
        wCPart.setLayout(self.vCPart)
        wRPart.setLayout(self.vRPart)
        wComp.setLayout(hComp)
        wOpenFiles.setLayout(CreateUI.hOpenFilesLay )

        print("create; createUI; create: Adding the layouts together")
        vTB.addLayout(tools)
        vTB.addLayout(vTabs)
        vTB.addLayout(winAc)
        vMain.addLayout(vTB)
        vMain.addLayout(gCenter)
        self.setLayout(vMain)

    def switchCompStatus(self, newStatus):
        if newStatus == "compiling":
            self.compileBtn.setIcon(self.toolbarIcons[8])
            self.currentCompStat = "compiling"
        elif newStatus == "uncompiled":
            self.compileBtn.setIcon(self.toolbarIcons[9])
            self.currentCompStat = "uncompiled"
        elif newStatus == "compiled":
            self.compileBtn.setIcon(self.toolbarIcons[10])
            self.currentCompStat = "compiled"
        elif newStatus == "error":
            self.compileBtn.setIcon(self.toolbarIcons[11])
            self.currentCompStat = "error"
        elif newStatus == "leftovers":
            self.compileBtn.setIcon(self.toolbarIcons[12])
            self.currentCompStat = "leftovers"
        else:
            print("create; createUI; switchCompStatus: Error, unable to determine the new icon status!")

    def switchMenu(self, index):
        self.vLPart.setCurrentIndex(index)