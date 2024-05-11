import cv2
import numpy as np
import pytesseract
from pytesseract import Output

def extract_features_and_text(image, contours):
    features = []
    texts = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        roi = image[y:y+h, x:x+w]
        text = pytesseract.image_to_string(roi, config='--psm 6')
        features.append([w, h, w/h])  # Ancho, alto, relación de aspecto
        texts.append(text.strip())
    return features, texts

def extract_text_from_contours(image_path, contours_path):
    image = cv2.imread(image_path)

    contours = ... 
    with open(contours_path, "r") as file:
        contours = file.readlines()
        contours = [np.array(eval(contour)) for contour in contours]

    text_data = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        roi = image[y:y+h, x:x+w]  # Extraer la región de interés basada en el contorno
        text = pytesseract.image_to_string(roi, config='--psm 6')
        text_data.append({'contour': contour, 'text': text.strip(), 'coordinates': (x, y, w, h)})
    return text_data

def load_and_preprocess_image(image_path):
    """Carga y preprocesa una imagen para detectar contornos."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    aislated_contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dilatar para unir contornos cercanos
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=3)
    
    # Encontrar contornos en la imagen dilatada
    components_contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return aislated_contours, components_contours



def contours_to_text(contours):
    """Convierte contornos en texto para ser procesado por InstantNeo."""
    contours_text = "\n".join([str(contour.tolist()) for contour in contours])
    return contours_text
