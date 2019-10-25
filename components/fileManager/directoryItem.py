import qtawesome as qta
import colorama as clr
import createWorkarea, os
from components import create
from components.fileManager import fmgActions as actions
from PyQt5 import QtGui, QtCore, QtWidgets

#Tabwidget for the open files ontop of the editor

class DirectoryItem(QtWidgets.QWidget):
    itmBtn = None
    itmName = None
    lastName = [False, "", ""]
    gPath = ""
    isDirCreating = True
    def setup(self, name, path, dType):
        lay = QtWidgets.QVBoxLayout()
        lay.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        DirectoryItem.itmBtn = QtWidgets.QPushButton("")
        DirectoryItem.itmName = QtWidgets.QLabel("")
        self.dirNameEdit = QtWidgets.QLineEdit()

        self.path = path
        self.name = name
        self.type = dType
        self.button = DirectoryItem.itmBtn
        DirectoryItem.gPath = path

        lay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        DirectoryItem.itmBtn.setMinimumSize(QtCore.QSize(50, 50))
        DirectoryItem.itmBtn.setMaximumSize(QtCore.QSize(100, 90))

        dirIco = qta.icon("fa.folder", color="#f9f9f9")
        fileIco = qta.icon("fa.file-text-o", color="#f9f9f9")
        editIco = qta.icon("fa.pencil", color="#f9f9f9")

        #Set the icons first!
        if self.type == "directory":
            DirectoryItem.itmBtn.setIcon(dirIco)
            DirectoryItem.itmBtn.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            DirectoryItem.itmBtn.clicked.connect(lambda:actions.fmgActions.changeLocation(self, self.path + "/"))
            DirectoryItem.itmBtn.customContextMenuRequested.connect(lambda:DirectoryItem.onRightClick(self.button, self.name, path))
        elif self.type == "file":
            DirectoryItem.itmBtn.setIcon(fileIco)
            DirectoryItem.itmBtn.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            DirectoryItem.itmBtn.customContextMenuRequested.connect(lambda:DirectoryItem.onRightClick(self.button, self.name, path))
        elif self.type == "create":
            DirectoryItem.itmBtn.setIcon(dirIco)
            DirectoryItem.itmBtn.clicked.connect(lambda:DirectoryItem.changeType(self))
        elif self.type == "edit":
            DirectoryItem.itmBtn.setIcon(editIco)
        
        #Check for faulty strings!
        else:
            print(clr.Fore.RED + "directoryItem; DirectoryItem; setup: Unknown filetype of item: {0}".format(path+"/"+name) + clr.Style.RESET_ALL)
        
        DirectoryItem.itmBtn.setIconSize(QtCore.QSize(64, 64))
        DirectoryItem.itmBtn.setObjectName("directoryItem")
        DirectoryItem.itmBtn.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        
        #Set the text of the element
        if self.type == "edit":
            self.dirNameEdit.setText(self.name)
        DirectoryItem.itmName.setText(name)
        DirectoryItem.itmName.setWordWrap(True)
        DirectoryItem.itmName.setObjectName("directoryText")

        self.setLayout(lay)
        lay.addWidget(DirectoryItem.itmBtn)
        if self.type == "create" or self.type == "edit":
            lay.addWidget(self.dirNameEdit)
        else:
            lay.addWidget(DirectoryItem.itmName)

        self.setMaximumSize(QtCore.QSize(100, 131))

    def createFile(self):
        path = DirectoryItem.gPath
        file = self.dirNameEdit.text()
        if DirectoryItem.isDirCreating:
            os.makedirs(path + file)
        else:
            f = open(path + file + ".hth", "w+")
            f.close()
        create.CreateUI.openProjectInEditor(self, "refresh")
        
    def abortChanges(self):
        create.CreateUI.openProjectInEditor(self, "refresh")
    
    def changeType(self):
        dirIco = qta.icon("fa.folder", color="#f9f9f9")
        fileIco = qta.icon("fa.file-text-o", color="#f9f9f9")
        if DirectoryItem.isDirCreating:
            DirectoryItem.itmBtn.setIcon(fileIco)
            DirectoryItem.isDirCreating = False
        else:
            DirectoryItem.itmBtn.setIcon(dirIco)
            DirectoryItem.isDirCreating = True

    def renameFile(self):
        oldPath = "/"
        for j in range(len(DirectoryItem.lastName[2].split("/"))):
            oldPath += DirectoryItem.lastName[2].split("/")[j]
            if j != 0:
                oldPath += "/"
            if j == len(DirectoryItem.lastName[2].split("/"))-2:
                break
        if(self.dirNameEdit.text() == ""):
            print(clr.Fore.YELLOW + "directoryItem; DirectoryItem; renameFile: Cannot rename file! No new name defined!" + clr.Style.RESET_ALL)
        else:
            os.rename(DirectoryItem.lastName[2], oldPath + self.dirNameEdit.text())
            print("directoryItem; DirectoryItem; renameFile: Renamed file to: {0}".format(self.dirNameEdit.text()))
            create.CreateUI.openProjectInEditor(self, "refresh")

    def onRightClick(self, name, path):
        moveIco = qta.icon("fa.arrows-alt", color="#f9f9f9")
        editIco = qta.icon("fa.pencil", color="#f9f9f9")
        deleteIco = qta.icon("fa.trash-o", color="#f9f9f9")

        popMenu = QtWidgets.QMenu()
        popMenu.setObjectName("rightClkMenu")
        popMenu.addAction(editIco, "Edit")
        popMenu.addAction(moveIco, "Move")
        popMenu.addSeparator()
        popMenu.addAction(deleteIco, "Delete")

        selected = popMenu.exec_(self.mapToGlobal(self.pos()))

        #Check wich action was executed
        try:
            if selected.text() == "Edit":
                create.CreateUI.openProjectInEditor(self, "edit", name)
                DirectoryItem.lastName[0] = True
                DirectoryItem.lastName[1] = name
                DirectoryItem.lastName[2] = path
            elif selected.text() == "Move":
                print("Move object")
            elif selected.text() == "Delete":
                print("Delete dis")
        except:
            print(clr.Fore.YELLOW + "directoryItem; DirectoryItem; onRightClick: Dismissed righclick menu" + clr.Style.RESET_ALL)
        
    def keyPressEvent(self, event):
        if DirectoryItem.lastName[0]:
            if event.key() == QtCore.Qt.Key_Enter:
                DirectoryItem.renameFile(self)
            elif event.key() == QtCore.Qt.Key_Escape:
                DirectoryItem.abortChanges(self)
            elif event.key() == 16777220:
                DirectoryItem.renameFile(self)
            else:
                print("{0} Pressed".format(event.key()))
        else:
            if event.key() == QtCore.Qt.Key_Enter:
                DirectoryItem.createFile(self)
            elif event.key() == QtCore.Qt.Key_Escape:
                DirectoryItem.abortChanges(self)
            elif event.key() == 16777220:
                DirectoryItem.createFile(self)
            else:
                print("{0} Pressed".format(event.key()))