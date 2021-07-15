menu = """
Bienvenido al conversor de monedas 💰

1 - De pesos Colombianos a dólares.
2 - De dólares a pesos Colombianos.

Elige una opción: """

def mensaje_pantalla(moneda):
    print("tienes un total de $" + moneda_resultante + " " + moneda) 

eleccion = input(menu)

if eleccion == "1":
    pesos_colombianos = float(input("¿Cuántos pesos colombianos tienes?: "))
    valor_dolar = 3823.2
    dolares = pesos_colombianos / valor_dolar
    moneda_resultante = str(round(dolares, 3))
    mensaje_pantalla("dólares")
elif eleccion == "2":
    dolares = float(input("¿Cuántos dolares tienes?: "))
    valor_dolar = 3823.2
    peso_colombiano = dolares * valor_dolar
    moneda_resultante = str(round(peso_colombiano, 3))
    mensaje_pantalla("pesos colombianos")
else:
    print("¡No se escogió una entrada valida, por favor intente de nuevo!")