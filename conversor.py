menu = """
Bienvenido al conversor de monedas 馃挵

1 - De pesos Colombianos a d贸lares.
2 - De d贸lares a pesos Colombianos.

Elige una opci贸n: """

def mensaje_pantalla(moneda):
    print("tienes un total de $" + moneda_resultante + " " + moneda) 

eleccion = input(menu)

if eleccion == "1":
    pesos_colombianos = float(input("驴Cu谩ntos pesos colombianos tienes?: "))
    valor_dolar = 3823.2
    dolares = pesos_colombianos / valor_dolar
    moneda_resultante = str(round(dolares, 3))
    mensaje_pantalla("d贸lares")
elif eleccion == "2":
    dolares = float(input("驴Cu谩ntos dolares tienes?: "))
    valor_dolar = 3823.2
    peso_colombiano = dolares * valor_dolar
    moneda_resultante = str(round(peso_colombiano, 3))
    mensaje_pantalla("pesos colombianos")
else:
    print("隆No se escogi贸 una entrada valida, por favor intente de nuevo!")