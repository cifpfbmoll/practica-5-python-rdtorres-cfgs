#Escribe un programa que pida un número y calcule su factorial.
a = int(input("Escriba un número entero: "))
total = 1
for i in (range(1, a + 1)):
    total = total * i
print(f'El facotrial de {a} es = {total} ')
