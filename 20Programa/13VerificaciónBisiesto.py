año = int(input("ingrese un año: "))

if (año % 400 == 0):
    print("el año es bisiesto")
elif (año % 100 == 0):
    print("el año no es bisiesto")
elif (año % 4 == 0):
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")

