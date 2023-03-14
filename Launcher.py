# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:41:17 2023

@author: Crisostomo Alberto Barajas-Solano

Launcher de evaluación Corte 1 - Machine Learning
UDI 2023-I
"""

import numpy as np
from datetime import datetime
from game import main_solve

#%%

# Funcion para crear el estado final        
def CrearFinal():
    
    final = np.zeros([3,3],dtype = int)
    final[0,0]=1
    final[0,1]=2
    final[0,2]=3
    final[1,2]=4
    final[2,2]=5
    final[2,1]=6
    final[2,0]=7
    final[1,0]=8    
    
    return final

# Funcion para crear un estado inicial aleatorio
def CrearInicial():
    
    ini = np.reshape(np.random.permutation(9),[3,3])
    
    return ini

def DistManhattan(A, B):
    
    dist = 0
    for i in range(3):
        for j in range(3):
            result = np.where(A == B[i,j])
            dist = dist + np.abs(i - int(result[0]))
            dist = dist + np.abs(j - int(result[1]))
    
    return dist

#%%

iteraciones = 20

exitoTiempo = list()
exitoAbiertos = list()
exitoCerrados = list()
fracasoTiempo = list()
fracasoCerrados = list()
exito = 0

# estado final, para comparar
final = CrearFinal()

start_total = datetime.now()

for i in range(iteraciones):
    
    print(' ')
    print("Lanzando realizacion " + str(i+1) + ' de ' + str(iteraciones) + '...')
    
    # -------------------------------------------------------------------------
    start_time = datetime.now()
    abiertos, cerrados = main_solve(CrearInicial())
    end_time = datetime.now()
    # -------------------------------------------------------------------------
    
    delta = (end_time-start_time).total_seconds()
    
    if len(abiertos) == 0:
        
        # no hay abiertos, probablemente no encontró una solución
        print('Realizacion finalizada. NO se encontro solucion.\t' + str(delta) +'s')
        fracasoTiempo.append(delta)
        fracasoCerrados.append(len(cerrados))
        
    else:
        
        # aun hay nodos abiertos, probablemente encontró una solución
        
        # evaluando el primer y ultimo nodo de la lista abiertos
        primero = DistManhattan(abiertos[0], final)
        ultimo = DistManhattan(abiertos[-1], final)
        print('Distancia del primer nodo de Abiertos: ' + str(primero))
        print('Distancia del ultimo nodo de Abiertos: ' + str(ultimo))
        
        if (primero == 0) or (ultimo == 0):
            print('Realizacion finalizada. SI se encontro solucion.\t' + str(delta) +'s')
            exito = exito +1
            exitoTiempo.append(delta)
            exitoAbiertos.append(len(abiertos))
            exitoCerrados.append(len(cerrados))
        else:
            print('Realizacion finalizada. NO se encontro solucion.\t' + str(delta) +'s')
            fracasoTiempo.append(delta)
            fracasoCerrados.append(len(cerrados))
            
            
end_total = datetime.now()
tSec = (end_total-start_total).total_seconds()
totalMin = int(np.floor(tSec/60))
totalSec = tSec - totalMin*60

print(' ')
print('-----------------------------------------------------------------------')
print('Tiempo de ejecución: ' + str(totalMin) + 'min : ' + str(totalSec) + 's')
print(' ')
print('Exitos:  ' + str(100*exito/iteraciones) + '%')
print('\tTiempo promedio: \t' + str(sum(exitoTiempo)/len(exitoTiempo)) + 's')
print('\tEvaluados promedio: ' + str(sum(exitoCerrados + exitoAbiertos)/(len(exitoCerrados))))
print(' ')
print('Fracasos:')
print('\tTiempo promedio: \t' + str(sum(fracasoTiempo)/len(fracasoTiempo)) + 's')
print('\tCerrados promedio: \t' + str(sum(fracasoCerrados)/len(fracasoCerrados)))
print('-----------------------------------------------------------------------')
