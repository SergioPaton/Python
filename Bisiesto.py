def checkYear(year):
    if year%400 == 0 or year%4 == 0:
        return True
    else:
        return False

year = int(input("Introduce un año: "))
if checkYear(year):
    print(year, " Es bisiesto")
else:
    print(year, "No es bisisto")