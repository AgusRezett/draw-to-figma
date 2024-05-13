import numpy as np
import json

def save_contours(contours):
    """Guarda los contornos en un archivo de texto."""
    with open("contours.txt", "w") as file:
        for contour in contours:
            file.write(str(contour.tolist()) + "\n")

def load_contours():
    """Carga los contornos desde un archivo de texto."""
    with open("contours.txt", "r") as file:
        contours = file.readlines()
        contours = [np.array(eval(contour)) for contour in contours
                    if len(eval(contour)) > 0
                    and len(eval(contour)[0]) > 0
        ]
    return contours

def load_json_as_string(file_path):
    """Carga los contornos desde un archivo de texto tipo json como string."""
    with open(file_path, "r") as file:
        contours = json.load(file)
    return contours
