# -*- coding: utf-8 -*-
"""
juego TIC TAC TOE
programación con algoritmo MIniMax
Juan Carlos Umanzor A.
octubre 2020
"""

import numpy as np
import random
from math import inf as infinity


HUMANO = "X"
COMPU = "0"
posicionesGanadoras = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                       [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                       [0, 4, 8], [2, 4, 6]]
    
print("Iniciamos el juego")

def imprimirMenu():
    print("┌─────┬─────┬─────┐")
    print("│  1  │  2  │  3  │")
    print("├─────┼─────┼─────┤")
    print("│  4  │  5  │  6  │")
    print("├─────┼─────┼─────┤")
    print("│  7  │  8  │  9  │")
    print("└─────┴─────┴─────┘")
    print()
    print("┌─────┬─────┬─────┐")
    print("│  {}  │  {}  │  {}  │".format(casillas[0],casillas[1],casillas[2]))
    print("├─────┼─────┼─────┤")
    print("│  {}  │  {}  │  {}  │".format(casillas[3],casillas[4],casillas[5]))
    print("├─────┼─────┼─────┤")
    print("│  {}  │  {}  │  {}  │".format(casillas[6],casillas[7],casillas[8]))
    print("└─────┴─────┴─────┘")
    


def evaluarTablero(tablero):
    if hayGanador(tablero, COMPU):
        score = +1
    elif hayGanador(tablero, HUMANO):    
        score = -1
    else:
        score = 0
    
    return score


def espaciosLibres():
    espacios=0
    for i in casillas:
        if i==" ":
            espacios=espacios+1
    return espacios


def casillaLibre(casilla):
    if casillas[casilla]==" ":
        return True
    return False


def hayGanador(tablero,jugador):
   for i in posicionesGanadoras:
        if tresIguales(tablero,i,jugador):
            return True
            break      
   return False


def tresIguales(tablero,tripleta,jugador):
    if tablero[tripleta[0]]==tablero[tripleta[1]]==tablero[tripleta[2]]==jugador:
        return True
    else:
        return False


def espaciosDisponibles(tablero):
    espacios=[]
    for i,j in enumerate(tablero):
        if j==" ":
            espacios.append(i)
    
    return espacios

def evaluarGanador(estadoTablero):
    if hayGanador(estadoTablero,COMPU):
        score = +1
    elif hayGanador(estadoTablero,HUMANO):
       score = -1 
    else:
        score = 0
    
    return score
    
def juegoTerminado(tablero):
    return (hayGanador(tablero, HUMANO) or hayGanador(tablero, COMPU))
    
                      
def turnoJugador():
    seguirJugando=True
    print("Turno del jugador humano")
    while seguirJugando:
        jugada=int(input("Seleccione su jugada: "))
     
        if casillaLibre(jugada-1):
            casillas[jugada-1]=HUMANO
            imprimirMenu()
            seguirJugando=False
        else:
            print("casilla ocupada o error, intente de nuevo")

 
        
def turnoCompuMiniMax():    
    print("Turno de la computadora")

    profundidad=len(espaciosDisponibles(casillas))
    if profundidad==0 or juegoTerminado(casillas):
        return
   
    jugada=MiniMax(casillas,profundidad,profundidad,COMPU)
    casillas[jugada[0]]=COMPU
    imprimirMenu()
    


def MiniMax(tablero,profundidad,profundidad2,jugador):
    if jugador==COMPU:
        best = [-1, -infinity]        
    else:
        best = [-1, +infinity]        
    
    if profundidad == 0 or juegoTerminado(tablero):
        score = evaluarTablero(tablero)
        if profundidad+1==profundidad2 and hayGanador(tablero, COMPU):
            score=100
        return [-1, score]
    
    for cell in espaciosDisponibles(tablero):
        tablero[cell]=jugador
        if hayGanador(tablero, COMPU):
            if convertirTablero(tablero) not in jugadasGanadoras:
                jugadasGanadoras.append(convertirTablero(tablero))
                jugadasSalida.append(2)
            
        if hayGanador(tablero, HUMANO):
            if convertirTablero(tablero) not in jugadasGanadoras:
                jugadasGanadoras.append(convertirTablero(tablero))
                jugadasSalida.append(1)
          
        if jugador==COMPU:
            score = MiniMax(tablero, profundidad-1, profundidad2, HUMANO)
        else:
            score = MiniMax(tablero, profundidad-1, profundidad2,  COMPU)
        
        tablero[cell]=" "
        score[0]=cell
        
        
        if jugador==COMPU:
            if score[1] > best[1]:    
                best=score           # max value 
        else:
            if score[1] < best[1]:    
                best=score           # min value
        
    return best
        

def convertirTablero(tablero):
    res = []
    for j in range(9):
        if tablero[j]==" ":
            res.append(0)
        elif tablero[j]==HUMANO:
            res.append(1)
        else:
            res.append(2)
    
    return res


def MiniMaxOLD(tablero,profundidad,jugador):
    if jugador==COMPU:
        best = [-1, -infinity]        
    else:
        best = [-1, +infinity]        
    
    if profundidad == 0 or juegoTerminado(tablero):
        score = evaluarTablero(tablero)
        return [-1, score]
    
    for cell in espaciosDisponibles(tablero):
        tablero[cell]=jugador

        if jugador==COMPU:
            score = MiniMax(tablero, profundidad-1, HUMANO)
        else:
            score = MiniMax(tablero, profundidad-1, COMPU)
        
        tablero[cell]=" "
        score[0]=cell
        
        
        if jugador==COMPU:
            if score[1] > best[1]:    
                best=score           # max value 
        else:
            if score[1] < best[1]:    
                best=score           # min value
        
    return best
        
        
    
    



########################################################
#    inicia el juego
########################################################

jugadasGanadoras=[]*9
jugadasSalida=[]

casillas=[" "]*9
#casillas=["X","X","0",
#          " ","0"," ",
#          " ","0"," ",]

for i in  range(1,10):
    casillas=[" "]*9
    imprimirMenu()
    turnoJugador()
    turnoCompuMiniMax()

np.savetxt('jugadasGanadoras.csv', jugadasGanadoras, delimiter=',', fmt='%i')
np.savetxt('jugadasSalida.csv', jugadasSalida, delimiter=',', fmt='%i')

print(jugadasSalida)
        
if hayGanador(casillas,HUMANO):
    print("ganador el humanmo...")
elif hayGanador(casillas,COMPU):
    print("ganador la compu...")
else:
    print("juego empatado")
 
    
 
        
    
    
