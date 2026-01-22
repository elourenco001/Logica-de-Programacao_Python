#Escreva um programa que receba uma sequência digitada pelo usuário e a salve num arquivo no formato txt. 

# -*- coding: utf-8 -*-

seq = input ("Digite uma sequencia: ")

arquivo = open("insulina.txt", "w")

arquivo.write(">seq\n")
arquivo.write(seq)  
arquivo.close()

