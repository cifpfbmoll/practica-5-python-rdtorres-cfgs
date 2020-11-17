#Escribe un programa que pida altura y ancho de un rectangulo y lo dibuje de la siguiente manera
#Altura triangulo:
altura = int(input("Altura del triángulo: "))
for i in range(1, altura + 1):
    for j in range(altura - i):
        print("  ", end="")
        #importante dejar 2 espacios o queda descolocado
    for j in range(1, i + 1):
        print("* ", end="")
    for j in range(1, i):
        print("* ", end="")
    print()
