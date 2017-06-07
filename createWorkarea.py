import sys, os
from PyQt5 import QtGui, QtCore, QtWidgets, QtOpenGL
from OpenGL.GL import *

#This is used to create the grid of the workarea for the scripting and some main functions

#Variables


class createArea(QtWidgets.QOpenGLWidget):
    def __init__(self, parent = None):
        print("CreateWorkarea: Init method called")

        super(createArea, self).__init__(parent)

    def paintGL(self):
        glColor3f(0.0, 0.0, 1.0)
        glRectf(-5, -5, 5, 5)
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(20, 20, 0)
        glEnd()

    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-50, 50, -50, 50, -50.0, 50.0)
        glViewport(0, 0, w, h)

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

"""
if __name__ == '__main__':
    app = QtWidgets.QApplication(["Winfred's PyQt OpenGL"])
    widget = createArea()
    widget.show()
    app.exec_()
"""