import random

n = int(input("Ingrese la cantidad de lanzamientos de dados: "))

frecuencias = [0] * 6 

for i in range(n):
     cara = random.randint(1, 6)
     frecuencias[cara-1] += 1 

print("Frecuencias:")
for i in range(6):
    print(str(i+1) + ": " + "*" * frecuencias[i])