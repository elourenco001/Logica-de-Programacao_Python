
nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")        

media = (float(nota1) + float(nota2)) / 2

if media >= 6:
    print ("Aprovado, sua média foi de", media)  
else:
    print ("Reprovado, sua média foi de", media)