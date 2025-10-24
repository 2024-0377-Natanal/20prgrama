peso = float(input("ingrese su peso en kg:"))
altura = float(input("ingrese su altura en metros:"))

imc = peso / (altura ** 2)
print(f"su indice de masa corporal es:{imc:.2f}")
if imc < 18.5:
    print("bajo peso")
elif imc >= 18.5 and imc < 24.9:
    print("peso normal") 
elif imc >= 25 and imc < 29.9:
    print("sobrepeso") 
elif imc >= 30:
    print("obesidad")  