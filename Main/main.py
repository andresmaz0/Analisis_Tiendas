import pandas as pd
#pd.options.display.max_columns = None
import matplotlib.pyplot as plt
import Utils.Calculos as utils
from matplotlib.ticker import MultipleLocator

url1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1 = pd.read_csv(url1)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tiendas = [tienda1, tienda2, tienda3, tienda4]
tiendas_string = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']
#print(tienda3.info())
#print(tienda3.head())
calculos = utils.Calculos

#Primero se evalua el ingreso totales de cada tienda
ingresos = calculos.ingresos_tiendas(tiendas)

#Ventas por categoria mas popular
calculos.ventas_categoria(tiendas)

#Conocer la calificacion de los clientes en cada tienda
calificaciones = calculos.calificacion_prom(tiendas)

#Productos mas y menos vendidos
calculos.mas_menos_productos(tiendas)

#Costo de envio promedio
costos = calculos.costo_envio_prom(tiendas)

#Graficas
#Ingresos
plt.figure()
plt.title('Ingresos promedio por tienda')
plt.bar(tiendas_string, ingresos)

#Calificaciones
plt.figure()
plt.title('Calificacion por tienda')
#plt.gca().yaxis.set_major_locator(MultipleLocator(0.15))
plt.scatter(tiendas_string, calificaciones)

#Costos
plt.figure()
plt.title('Costos de envio por tienda(miles)')
plt.pie(costos,labels=tiendas_string,autopct='%1.1f', startangle=90)
plt.show()