import sys, os
from PyQt5 import QtGui, QtCore, QtWidgets, QtOpenGL
from OpenGL import GL, GLU

#This is used to create the grid of the workarea for the scripting and some main functions

#Variables


class createArea(QtWidgets.QOpenGLWidget):
    def __init__(self, parent = None):
        print("CreateWorkarea: Init method called")

        super(createArea, self).__init__(parent)

    def paintGL(self):
        GL.glColor3f(0.0, 0.0, 1.0)
        GL.glRectf(-5, -5, 5, 5)
        GL.glColor3f(1.0, 0.0, 0.0)
        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(20, 20, 0)
        GL.glEnd()

    def resizeGL(self, w, h):
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(-50, 50, -50, 50, -50.0, 50.0)
        GL.glViewport(0, 0, w, h)

    def initializeGL(self):
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)


"""
class SpiralWidgetDemo(QtWidgets.QMainWindow):
    ''' Example class for using SpiralWidget'''
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        widget = createArea(self)    
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QtWidgets.QApplication(['Spiral Widget Demo'])
    window = SpiralWidgetDemo()
    window.show()
    app.exec_()
"""