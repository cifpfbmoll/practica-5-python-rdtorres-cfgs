# Escribe un programa que pida dos números y escriba qué números entre ese par de números
# son pares y cuáles impares
print("PARES E IMPARES")
a = int(input("Escriba un número entero: "))
b = int(input(f"Escriba un número entero mayor o igual que {a}: "))
for i in (range(a, b, 1)):
    if i % 2 == 0:
        print(f'El número {i} es par.')
    else:
        print(f'El número {i} es impar.')
