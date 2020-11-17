#Escribe un programa que pida altura y ancho de un rectangulo y lo dibuje de la siguiente manera
#Anchura rectangulo:
#Altura rectangulo:
altura = int(input("Escriba la altura: "))
anchura = int(input("Escriba la anchura: "))
print(f'La altura es {altura}')
print(f'La anchura es {anchura}')
for i in range(anchura):
    print("* ", end="")
print()
for i in range(altura - 2):
    print("* ", end="")
    for j in range(anchura + 1):
        print(" ", end="")
    print("*")
for i in range(anchura):
    print("* ", end="")
