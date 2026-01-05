import pandas as pd

#Convertimos el archivo csv en un DataFrame con pandas
df = pd.read_csv("gastos.csv")

"""Métodos de pandas para explorar los datos"""

#Este método muestra las primeras filas del df
print(df.head())
print("|-------------------------------------|")

#Este método genera información de los datos, como las columnas,
#el tipo gastos.csv

df.info()
print("|-------------------------------------|")
#Este método muestra estadísticas básicas de columnas matemáticas
#Ej: promedio, max, min 
print(round(df.describe(),3))
print("|-------------------------------------|")

""" Limpieza de datos """

#Detectamos qué columnas tienen valores nulos para realizar la limpieza
print("Detección de valores nulos")
print("")
print(df.isnull().sum())
print("|-------------------------------------|")

""" Rellenamos los valores faltantes """

#Caso 1: monto vacio:
df["monto"] = df["monto"].fillna(0)

#Caso 2: metodo_pago vacio:
df["metodo_pago"] = df["metodo_pago"].fillna("Desconocido")

print("|-------------------------------------|")

print(df.head(len(df)))

print("|-------------------------------------|")

""" Convertir tipos de datos """

#Convertimos fecha de string a datetime
df["fecha"] = pd.to_datetime(df["fecha"])

#Aseguramos que monto sea numérico
df["monto"] = pd.to_numeric(df["monto"])

df.info()

print("|-------------------------------------|")

""" Análisis básico """
#Suma total de los gastos
print(f'Suma de gastos total: {df["monto"].sum()}')
print("")
#Gasto por categoría
gasto_categoria = df.groupby("categoria")["monto"].sum()

print("Gastos totales por categoria: ")
print(gasto_categoria)
print("")

#Gasto promedio
print(f'Gasto promedio: {df["monto"].mean()}')

print("|-------------------------------------|")

""" Filtrar datos """

#Filtrar categoria solo Comida
print(f"Filtro de categoria == Comida: ")
print("")
print(df[df["categoria"] == "Comida"])

print("")

#Filtrar por gastos mayores a 10.000
print(f"Filtro de gasto > 10000: ")
print("")
print(df[df["monto"] > 10000])

gasto_categoria.to_csv("resumen_gastos.csv")

df.to_csv("new_gastos.csv")















