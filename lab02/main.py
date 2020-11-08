from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1, 0, 1, 0)
    glutWireTorus(0.3, 0.5, 15, 30)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowPosition(0, 0)
glutInitWindowSize(800, 800)
glutCreateWindow(b"Torus")
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
glutMainLoop()