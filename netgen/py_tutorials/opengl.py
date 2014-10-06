from netgen.csg import *
import netgen.meshing as meshing

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



sp1 = Sphere (Pnt(0,0,0), 0.2)
sp2 = Sphere (Pnt(0.5,0,0), 0.2)
sp3 = Sphere (Pnt(0,0,0.5), 0.2)
sp4 = Sphere (Pnt(0,0.2,0.7), 0.2)
sp5 = Sphere (Pnt(0,0,0.3), 0.2)


all = sp1+sp2+sp3+sp4+sp5


geom = CSGeometry()
geom.Add (all)


vis = VS(geom)
# vis.Draw()


window = 0                                             # glut window number
width, height = 500, 500



def mydraw():

    glViewport(0, 0, width, height);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    
    pnear = 0.1;
    pfar = 10;

    gluPerspective(20.0, 1.0*width / height, pnear, pfar);
    glMatrixMode(GL_MODELVIEW);
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#    glLoadIdentity()
#    gluLookAt (0, 0, 6, 0, 0, 0, 0, 1, 0);
    
##    glBegin(GL_QUADS)
##    glColor4d(0.0, 1.0, 0.0, 0.0);
##    glVertex3d(0.0,0.0,0.7)
##    glVertex3d(1.0,0.0,2.1)
##    glColor4d(1.0, 1.0, 1.0, 0.0);
##    glVertex3d(1.0,1.0,0.2)
##    glVertex3d(0.0,1.0,0.5)
##    glEnd()
     
    vis.Draw()
    
    glutSwapBuffers()

xold = -1;
yold = -1;
mode = 'r'

def myMotionHandler( x, y ):
    global xold, yold
    MouseMove(vis,xold,yold, x,y, mode)  # 'm','z'
    xold = x
    yold = y

def myPassiveMotionHandler( x, y ):
    global xold, yold
    xold = x
    yold = y

def myMouseHandler( button, state, x, y ):
    print(button,state,x,y)
    modes = {0:'r', 1:'m', 2:'z'}
    global mode
    if button<3:
        if state==0:
            mode = modes[button]
        else:
            mode = 'r'



glutInit("mainwin")                                   # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b"ngs")                      # create window with title
glutMotionFunc(myMotionHandler)
glutMouseFunc(myMouseHandler)
glutPassiveMotionFunc(myPassiveMotionHandler)
glutDisplayFunc(mydraw)                                 # set draw function callback
glutIdleFunc(mydraw)                                     # draw all the time
glutMainLoop()        



# param = meshing.MeshingParameters(maxh=0.2)
# mesh = GenerateMesh (geom, param)
# mesh.Save ("test.vol")

