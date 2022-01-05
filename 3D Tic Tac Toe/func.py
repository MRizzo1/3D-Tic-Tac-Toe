from OpenGL.GLUT import *
from OpenGL.GL import *

def LineaHorizontal(A,S,n):
    k,j,i,cont1,cont2=0,0,0,0,0
    while k<n:
        while j<n:
            while i<n:
                if A[k][j][i] in S:
                    cont1+=1
                i+=1
            j+=1
            i=0
            if cont1==n:
                cont2+=1
            cont1=0
        k+=1
        j=0
    return cont2

def LineaVert(A,S,n):
    k,j,i,cont1,cont2=0,0,0,0,0
    while k<n:
        while j<n:
            while i<n:
                if A[k][i][j] in S:
                    cont1+=1
                i+=1
            j+=1
            i=0
            if cont1==n:
                cont2+=1
            cont1=0
        k+=1
        j=0
    return cont2

def Linea3D(A,S,n):
    k,j,i,cont1,cont2=0,0,0,0,0
    while k<n:
        while j<n:
            while i<n:
                if A[i][k][j] in S:
                    cont1+=1
                i+=1
            j+=1
            i=0
            if cont1==n:
                cont2+=1
            cont1=0
        k+=1
        j=0
    return cont2

def LineaDiagoDer(A,S,n):
    k,i,cont1,cont2=0,0,0,0
    while k<n:
        while i<n:
            if A[k][i][i] in S:
                cont1+=1
            i+=1
        i=0
        if cont1==n:
            cont2+=1
        cont1=0
        k+=1
    return cont2

def LineaDiagoIzq(A,S,n):
    k,i,cont1,cont2=0,n-1,0,0
    while k<n:
        while i>=0:
            if A[k][(n-1)-i][i] in S:
                cont1+=1
            i-=1
        i=n-1
        if cont1==n:
            cont2+=1
        cont1=0
        k+=1
    return cont2

def PuntosTotales(Arr,Saved,num):
    return str(Linea3D(Arr,Saved,num)+LineaDiagoDer(Arr,Saved,num)+LineaDiagoIzq(Arr,Saved,num)+LineaHorizontal(Arr,Saved,num)+LineaVert(Arr,Saved,num))

def printText(x,y, type, string):
        glutInit("")
        glColor3f(1,1,1)
        glRasterPos2i(x,y)
        for ch in string:
            glutBitmapCharacter(type, ctypes.c_int( ord(ch) ))
