import re
import os
from dotenv import load_dotenv
from src.files_management import load_contours
from src.instantneo_integration import classify_contours
from src.figma_integration import create_figma_frame, get_figma_file_structure

load_dotenv()

figma_token = os.getenv("FIGMA_TOKEN")
file_id = os.getenv("FILE_ID")

def parse_classification_results(results):
    print("Classification Results:", results)
    """Parsea el string de resultados para extraer la cantidad de cada componente."""
    pattern = r"-\s*(Text|Input|Button):\s*(\d+)"
    matches = re.findall(pattern, results)
    return {match[0]: int(match[1]) for match in matches}

def detect_components():
    classification_results = classify_contours(load_contours())
    
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
