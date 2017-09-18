import qtawesome as qta
import createWorkarea
from components import introductionWindow
from PyQt5 import QtGui, QtCore, QtWidgets

#Tabwidget for the open files ontop of the editor

class LastProjItem(QtWidgets.QWidget):
    projBtn = None
    def setup(self, text, path):
        lay = QtWidgets.QHBoxLayout()
        LastProjItem.projBtn = QtWidgets.QPushButton()

        self.path = path
        self.name = text

        lay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        LastProjItem.projBtn.setText(text)
        LastProjItem.projBtn.setMaximumHeight(51)
        LastProjItem.projBtn.setMinimumWidth(160)
        #LastProjItem.projBtn.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred))
        LastProjItem.projBtn.setObjectName("projectName")
        LastProjItem.projBtn.clicked.connect(lambda:introductionWindow.Introduction.selectProject(self))

        self.setLayout(lay)
        lay.addWidget(LastProjItem.projBtn)

        self.setMaximumWidth(150)