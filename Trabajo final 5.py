@@ -0,0 +1,26 @@
# Matriz de inventario: [Código, Nombre, Stock Actual, Stock Mínimo]
inventario = [
    [101, "Laptop", 5, 10],
    [102, "Mouse", 20, 15],
    [103, "Teclado", 8, 12],
    [104, "Monitor", 2, 5],
    [105, "Cable HDMI", 50, 20]
]

def calcular_pedido(stock_actual, stock_minimo):
    """Calcula la cantidad a pedir si el stock es insuficiente."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Procesamiento y Salida
print("--- Informe de Pedidos de Inventario ---")
for articulo in inventario:
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]
    
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)
    
    print(f"Artículo: {nombre} | Cantidad a pedir: {cantidad_pedir}")
