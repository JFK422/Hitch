import createWorkarea
from components import introductionWindow
from PyQt5 import QtGui, QtCore, QtWidgets

#Tabwidget for the open files ontop of the editor

class LastProjItem(QtWidgets.QWidget):
    projBtn = None
    def setup(self, name, path, itemIndex, colour):
        lay = QtWidgets.QHBoxLayout()
        LastProjItem.projBtn = QtWidgets.QPushButton()

        self.path = path
        self.name = name
        self.index = itemIndex
        self.colour = colour

        lay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        LastProjItem.projBtn.setText(name)
        LastProjItem.projBtn.setMaximumHeight(51)
        LastProjItem.projBtn.setMinimumWidth(160)
        if colour:
            LastProjItem.projBtn.setStyleSheet("background-color: #a51946;")
            #Create a dialog here, when the button is clicked, asking if the project is wanted to be removed.
            #LastProjItem.projBtn.clicked.connect(lambda:introductionWindow.Introduction.projNotFound(self))
        else:
            LastProjItem.projBtn.setObjectName("projectName")
            LastProjItem.projBtn.clicked.connect(lambda:introductionWindow.Introduction.selectProject(self))
        #LastProjItem.projBtn.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred))

        self.setLayout(lay)
        lay.addWidget(LastProjItem.projBtn)

        self.setMaximumWidth(150)