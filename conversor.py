eleccion = input("Bienvenido, ¿Qué moneda deseas convertir: Dólares o Pesos Colombianos 1 para Pesos Colombianos o 2 para Dólares: ")

if eleccion == "1":
    pesos_colombianos = float(input("¿Cuántos pesos colombianos tienes?: "))
    valor_dolar = 3823.2
    dolares = pesos_colombianos / valor_dolar
    dolares = str(round(dolares, 3))
    print("Tienes un total de $" + dolares + " dólares.")
elif eleccion == "2":
    dolares = float(input("¿Cuántos dolares tienes?: "))
    valor_dolar = 3823.2
    peso_colombiano = dolares * valor_dolar
    peso_colombiano = str(round(peso_colombiano, 3))
    print("Tienes un total de $" + peso_colombiano + " pesos Colombianos.")
else:
    print("¡No se escogió una entrada valida, por favor intente de nuevo!")