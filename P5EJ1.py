# Escribe un programa que escriba a los siguientes número
# (la separación entre número es para facilitar cuántos números se deben escribir en cada bucle)
# y en el que la función range que utilices tenga un ÚNICO argumento y
# que el valor de este se corresponda con el número de elementos que aparecen en la lista
# ( por Ejemplo, para la primera lista range (10)).
for i in (range(10)):
    print(i++1, end="\t")
print('\n')
for i in (range(10)):
    print((i+1)*2, end="\t")
print('\n')
for i in (range(10)):
    print((i+10)*2, end="\t")
print('\n')
for i in (range(6)):
    print((i*4)+10, end="\t")
print('\n')
for i in (range(9)):
    print((-i+8)*5, end="\t")
print('\n')


