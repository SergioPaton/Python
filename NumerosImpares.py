numero_1 = int(input("Introduce el primer numero: "))
numero_2 = int(input("Introduce el segundo numero: "))
for i in range(numero_1, numero_2, 2):
	if i%2!=0:
		print(i)