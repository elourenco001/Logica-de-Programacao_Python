# -*- coding: utf-8 -*-

def pares(i):
    if i % 2 == 1: # Formula para trazer numeros [0]-Pares [1]-Impares
        return i
    
lista = [0,1,2,3,4,5,6,7,8,9,10]

lista_pares = filter(pares, lista) # Filter "Filtro" para trazer apenas os dados solicitados
print (list(lista_pares))