import matplotlib.pyplot as plt

class Calculos:

    @staticmethod
    def ingresos_tiendas(tiendas):
        ingresos = []
        for tienda in tiendas:
            ingresos.append(tienda['Precio'].sum())

        print("los ingresos de cada tienda en promedio son: ")
        for i in range(len(ingresos)):
            print(f"Tienda {i+1}: {ingresos[i]}")

        return ingresos
    
    @staticmethod
    #En este metodo se calculan la cantidad de productos vendidos por categoria
    def ventas_categoria(tiendas):
        for i in range(len(tiendas)):
            productos = tiendas[i]['Categoría del Producto'].value_counts()
            print(productos)
            # como siempre pone el que mas se repite en primera posicion ese es el mas popular
            print(f"la tienda {i} su producto mas popular es: {productos.index[0]}")