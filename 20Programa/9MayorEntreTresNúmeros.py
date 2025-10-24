num1 = float(input("introdusca el primer numero:"))
num2 = float(input("introdusca el segundo numero:"))
num3 = float(input("introdusca el tercer numero:"))

if num1 > num2 and num1 > num3:
    print("el numero mayor es:", num1)
elif num2 > num1 and num2 > num3:
    print("el numero mayor es:", num2)
elif num3 > num1 and num3 > num2:
    print("el numero mayor es:", num3)
else:
    print("los dos numeros son iguales")