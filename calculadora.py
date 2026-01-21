# Escreva um programa que receba 2 valores e um sinal, e faça a operação matemática conforme o sinal.

n1 = int (input("Digite o primeiro valor: "))
sinal = input("Digite o sinal da operação (+, -, *, /): ")
n2 = int (input("Digite o segundo valor: "))

if sinal == "+":
    op = n1 + n2

elif sinal == "-":
    op = n1 - n2 

elif sinal == "*":
    op = n1 * n2    

elif sinal == "/":
    op = n1 / n2    

else:
    print("Sinal inválido")

print (op)
