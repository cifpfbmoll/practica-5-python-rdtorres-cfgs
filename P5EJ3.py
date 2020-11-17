#Escribe un programa que pida dos números y escriba
# la suma de enteros desde el primero hasta el último.
print("PARES E IMPARES")
a = int(input("Escriba un número entero: "))
b = int(input(f"Escriba un número entero mayor o igual que {a}: "))
total = 0
for i in (range(a, b + 1)):
    total = total + i
print(f'La suma de {a} hasta llegar a {b} es {total}')
