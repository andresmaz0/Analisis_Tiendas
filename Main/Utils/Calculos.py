import matplotlib.pyplot as plt

class Calculos:

    @staticmethod
    def ingresos_tiendas(tiendas):
        print("Ingresos")
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
        print("\nVentas por categoria")
        for i in range(len(tiendas)):
            categorias = tiendas[i]['Categoría del Producto'].value_counts()
            # como siempre pone el que mas se repite en primera posicion ese es el mas popular
            print(f"la tienda {i+1} su producto mas popular es: {categorias.index[0]}")

    @staticmethod
    #En este metodo se calcula la calificacion promedio en cada tienda
    def calificacion_prom(tiendas):
        print("\nCalificacion promedio")
        for i in range(len(tiendas)):
            calificacion = tiendas[i]['Calificación'].mean()
            print(f"la tienda {i+1} tiene una calificacion promedio de: {calificacion}")

    @staticmethod
    def mas_menos_productos(tiendas):
        print("\nMas-Menos-Productos")
        for i in range(len(tiendas)):
            productos = tiendas[i]['Producto'].value_counts()
            print(f"""la tienda {i+1} sus productos mas vendido son: {productos.index[0]} y {productos.index[1]}
            los menos son: {productos.index[-1]} y {productos.index[-2]}""")

    @staticmethod
    def costo_envio_prom(tiendas):
        print("\nCosto envio promedio")
        for i in range(len(tiendas)):
            costo_prom = tiendas[i]['Costo de envío'].mean()
            print(f"El costo de envio promedio de la tienda {i+1} es: {costo_prom}")