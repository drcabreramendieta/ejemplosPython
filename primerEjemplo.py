print("Hola")
print("mundo")

a = 12

if a <= 15:
    print("a es menor o igual a 15")
    print("a es ", a)
else:
    print("a es mayor que 15")

while a <= 15:
    print("Dentro del bucle a es ", a)
    a += 1 # a = a + 1

lista = [1,3,5,7]
for e in lista:
    print("elemento ", e)

rango = range(0,10,2)
for e in rango:
    print("rango:",e)