import pandas as pd
import matplotlib.pyplot as plt
import Utils.Calculos as utils

url1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1 = pd.read_csv(url1)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tiendas = [tienda1, tienda2, tienda3, tienda4]
#print(tienda3.info())
#print(tienda3.head())
calculos = utils.Calculos

#Primero se evalua el ingreso totales de cada tienda
ingresos = calculos.ingresos_tiendas(tiendas)

#Ventas por categoria mas popular
calculos.ventas_categoria(tiendas)