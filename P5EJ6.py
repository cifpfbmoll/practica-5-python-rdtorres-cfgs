#Escribe un programa que pida altura y ancho de un rectangulo y lo dibuje de la siguiente manera
#Altura triangulo:
altura = int(input("Escriba la altura: "))
print(f'La altura es {altura}')
for i in range(altura):
    for j in range(i + 1):
        print("* ", end="")
    print()