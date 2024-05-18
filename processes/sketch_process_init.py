import os
import cv2
import spacy
import numpy as np
from tensorflow.keras.models import load_model

# Cargar el modelo de spaCy
nlp = spacy.load("es_core_news_md")

# Cargar el modelo guardado
model = load_model('modelo_entrenado.keras')

def preprocess_image(image_path):
    if not os.path.exists(image_path) or image_path is None:
        raise FileNotFoundError("🟢 No se encontró la imagen. Verifica la ruta del archivo.")
    image = cv2.imread(image_path)    
    if image is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen en la ruta: {image_path}")
    
    # Redimensionar la imagen a 224x224 píxeles
    image = cv2.resize(image, (224, 224))
    # Normalizar la imagen para que los valores de los píxeles estén en el rango [0, 1]
    image = image / 255.0
    # Añadir una dimensión extra para el batch
    image = np.expand_dims(image, axis=0)
    
    return image

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return tokens

def predict_component(image):
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions, axis=1)[0]
    return predicted_class, predictions

class Dataset:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.data = []
        self._load_data()

    def _load_data(self):
        for filename in os.listdir(self.data_dir):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(self.data_dir, filename)
                text_path = os.path.join(self.data_dir, filename.rsplit('.', 1)[0] + ".txt")
                if os.path.exists(text_path):
                    with open(text_path, "r", encoding="utf-8") as file:
                        description = file.read()
                    image = preprocess_image(image_path)
                    tokens = preprocess_text(description)
                    self.data.append((image, tokens))
                else:
                    print(f"No se encontró una descripción para la imagen {filename}")

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

class PreprocessedData:
    def __init__(self, dataset):
        self.dataset = dataset
        self.images = []
        self.texts = []
        self._preprocess_all()

    def _preprocess_all(self):
        for image, tokens in self.dataset:
            self.images.append(image)
            self.texts.append(tokens)

    def get_images(self):
        return np.array(self.images)

    def get_texts(self):
        return self.texts
