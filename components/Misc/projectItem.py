import qtawesome as qta
import createWorkarea
from components import introductionWindow
from PyQt5 import QtGui, QtCore, QtWidgets

#Tabwidget for the open files ontop of the editor

class LastProjItem(QtWidgets.QWidget):
    name = None
    path = None
    def setup(self, text, path):
        lay = QtWidgets.QHBoxLayout()
        projBtn = QtWidgets.QPushButton()

        LastProjItem.path = path
        LastProjItem.name = text

        lay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        projBtn.setText(text)
        projBtn.setMaximumHeight(51)
        projBtn.setMinimumWidth(150)
        #projBtn.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred))
        projBtn.setObjectName("projectName")
        projBtn.clicked.connect(lambda:introductionWindow.Introduction.selectProject(self, LastProjItem.path))

        self.setLayout(lay)
        lay.addWidget(projBtn)

        self.setMaximumWidth(150)