# input
n = int(input("Ingrese un número entero: "))
fact = 1
# procesing and output
for i in range(1, n+1):
    fact *= i

print("El factorial de", n, "es", fact)