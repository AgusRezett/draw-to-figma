import requests

def create_figma_frame(token, file_id, parent_id, name, position, size):
    """Crea un frame en Figma."""
    url = f"https://api.figma.com/v1/files/{file_id}/nodes"
    headers = {"X-Figma-Token": token}
    payload = {
        "name": name,
        "parent_id": parent_id,
        "type": "FRAME",
        "position": position,
        "size": size
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def get_figma_file_structure(token, file_id):
    """Obtiene la estructura de un archivo de Figma."""
    url = f"https://api.figma.com/v1/files/{file_id}"
    headers = {"X-Figma-Token": token}
    response = requests.get(url, headers=headers)
    return response.json()
