num1 = int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero:"))
num3 = int(input("ingrese el tercer numero:"))

if num1 == 0 or num2 == 0 or num3 == 0:
    print("se encuentra un numero cero")
elif num1 > 0 and num2 > 0 and num3 > 0:
    print("los tres numeros son positivos")
elif num1 < 0 and num2 < 0 and num3 < 0:
    print("los tres numeros son negativos")
else:
    print("hay numeros mixtos y (positivos y negativos)")   