import qtawesome as qta
import createWorkarea
from components import introductionWindow
from PyQt5 import QtGui, QtCore, QtWidgets

#Tabwidget for the open files ontop of the editor

class DirectoryItem(QtWidgets.QWidget):
    itmBtn = None
    itmName = None
    def setup(self, name, path, dType):
        lay = QtWidgets.QVBoxLayout()
        lay.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        DirectoryItem.itmBtn = QtWidgets.QPushButton("")
        DirectoryItem.itmName = QtWidgets.QLabel("")

        self.path = path
        self.name = name
        self.type = dType

        lay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        DirectoryItem.itmBtn.setMinimumSize(QtCore.QSize(50, 50))
        DirectoryItem.itmBtn.setMaximumSize(QtCore.QSize(100, 90))
        dirIco = qta.icon("fa.folder", color="#f9f9f9")
        fileIco = qta.icon("fa.file-text-o", color="#f9f9f9")
        if self.type == "directory":
            DirectoryItem.itmBtn.setIcon(dirIco)
        else:
            DirectoryItem.itmBtn.setIcon(fileIco)
        DirectoryItem.itmBtn.setIconSize(QtCore.QSize(64, 64))
        DirectoryItem.itmBtn.setObjectName("directoryItem")
        DirectoryItem.itmBtn.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        DirectoryItem.itmName.setText(name)
        DirectoryItem.itmName.setWordWrap(True)
        DirectoryItem.itmName.setObjectName("directoryText")

        self.setLayout(lay)
        lay.addWidget(DirectoryItem.itmBtn)
        lay.addWidget(DirectoryItem.itmName)

        self.setMaximumSize(QtCore.QSize(100, 131))