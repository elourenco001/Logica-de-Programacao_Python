# -*- coding: utf-8 -*-

x = [1,2,3,4,5]
y = [i**2 for i in x]
z = [i for i in x if i%2==1]

print("Usando List Comprehension")
print(x)
print(y)
print(z)
