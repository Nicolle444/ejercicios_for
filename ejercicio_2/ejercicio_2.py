multiplos_7 = 0
multiplos_9 = 0

for i in range(1000, 5001):
    if i % 7 == 0:
        multiplos_7 += 1
    if i % 9 == 0:
        multiplos_9 += 1

print("Cantidad de múltiplos de 7:", multiplos_7)
print("Cantidad de múltiplos de 9:", multiplos_9)