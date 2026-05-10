import pandas as pd

#Lectura del dataset
df = pd.read_csv("datos/ventas.csv")

#Calcular total por venta
df["total"] = df["cantidad"] * df["precio"]

#Ventas totales
ventas_totales = df["total"].sum()

#Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

#Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

#Guardar resultados
with open("resultados/resumen.txt", "w") as archivo:
    archivo.write(f"Ventas totales: {ventas_totales}\n")
    archivo.write(f"Producto más vendido: {producto_mas_vendido}")
