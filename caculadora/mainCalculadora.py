import calculadora

operador_a = int(input("Introuduce el primer numero"))
operador_b = int(input("Introuduce el segundo numero"))
operador_opcion = input("Elegi que operacion deaseas ralizar (+ - * /)")


if operador_opcion == "+":
    print(calculadora.suma(operador_a, operador_b))

elif operador_opcion =="-":
    print(calculadora.resta(operador_a, operador_b))

elif operador_opcion == "*":
    print(calculadora.multiplicar(operador_a, operador_b))

elif operador_opcion == "/":
    print(calculadora.dividir(operador_a, operador_b))

else:
    print("El operador no es válido")