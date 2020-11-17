#Escribe un programa que pida altura y ancho de un rectangulo y lo dibuje de la siguiente manera
#Anchura rectangulo:
#Altura rectangulo:
anchura = int(input("Escriba la anchura: "))
altura = int(input("Escriba la altura: "))
print(f'La anchura es {anchura}')
print(f'La altura es {altura}')
for i in range(altura):
    for j in range(anchura):
        print("* ", end='\t')
    print()
