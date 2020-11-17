#Escribe un programa que pida altura y ancho de un rectangulo y lo dibuje de la siguiente manera
#Altura triangulo:
altura = int(input("Escriba la altura: "))
print(f'La altura es {altura}')
for i in range(altura, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()