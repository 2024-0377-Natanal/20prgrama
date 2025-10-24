tenp = float(input("ingresa la tenperatura en grados celsius:"))

if tenp < 0: 
    print("hace mucho frio")
elif tenp >= 0 and tenp < 20:
    print("clima fresco")
elif tenp >= 21 and tenp < 30:
    print("clima agradable")
elif tenp >= 30:
    print("hace mucho calor")