import sys, os
import qtawesome as qta
from PyQt4 import QtGui, QtCore

#This is used to create the grid of the workarea for the scripting and some main functions

#Variables


class createArea():
    def __init__(self):
        print("CreateWorkarea: Init mehtod called")

    def createGrid(self):
        print("CreateWorkarea: Creating Grid")

        pGrid = QtGui.QPainter()