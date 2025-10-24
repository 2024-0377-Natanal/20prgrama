angulo = float(input("introdusca el valor del angulo en grado "))

if angulo < 90:
    print("el angulo es agudo.")
elif angulo == 90:
    print("el angulo es recto")
elif angulo > 90 and angulo < 180:
    print("el angulo es absoluto")
elif angulo == 180:
    print("el angulo es llano")
else:
    print("el valor no coresponde a nimgun angulo(el angulo deve de estar entre 0 y 180)")