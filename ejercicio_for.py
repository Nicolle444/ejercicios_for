# caso 1
x = range (10)
for i in x:
    print(i)

# caso 2
x = range (10)
rta = "rango: | "
for i in x:
    rta = rta + str(i) + ","
    rta = rta + "|"
print (rta)

# caso 4 
x = range(3,10,2)
rta = "rango = |"
for i in x:
    rta = rta + str(i) + ", "
rta = rta + "|"
print (rta)


