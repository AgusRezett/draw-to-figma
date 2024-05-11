import re
from src.image_processing import load_and_preprocess_image, contours_to_text, extract_features_and_text
from src.instantneo_integration import classify_contours
from src.figma_integration import create_figma_frame, get_figma_file_structure
import os
from dotenv import load_dotenv
load_dotenv()
from agents.classifier_role import classifier_description
from src.files_management import save_contours, load_contours

instantneo_api_key = os.getenv("INSTANTNEO_API_KEY")
instantneo_model = os.getenv("INSTANTNEO_MODEL")
figma_token = os.getenv("FIGMA_TOKEN")
file_id = os.getenv("FILE_ID")

def parse_classification_results(results):
    print("Classification Results:", results)
    """Parsea el string de resultados para extraer la cantidad de cada componente."""
    pattern = r"-\s*(Text|Input|Button):\s*(\d+)"
    matches = re.findall(pattern, results)
    return {match[0]: int(match[1]) for match in matches}

def main(image_path, api_key, model, figma_token, file_id):
    if image_path is None:
        raise ValueError("No se pudo cargar la imagen. Verifica la ruta del archivo.")

    aislated_contours, components_contours = load_and_preprocess_image(image_path)

    # Extraer características y texto de los contornos
    # contours_text = contours_to_text(contours)

    # Guardar contornos en un archivo de texto para pruebas
    save_contours(components_contours)

    """
    text_data = extract_text_from_contours(image_path, "contours.txt")
    # Procesar y almacenar metadatos
    for data in text_data:
        print(f"Contorno en {data['coordinates']} con texto: {data['text']}")
    """

    classification_results = classify_contours(api_key, model, classifier_description, load_contours())
    
    # Parsear los resultados de clasificación
    parsed_results = parse_classification_results(classification_results)
    print("Parsed Classification Results:", parsed_results)
    
    file_structure = get_figma_file_structure(figma_token, file_id)
    document_id = file_structure['document']['id']
    
    # Asumir una posición y tamaño estándar para el ejemplo
    position = {'x': 100, 'y': 100}
    size = {'width': 100, 'height': 50}

    # Crear frames para cada tipo de componente detectado
    for component_type, count in parsed_results.items():
        for _ in range(count):
            create_figma_frame(figma_token, file_id, document_id, component_type, position, size)
            # Ajustar la posición para el siguiente componente del mismo tipo
            position['y'] += 60  # Aumentar en 60 la posición y para no solapar componentes

if __name__ == "__main__":
    main("data/boceto.jpg", instantneo_api_key, instantneo_model, figma_token, file_id)
