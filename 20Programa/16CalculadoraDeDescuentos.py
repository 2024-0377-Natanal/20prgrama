precio = float(input("ingresa el precio del producto:"))

if precio < 50:
    print("no tiene descuento")
elif precio >= 50 and precio < 100:
    print("tiene un descuento del 5%")
elif precio >= 100:
    print("tiene un descuento del 10%")
    
