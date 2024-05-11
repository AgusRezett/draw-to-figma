from instantneo.core import InstantNeo
import json

def classify_contours(api_key, model, role_description, contours):
    contours_list = [contour.tolist() for contour in contours]
    contours_json = json.dumps(contours_list)

    print(contours_json)
    """Clasifica los contornos usando InstantNeo."""
    classifier = InstantNeo(api_key, model, role_description, 0.5, 700)
    classification_results = classifier.run(contours_json)
    return classification_results
