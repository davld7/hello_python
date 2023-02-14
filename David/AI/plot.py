# Se importa el módulo matplotlib.pyplot y se le asigna el nombre de la instancia "pyplot".
import matplotlib.pyplot as pyplot
# Título del gráfico(plot).
pyplot.title("Gastos de los últimos 6 meses.")
# Eje X.
pyplot.xlabel("Meses")
# Eje Y.
pyplot.ylabel("Gastos")
# Lista Meses.
months = ["Mes 1", "Mes 2", "Mes 3", "Mes 4", "Mes 5", "Mes 6"]
# Pedir al usuario que ingrese los valores separados por comas.
bills_input = input(
    "Ingrese los gastos de los últimos 6 meses separados por comas: ")
# Convertir la cadena de entrada en una lista de cadenas.
bills_values = bills_input.split(",")

# Lista Gastos.
# Convertir la lista de cadenas en una lista de números reales.
bills = list(map(float, bills_values))

# Se dibuja el gráfico y luego se muestra.
pyplot.plot(months, bills)
pyplot.show()
