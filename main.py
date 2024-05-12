from processes.sketch_process_init import preprocess_image
from processes.detection_process_init import detect_components

class SketchToDesignOrchestrator:
    def __init__(self, image_path):
        self.image_path = image_path
        self.components = []
        self.texts = []
        self.design = None

    def process_image(self):
        # Preprocessing
        preprocess_image(self.image_path)
        
        # Detect components
        self.components = detect_components()

        print("Components:", self.components)
        """ 
        # Recognize text within components
        self.texts = recognize_text(self.components)
        
        # Classify components
        classified_components = classify_components(self.components, self.texts)
        
        # Adapt components to HIG
        adapted_components = adapt_to_hig(classified_components)
        
        # Generate Figma design
        self.design = generate_figma_design(adapted_components)
        """
    def get_design(self):
        return self.design

# Usage
orchestrator = SketchToDesignOrchestrator("sketch.jpg")
orchestrator.process_image()
design = orchestrator.get_design()
