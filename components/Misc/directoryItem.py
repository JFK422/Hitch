import qtawesome as qta
import colorama as clr
import createWorkarea, os
from components import create
from PyQt5 import QtGui, QtCore, QtWidgets

#Tabwidget for the open files ontop of the editor

class DirectoryItem(QtWidgets.QWidget):
    itmBtn = None
    itmName = None
    itmEdit = None
    def setup(self, name, path, dType):
        lay = QtWidgets.QVBoxLayout()
        lay.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        DirectoryItem.itmBtn = QtWidgets.QPushButton("")
        DirectoryItem.itmName = QtWidgets.QLabel("")
        DirectoryItem.itmEdit = QtWidgets.QLineEdit("")

        self.path = path
        self.name = name
        self.type = dType

        lay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        DirectoryItem.itmBtn.setMinimumSize(QtCore.QSize(50, 50))
        DirectoryItem.itmBtn.setMaximumSize(QtCore.QSize(100, 90))
        dirIco = qta.icon("fa.folder", color="#f9f9f9")
        fileIco = qta.icon("fa.file-text-o", color="#f9f9f9")
        editIco = qta.icon("fa.pencil", color="#f9f9f9")
        if self.type == "directory":
            DirectoryItem.itmBtn.setIcon(dirIco)
        elif self.type == "create":
            DirectoryItem.itmBtn.setIcon(dirIco)
        elif self.type == "edit":
            DirectoryItem.setIcon(editIco)
        elif self.type == "file":
            DirectoryItem.itmBtn.setIcon(fileIco)
        else:
            print(clr.Fore.RED + "directoryItem; DirectoryItem; setup: Unknown filetype of item: {0}".format(path+"/"+name))
            print(clr.Style.RESET_ALL)
        DirectoryItem.itmBtn.setIconSize(QtCore.QSize(64, 64))
        DirectoryItem.itmBtn.setObjectName("directoryItem")
        DirectoryItem.itmBtn.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        if self.type == "edit":
            DirectoryItem.itmName.setText(name)
        else:
            DirectoryItem.itmName.setText(name)
            DirectoryItem.itmName.setWordWrap(True)
            DirectoryItem.itmName.setObjectName("directoryText")

        self.setLayout(lay)
        lay.addWidget(DirectoryItem.itmBtn)
        if self.type == "create" or self.type == "edit":
            lay.addWidget(DirectoryItem.itmEdit)
        else:
            lay.addWidget(DirectoryItem.itmName)

        self.setMaximumSize(QtCore.QSize(100, 131))

    def createFile(self, file, path):
        os.makedirs(path)
        f = open(path + file, "w+")
        f.close()
        create.CreateUI.openProjectInEditor(self)
        
    def abortChanges(self):
        print("L")