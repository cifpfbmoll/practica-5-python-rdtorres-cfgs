#Escribe un programa que pida altura y ancho de un rectangulo y lo dibuje de la siguiente manera
#Altura triangulo:
num = int(input("Dime un numero: "))
for i in range(1,num + 1):
    if num % i == 0:
        print(i, end=" ")

