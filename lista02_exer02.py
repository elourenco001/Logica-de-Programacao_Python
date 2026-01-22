# Escreva um programa que abra um arquivo digitado pelo usuário e imprima seu conteúdo na tela.
# -*- coding: utf-8 -*-

nome = input("Digite o nome do arquivo (com extensão): ")
arquivo = open(nome)
linhas = arquivo.readlines() 

for linha in linhas:
    print(linha.strip())