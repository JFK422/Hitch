import qtawesome as qta
from components.Menu import menuSeperator
from components.Menu import menuActions
from PyQt5 import QtGui, QtCore, QtWidgets

#Menu widget placed in the stack of vLPart

class MenuFile(QtWidgets.QWidget):
    def setup(self):
        vMenu = QtWidgets.QVBoxLayout()
        vMenu.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        vMenu.setContentsMargins(QtCore.QMargins(20,20,20,20))

        scrollLay = QtWidgets.QVBoxLayout()
        scrollLay.setContentsMargins(QtCore.QMargins(10,10,10,10))
        scrollLay.setAlignment(QtCore.Qt.AlignTop)

        scrollLayWid = QtWidgets.QWidget()
        scrollLayWid.setObjectName("menuLay")
        scrollLayWid.setLayout(scrollLay)

        fileText = QtWidgets.QLabel("File")
        fileText.setObjectName("menuTitle")
        vMenu.addWidget(fileText)

        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(scrollLayWid)
        scroll.setWidgetResizable(True)
        vMenu.addWidget(scroll)

        #Add icons later!
        newFile = QtWidgets.QPushButton("New File")
        newFile.setMaximumHeight(50)
        newFile.setObjectName("menuItem")
        scrollLay.addWidget(newFile)

        openProject = QtWidgets.QPushButton("Open Project")
        openProject.setMaximumHeight(50)
        openProject.setObjectName("menuItem")
        openProject.clicked.connect(lambda:menuActions.MenuAction.openProjectFromFile(self))
        scrollLay.addWidget(openProject)

        sep = menuSeperator.MenuSeperator()
        sep.setup()
        scrollLay.addWidget(sep)

        saveFile = QtWidgets.QPushButton("Save File")
        saveFile.setMaximumHeight(50)
        saveFile.setObjectName("menuItem")
        scrollLay.addWidget(saveFile)

        saveAllFiles = QtWidgets.QPushButton("Save All")
        saveAllFiles.setMaximumHeight(50)
        saveAllFiles.setObjectName("menuItem")
        scrollLay.addWidget(saveAllFiles)

        sep2 = menuSeperator.MenuSeperator()
        sep2.setup()
        scrollLay.addWidget(sep2)

        projSettings = QtWidgets.QPushButton("Project Settings")
        projSettings.setMaximumHeight(50)
        projSettings.setObjectName("menuItem")
        scrollLay.addWidget(projSettings)

        editSettings = QtWidgets.QPushButton("Editor Settings")
        editSettings.setMaximumHeight(50)
        editSettings.setObjectName("menuItem")
        scrollLay.addWidget(editSettings)

        switchProj = QtWidgets.QPushButton("Switch Project")
        switchProj.setMaximumHeight(50)
        switchProj.setObjectName("menuItem")
        scrollLay.addWidget(switchProj)

        sep3 = menuSeperator.MenuSeperator()
        sep3.setup()
        scrollLay.addWidget(sep3)

        quit = QtWidgets.QPushButton("Close Editor")
        quit.setMaximumHeight(50)
        quit.setObjectName("quitBtnFile")
        quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        scrollLay.addWidget(quit)

        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        self.setLayout(vMenu)