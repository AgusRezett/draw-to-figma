import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread('data/boceto.jpg')
image2 = cv2.imread('data/blanco.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización adaptativa
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 10)

# Buscar contornos en la imagen umbralizada
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos impares en la imagen original con color negro
for i, contour in enumerate(contours):
    # Dibujar el contorno en la imagen blanca con color negro
    cv2.drawContours(image2, [contour], -1, (0, 0, 0), 1)
    # Obtener el punto inicial del contorno
    x, y = contour[0][0]

# Guardar la imagen con los contornos y etiquetas
cv2.imwrite('contornos.jpg', image2)

with open('data/contours.txt', 'w') as file:  # Cambio aquí: 'w' en lugar de 'wb'
    for i, contorno in enumerate(contours):
        file.write(f"Contorno {i}:\n")
        for punto in contorno:
            file.write(f"{punto[0][0]}, {punto[0][1]}\n")
        file.write("\n")

