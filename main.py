from processes.sketch_process_init import preprocess_image, preprocess_text, predict_component
from model.yolo_model import detect_objects

class SketchToDesignOrchestrator:
    def __init__(self, image_path):
        self.image_path = image_path
        self.components = []
        self.texts = []
        self.design = None

    def process_image(self):
        # Preprocessing
        processed_image = preprocess_image(self.image_path)
        print(f"Imagen preprocesada: {processed_image.shape}")

        description = "Este es un botón para enviar el formulario."
        processed_text = preprocess_text(description)
        print(f"Texto preprocesado: {processed_text}")

        # predicted_class, predictions = predict_component(processed_image)
        # print(f'Predicted class: {predicted_class}')
        # print(f'Predictions: {predictions}')

        detected_components = detect_objects(self.image_path)

        # Imprimir los componentes detectados
        for component in detected_components:
            print(f"Detected {component['label']} with confidence {component['confidence']} at {component['box']}")

# Usage
orchestrator = SketchToDesignOrchestrator("sketch.jpg")
orchestrator.process_image()
