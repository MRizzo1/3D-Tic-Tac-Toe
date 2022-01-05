"""
*IMFORMACIÓN*
Algoritmo del Juego Tres en linea en 3D
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import func
import index

#N=int(input()) Variable Global. No la Necesito porque se la paso por parametro
#a la funcion main()

class Cuadrado:       #Dibuja un cuadrado del Cuadriculado

    def __init__(self,x,y,z):       #Inicializa el Cuadro
        self.vertices=[[x,y,z],
                        [x,y-2,z],
                        [x+2,y-2,z],
                        [x+2,y,z]]
        self.ladito=[[0,1],[1,2],[2,3],[3,0]]
        self.superficies=[[0,1,2,3]]


    def draw(self,r,g,b):
        self.colorear(r,g,b)

        glBegin(GL_LINES)   #Dibuja lineas
        for lado in self.ladito:
            for vertice in lado:
                glVertex3fv(self.vertices[vertice])
                glColor3f(1,1,1)
        glEnd()

    def colorear(self,r,g,b):  #Rellena Las Superficies
        glBegin(GL_QUADS)
        for superficie in self.superficies:
            for vertice in superficie:
                glColor3f(r,g,b)
                glVertex3fv(self.vertices[vertice])
        glEnd()





"""
    p -> Selector de Tablero
    e -> Boton de ENTER
    k1 ->  Selector de Columna
    k2 -> Selector de fila
    s1 -> Variable auxiliar almacenar coordenada k1 del jugador azul
    s2 -> Variable auxiliar almacenar coordenada k2 del jugador azul
    s3 -> Variable auxiliar almacenar coordenada k1 del jugador rojo
    s4 -> Variable auxiliar almacenar coordenada k2 del jugador rojo
    s5 -> Variable auxiliar almacenar coordenada c del jugador azul
    s6 -> Variable auxiliar almacenar coordenada c del jugador rojo
    savedcuadradoA -> Array que guarda los cuadrados del jugador azul
    savedcuadradoR -> Array que guarda los cuadrados del jugador rojo
    Colores -> Array que almacena las tuplas con colores.
    v1,v2 -> Permiten la rotación de los tableros de izquierda a derecha (presiona tecla a, d)
    w,s -> Permiten la rotación de los tableros de arriba a abajo cambiando la perspectiva (presiona tecla w, s)
"""
def main(N,p1,p2):
    pygame.init()
    display=(800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("N-In-Line Game")
    icon = pygame.image.load("img/ico.ico")
    pygame.display.set_icon(icon)

    gluPerspective(45, (display[0]/display[1]), 0.1, 60)

    glTranslatef(0,0,-60)

    glRotatef(-68,3,1,1.5)

    c=N-1 #Contador del piso del tablero
    p,e,k1,k2,s1,s2,s3,s4,s5,s6=0,0,0,0,0,0,0,0,0,0
    Colores=[(0.0588235294, 0.364705882, 0.517647059), (0.22352941,0.729411765,0.71372549),(0,0.2,0.2),(0.592156863,0.141176471,0.545098039),(0.470588235,0.68627451,0.68627451),(0.737254902,0.309803922,0.694117647)]
    cuadrados=[[[Cuadrado(2*n,1-2*n1-2,2*n2) for n in range(N)] for n1 in range(N)]for n2 in range(N)]
    jugadas=N*N*N
    savedcuadradoA=[]
    savedcuadradoR=[]
    v1,v2,w,s=0,0,0,0
    valida=0
    clock=pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if jugadas>0:
            if keys[pygame.K_LEFT] and k1!=0 and e!=0:
                k1-=1
            if keys[pygame.K_RIGHT] and k1!=N-1 and e!=0:
                k1+=1
            if keys[pygame.K_UP] and c!=N-1 and e==0:
                p=1
                c+=1
            elif keys[pygame.K_UP] and k2!=0 and e!=0:
                k2-=1
            if keys[pygame.K_DOWN] and c!=0 and e==0:
                p=1
                c-=1
            elif keys[pygame.K_DOWN] and k2!=N-1 and e!=0:
                k2+=1
            if keys[pygame.K_RETURN] and e==0 and jugadas==N*N*N:
                e=1
            elif keys[pygame.K_RETURN] and e==0 and jugadas<N*N*N:
                if (N*N*N)%2==0 and jugadas%2==0:
                    e=1
                elif (N*N*N)%2==0 and jugadas%2!=0:
                    e=2
                elif (N*N*N)%2!=0 and jugadas%2!=0:
                    e=1
                elif (N*N*N)%2!=0 and jugadas%2==0:
                    e=2
            elif keys[pygame.K_RETURN] and e==2:
                e=1
            elif keys[pygame.K_RETURN] and e==1:
                e=2
            if keys[pygame.K_TAB]:
                e=0
                k1,k2=0,0
            if keys[pygame.K_d] and v1<=10:
                glRotatef(3,0,0,abs(v1))
                v1+=1
                v2-=1
            if keys[pygame.K_a] and v2<=13:
                glRotatef(3,0,0,-abs(v2))
                v2+=1
                v1-=1
            if keys[pygame.K_w] and w<=6:
                glRotatef(3,-abs(w),-abs(w),0)
                w+=1
                s-=1
            if keys[pygame.K_s] and s<=3:
                glRotatef(3,abs(s),abs(s),0)
                w-=1
                s+=1
        else:
            if keys[pygame.K_y]:
                pygame.quit()
            if keys[pygame.K_n]:
                pygame.quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        for k in range(N-1):
            for j in range(N):
                for i in range(N):
                    if p==0:
                        if cuadrados[N-1][j][i] in savedcuadradoA:
                            cuadrados[N-1][j][i].draw(Colores[2][0],Colores[2][1],Colores[2][2])
                        elif cuadrados[N-1][j][i] in savedcuadradoR:
                            cuadrados[N-1][j][i].draw(Colores[3][0],Colores[3][1],Colores[3][2])
                        else:
                            cuadrados[N-1][j][i].draw(Colores[1][0],Colores[1][1],Colores[1][2])
                    else:
                        if cuadrados[N-1][j][i] in savedcuadradoA:
                            cuadrados[N-1][j][i].draw(Colores[2][0],Colores[2][1],Colores[2][2])
                        elif cuadrados[N-1][j][i] in savedcuadradoR:
                            cuadrados[N-1][j][i].draw(Colores[3][0],Colores[3][1],Colores[3][2])
                        else:
                            cuadrados[N-1][j][i].draw(Colores[0][0],Colores[0][1],Colores[0][2])
                    if cuadrados[k][j][i] in savedcuadradoA:
                        cuadrados[k][j][i].draw(Colores[2][0],Colores[2][1],Colores[2][2])
                    elif cuadrados[k][j][i] in savedcuadradoR:
                        cuadrados[k][j][i].draw(Colores[3][0],Colores[3][1],Colores[3][2])
                    else:
                        cuadrados[k][j][i].draw(Colores[0][0],Colores[0][1],Colores[0][2])

        if p==1:
            for x in range(N):
                for y in range(N):
                    if cuadrados[c][y][x] in savedcuadradoA:
                        cuadrados[c][y][x].draw(Colores[2][0],Colores[2][1],Colores[2][2])
                    elif cuadrados[c][y][x] in savedcuadradoR:
                        cuadrados[c][y][x].draw(Colores[3][0],Colores[3][1],Colores[3][2])
                    else:
                        cuadrados[c][y][x].draw(Colores[1][0],Colores[1][1],Colores[1][2])

        if e==1:
            s2,s1,s5=k2,k1,c
            if len(savedcuadradoA)!=0 and cuadrados[s6][s4][s3] not in savedcuadradoA and cuadrados[s6][s4][s3] not in savedcuadradoR:
                savedcuadradoR.append(cuadrados[s6][s4][s3])
                jugadas-=1
                valida=0
            elif len(savedcuadradoA)!=0 and cuadrados[s6][s4][s3] in savedcuadradoA:
                e=2
                valida=1
            else:
                cuadrados[c][k2][k1].draw(Colores[4][0],Colores[4][1],Colores[4][2])


        if e==2:
            s3,s4,s6=k1,k2,c
            if cuadrados[s5][s2][s1] not in savedcuadradoR and cuadrados[s5][s2][s1] not in savedcuadradoA:
                savedcuadradoA.append(cuadrados[s5][s2][s1])
                jugadas-=1
                valida=0
            if len(savedcuadradoR)!=0 and cuadrados[s5][s2][s1] in savedcuadradoR :
                e=1
                valida=1
            else:
                cuadrados[c][k2][k1].draw(Colores[5][0],Colores[5][1],Colores[5][2])

        glMatrixMode( GL_MODELVIEW )
        glPushMatrix()
        glLoadIdentity()

        glMatrixMode( GL_PROJECTION )
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D( 0, display[0], display[1], 0 )


        func.printText(10,50, GLUT_BITMAP_HELVETICA_18, p1)
        func.printText(10,100, GLUT_BITMAP_HELVETICA_18,func.PuntosTotales(cuadrados,savedcuadradoA,N))
        func.printText(680,50, GLUT_BITMAP_HELVETICA_18,p2)
        func.printText(680,100, GLUT_BITMAP_HELVETICA_18,func.PuntosTotales(cuadrados,savedcuadradoR,N))

        func.printText(600,600,  GLUT_BITMAP_HELVETICA_10, "Instrucciones:")
        func.printText(600,630,  GLUT_BITMAP_HELVETICA_10,"Movimientos de cámara: a,s,d,w")
        func.printText(600,660,  GLUT_BITMAP_HELVETICA_10,"Movimiento entre tableros: flechas")
        func.printText(600,690,  GLUT_BITMAP_HELVETICA_10,"Selección de tablero y realizar jugada: enter")
        func.printText(600,720,  GLUT_BITMAP_HELVETICA_10,"Movimientos en el tablero: flechas")
        func.printText(600,750,  GLUT_BITMAP_HELVETICA_10,"Volver al modo selección de tablero: tab")

        if jugadas==0:
            func.printText(300,400, GLUT_BITMAP_TIMES_ROMAN_24,"¿Quieres jugar de nuevo?")
            func.printText(350,450, GLUT_BITMAP_TIMES_ROMAN_24,"Y")
            func.printText(450,450, GLUT_BITMAP_TIMES_ROMAN_24,"N")

        if valida!=0:
            func.printText(300,700, GLUT_BITMAP_HELVETICA_18,"Jugada inválida")

        glPopMatrix()
        glMatrixMode( GL_MODELVIEW )
        glPopMatrix()

        pygame.display.flip()
