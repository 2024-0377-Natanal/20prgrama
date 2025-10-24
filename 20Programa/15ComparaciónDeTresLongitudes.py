a = float(input("ingresa la longitud del primer lado :"))
b = float(input("ingresa la longitud del segundo lado :"))
c = float(input("ingresa la longitud del tercer lado :"))

if (a + b > c) and (a + c > b) and (b + c > a): 
    print("los lados forman un triangulo")
else:
    print("los lados no forman un triangulo")  
    