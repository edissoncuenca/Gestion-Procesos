import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Leemos los datos del archivo CSV
tiempo = []
memoria = []
cpu = []

with open('recursos.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  # Ignoramos la primera fila (encabezados)
    for fila in lector_csv:
        tiempo.append(datetime.strptime(fila[0], "%Y-%m-%d %H:%M:%S"))
        memoria.append(float(fila[1]))
        cpu.append(float(fila[2]))

# Creamos la gráfica
plt.figure(figsize=(10, 6))
plt.plot(tiempo, memoria, label='Memoria', color='blue')
plt.plot(tiempo, cpu, label='CPU', color='red')
plt.xlabel('Tiempo')
plt.ylabel('Uso (%)')
plt.title('Consumo de CPU y Memoria')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

# Mostramos la gráfica
plt.tight_layout()
plt.show()
