import numpy as np
import time

a = np.array([1, 2, 3, 4, 5])
ceros = np.zeros((2, 3))
rango = np.arange(0, 10, 2)
espaciado = np.linspace(0, 1, 5)

print('Array base:', a)
print('Matriz de ceros:\n', ceros)
print('Rango:', rango)
print('Espaciado:', espaciado)


n = 1_000_000
lista = list(range(n))
array = np.arange(n)

inicio = time.time()
resultado_lista = [x + 10 for x in lista]
print("Bucle for:", time.time() - inicio, "segundos")

inicio = time.time()
resultado_array = array + 10
print("Vectorizado:", time.time() - inicio, "segundos")


import numpy as np
temperaturas = np.array([12.5, 14.0, 11.8, 13.2, 15.1, 10.9, 12.7])
print('Promedio:', temperaturas.mean())
print('Desviación estándar:', temperaturas.std())
print('Mínima:', temperaturas.min())
print('Máxima:', temperaturas.max())