# Escreva um programa que leia um arquivo multi-txt e armazene em um dicionário: Cabeçalho da sequencia com a chave e a sequencia como valor

# -*- coding: utf-8 -*-

arquivo = open("Insulina.txt")

linhas = arquivo.readlines()
multifasta = {}

for linha in linhas:
    if linha[0] ==">":
        seq_atual = linha[1:].strip()
        multifasta[seq_atual] = ""
    else:
        multifasta[seq_atual] = f"{multifasta[seq_atual]}{linhas[1].strip()}"

print (multifasta ["seq2"]) 