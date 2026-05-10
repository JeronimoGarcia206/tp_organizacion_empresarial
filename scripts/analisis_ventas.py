import pandas as pd
import matplotlib.pyplot as plt

# Lectura del dataset
df = pd.read_csv("datos/ventas.csv")

# Calcular total por venta
df["total"] = df["cantidad"] * df["precio"]

# Ventas totales
ventas_totales = df["total"].sum()

# Producto más vendido
ventas_producto = df.groupby("producto")["cantidad"].sum()
producto_mas_vendido = ventas_producto.idxmax()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Guardar resumen
with open("resultados/resumen.txt", "w") as archivo:
    archivo.write(f"Ventas totales: {ventas_totales}\n")
    archivo.write(f"Producto más vendido: {producto_mas_vendido}")

# Generar gráfico
ventas_producto.plot(kind="bar")

plt.title("Cantidad vendida por producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

# Mostrar gráfico
plt.show()
