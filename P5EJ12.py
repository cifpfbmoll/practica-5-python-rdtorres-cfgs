num = int((input("Escribe un numero: ")))
contador = num
for i in range(2, num + 1):
    if num % i != 0:
        print(f"{contador} es primo.")
    else:
        print(f"{contador} no es primo")
