import qtawesome as qta
import createWorkarea
from PyQt5 import QtGui, QtCore, QtWidgets

#Tabwidget for the open files ontop of the editor

class openFileTab(QtWidgets.QWidget):
    def setup(self, text, icon, path):
        lay = QtWidgets.QHBoxLayout()
        fileBtn = QtWidgets.QPushButton()
        close = QtWidgets.QPushButton()

        lay.setContentsMargins(QtCore.QMargins(0,0,10,0))
        fileBtn.setText(text)
        fileBtn.setIcon(icon)
        #fileBtn.Align(QtCore.Qt.AlignLeft)
        fileBtn.setObjectName("openFilesTab")
        close.setIcon(qta.icon("fa.times", color = "white"))
        close.setObjectName("quitBtn")
        close.setMaximumWidth(20)
        self.filePath = path                

        self.setLayout(lay)
        lay.addWidget(fileBtn)
        lay.addWidget(close)

        self.setMaximumWidth(150)