from instantneo.core import InstantNeo
import json
from agents.classifier_role import classifier_role
import os
from dotenv import load_dotenv
load_dotenv()

instantneo_api_key = os.getenv("INSTANTNEO_API_KEY")
instantneo_model = os.getenv("INSTANTNEO_MODEL")

def classify_contours(contours):
    contours_list = [contour.tolist() for contour in contours]
    contours_json = json.dumps(contours_list)

    print(contours_json)
    """Clasifica los contornos usando InstantNeo."""
    classifier = InstantNeo(instantneo_api_key, instantneo_model, classifier_role)
    classification_results = classifier.run(contours_json)
    return classification_results
