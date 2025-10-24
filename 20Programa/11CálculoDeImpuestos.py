impuesto = float(input("introduzca su salario:"))

if impuesto < 10.000:
    print("no paga impuestos")
elif impuesto >= 10.000 and impuesto < 30.000:
    print("paga un 10% de impuestos")
elif impuesto >= 30.000:
    print("paga un 20% de impuestos")