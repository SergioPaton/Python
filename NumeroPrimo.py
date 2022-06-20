#Escribe una función que pueda decirte si un número (número entero) es primo o no.

def comprobarPrimo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True


numero=int(input("Introduce un numero: "))
if comprobarPrimo(numero):
    print(numero, " Es primo")
else:
    print(numero, " No es primo")
