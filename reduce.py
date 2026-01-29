# -*- coding: utf-8 -*-

from functools import reduce # Comando para importar a biblioteca Reduce

"""def soma(x,y): # Função de Soma entre eles
    return x+y

lista = [1,3,5,10,20,40] # Criação da Lista

soma = reduce(soma,lista) # Formula importando a Biblioteca
print(soma)"""

lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = reduce(lambda x,y: x+y, lista)
print(lista2)

