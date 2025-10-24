hora = float(input("ingrese la hora (0-23): "))

if hora >= 0 and hora < 23:
    if hora >= 6 and hora < 11:
        print("turno de mañana")
    elif hora >= 12 and hora < 17:
        print("turno de tarde")
    elif hora >= 18 and hora < 23:
        print("turno de noche")
    elif hora >= 0 and hora < 5:
        print("turno de madrugada")