import os
from dotenv import load_dotenv
from src.image_processing import load_and_preprocess_image
from src.files_management import save_contours

load_dotenv()

def preprocess_image(image_path):
    if not os.path.exists(image_path) or image_path is None:
        raise FileNotFoundError("🟢 No se encontró la imagen. Verifica la ruta del archivo.")

    aislated_contours, components_contours = load_and_preprocess_image(image_path)

    # Extraer características y texto de los contornos
    # contours_text = contours_to_text(contours)

    

    # Guardar contornos en un archivo de texto para pruebas
    save_contours(components_contours)

    return aislated_contours, components_contours
