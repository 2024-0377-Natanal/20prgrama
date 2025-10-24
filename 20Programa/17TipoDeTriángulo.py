a = float(input("ingresa la longitud del primer lado :"))
b = float(input("ingresa la longitud del segundo lado :"))
c = float(input("ingresa la longitud del tercer lado :"))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("el triangulo es equilatero")
    elif a == b or b == c or a == c:
        print("el triangulo es isoceles") 
    else:
        print("el triangulo es escaleno")
else:
    print("las longitudes no forman un triangulo")  
    