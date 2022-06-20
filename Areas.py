'''Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros
 y otra función que calcule el área de un círculo recibiendo el radio del mismo.'''

import math

def AreaTriangulo(altura, base):
    AreaTriangulo= (altura*base)/2
    print("El area es: ", round(AreaTriangulo, 2))

def AreaCirculo(radio):
     AreaCirculo= math.pi*radio
     print("El area es: ", round(AreaCirculo,2))

altura=float(input("Introduce la altura: "))
base=float(input("Instroduce la base: "))
AreaTriangulo(altura, base)

radio=float(input("Introduce el radio: "))
AreaCirculo(radio)