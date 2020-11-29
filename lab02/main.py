import pygame,sys
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL import Image
import numpy as np

pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0,0.0, -5)

img = Image.open('texture.jpg')
img = np.asarray(img, dtype=np.uint8)

def draw():
    # clear
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # set light
    glShadeModel (GL_SMOOTH)
    glLightfv (GL_LIGHT0, GL_DIFFUSE, [1.0,1.0,1.0,1.0])
    glLightfv (GL_LIGHT0, GL_POSITION, [-0.8, 0.8, 1.1, 1.0])
    
    glEnable (GL_LIGHTING)
    glEnable (GL_LIGHT0)
    glEnable (GL_DEPTH_TEST)
    glDisable(GL_COLOR_MATERIAL)

    # bind texture
    textures = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textures)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.shape[0], img.shape[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img)

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)

    # draw torus
    glutSolidTorus(0.3, 0.5, 15, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    glRotatef(1, 1, 1, 1)
    draw()
    pygame.display.flip()
    pygame.time.wait(10)