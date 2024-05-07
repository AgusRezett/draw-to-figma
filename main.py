
import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('data/boceto.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización adaptativa
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 10)

# Buscar contornos en la imagen umbralizada
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen original con color negro
for contour in contours:
    # Calcular el área del contorno
    area = cv2.contourArea(contour)
    if area > 100:  # Filtro para eliminar contornos pequeños
        # Dibujar el contorno en la imagen original con color negro
        cv2.drawContours(image, [contour], -1, (0, 0, 0), 2)


print(f"Contornos detectados: {contours}")


# Clasificar los contornos detectados en categorías
botones = []
campos_texto = []
imagenes = []

# Umbral inicial para los botones
umbral_botones = 500
# Umbral inicial para los campos de texto
umbral_campos_texto = 200

for contour in contours:
    # Calcular el área del contorno
    area = cv2.contourArea(contour)
    if area > 100:  # Filtro para eliminar contornos pequeños
        # Clasificar los contornos en categorías
        # Aquí necesitarás implementar un método para identificar y clasificar los contornos
        # Puedes utilizar técnicas como la comparación de áreas, la forma de los contornos, etc.
        # Dependiendo de tu imagen y la complejidad de los contornos, este proceso puede ser más o menos complejo

        # Ejemplo de cómo podrías clasificar los contornos:
        if area > umbral_botones:
            botones.append(contour)
        elif area > umbral_campos_texto:
            campos_texto.append(contour)
        else:
            imagenes.append(contour)

print(f"Botones: {len(botones)}")
print(f"Campos de texto: {len(campos_texto)}")
print(f"Imágenes: {len(imagenes)}")

# Mostrar la imagen con los contornos detectados
cv2.imshow('Contornos', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Generar el diseño en Figma
# Aquí necesitarás implementar la lógica para crear los marcos y organizar los componentes en Figma
# Puedes utilizar la API de Figma para interactuar con tu diseño en Figma desde Python, si es necesario

# Estilizar y refinar el diseño en Figma

# Exportar el diseño en Figma
