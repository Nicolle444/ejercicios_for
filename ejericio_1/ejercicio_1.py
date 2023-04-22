#intput
n = int(input("Ingrese la cantidad de números enteros que desea ingresar: "))
n_pares = 0
n_impares = 0

for i in range(n):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        n_pares += 1
    else:
        n_impares += 1

print("Cantidad de números pares:", n_pares)
print("Cantidad de números impares:", n_impares)