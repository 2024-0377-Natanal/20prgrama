num = float(input("ingrese la calificacion (0-100):"))

if num < 0 or num > 100:
    print("la calificacion deve de estar entre 0 y 100")
else:
    if num >= 60:
        print("aprobado")
    else: 
        print("reprobado")
        