import pandas as pd

df = pd.read_csv("gastos_practica.csv")

#Mostrar el tamaño de los datos (filas, columnas)\<>
print(f"Tamaño del set de datos (row,column): {df.shape}")
print("\n")

#Mostrar las primeras filas (en este caso todas por la cantidad)
print(df.head(len(df)))
print("\n")

#Mostrar información general del dataframe
df.info()
print("\n")

#Descripciones estadísticas de las columnas numéricas
print(round(df.describe()))
print("\n")

#Detectamos valores nulos
print(df.isnull().sum())
print("\n")

#Rellenamos valores faltantes
df["monto"] = df["monto"].fillna(0)
df["metodo_pago"] = df["metodo_pago"].fillna("Desconocido")

#Convertimos los tipos de datos a los que no coinciden
df["fecha"] = pd.to_datetime(df["fecha"])
df["monto"] = pd.to_numeric(df["monto"])

#Mostramos los cambios
df.info()
print("\n")

""" Análisis básico """
print("Análisis básico")
print("\n")

#Gasto total
print(f"Gasto total: {df['monto'].sum()}")

#Gasto promedio
print(f"Gasto promedio: {df['monto'].mean()}")
print("\n")
      
#Gasto total por categoria
gasto_total_categoria = df.groupby("categoria")["monto"].sum()
print(f"Gasto total por categoria: \n{gasto_total_categoria}")
print("\n")

#Categoría con mayor gasto
categoria_max_gasto = gasto_total_categoria.idxmax()
print(f"Categoría con mayor gasto: \n{categoria_max_gasto}")
print("\n")

#Gasto total por método de pago
gasto_total_pago = df.groupby("metodo_pago")["monto"].sum()
print(f"Gasto total por método de pago: \n{gasto_total_pago}")
print("\n")

""" Filtros """
print("Filtros")

#Todos los gastos de Comida
total_gastos_comida = df[df["categoria"] == "Comida"]
print(f"Todos los gastos de Comida: \n{total_gastos_comida}")
print("\n")

#Gastos mayores a 20.000
gastos_mayor_20k = df[df["monto"] > 20000]
print(f"Gastos mayores a 20.000 \n{gastos_mayor_20k}")
print("\n")

#Gastos realizados con Tarjeta
gastos_tarjeta = df[df["metodo_pago"] == "Tarjeta"]
print(f"Gastos realizados con Tarjeta: \n{gastos_tarjeta}")
print("\n")

""" Ordenar el DataFrame antes de guardarlo en archivo """
#Ordenado por monto de mayor a menor
df_ordenado = df.sort_values(by="monto", ascending=False)
print(df_ordenado)

gasto_categoria = df.to_csv("resumen_categoria.csv")
final_dataset = df.to_excel("dataset_gastos_limpio.xlsx", index=False)



