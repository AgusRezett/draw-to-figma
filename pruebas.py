import matplotlib.pyplot as plt
import numpy as np

# Lista de contornos
contours = ...
with open("contours.txt", "r") as file:
    contours = file.readlines()
    contours = [np.array(eval(contour)) for contour in contours
                if len(eval(contour)) > 0
                and len(eval(contour)[0]) > 0
    ]

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Establecer el color del ciclo para tener diferentes colores para cada contorno
ax.set_prop_cycle('color', plt.cm.tab20(np.linspace(0, 1, len(contours))))

# Graficar cada contorno
for contour in contours:
    # Convertir a un arreglo numpy y cambiar la forma para graficar
    contour_array = np.array(contour).reshape(-1, 2)
    ax.plot(contour_array[:, 0], contour_array[:, 1], marker='o', linestyle='-', linewidth=2)

# Configurar los límites de la gráfica
ax.set_xlim(200, 600)
ax.set_ylim(100, 500)
ax.invert_yaxis()  # Invertir el eje Y para coincidir con la orientación de las coordenadas de imagen

# Añadir etiquetas y título
plt.title("Visualización de Contornos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostrar la gráfica
plt.grid(True)
plt.show()
