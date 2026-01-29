# -*- coding: utf-8 -*-

def dobro(x): # Função para dobrar os valores
    return x*2

valor = [1,2,3,4,5] # Lista de valores

valor_dobrado = map(dobro,valor) # Variavel para chamar a função MAP 
valor_dobrado = list(valor_dobrado) # Montando em uma lista
print(valor_dobrado)

