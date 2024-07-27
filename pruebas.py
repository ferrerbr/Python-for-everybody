import math

while True:
    geo = input("que forma geometrica quieres calcular? (cuadrado, rectangulo, triangulo, circulo)")
    
    if geo == "cuadrado":
        lado = input("introduce el valor del lado: ")
        lado = float(lado)
        area = lado * lado
        print("Area=",area)
        break

    if geo == "rectangulo":
        altura = input("introduce la altura: ")
        altura = float(altura)
        base = input("introduce la base: ")
        base = float(base)
        area = base * altura
        print("Area=",area)
        break

    if geo == "triangulo":
        altura = input("introduce la altura: ")
        altura = float(altura)
        base = input("introduce la base: ")
        base = float(base)
        area=(base*altura)/2
        print("Area=",area)
        break

    if geo == "circulo":
        radio = input("introduce el radio: ")
        radio = float(radio)
        area = math.pi*radio**2
        print("Area=",area)
        break

    if  geo == "fin":
        break
    else:
        print("por favor introduce una figura geometrica")
    

