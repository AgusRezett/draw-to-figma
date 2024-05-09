

from instantneo.core import InstantNeo
import openai
import pickle

api_key = "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"
model = "gpt-3.5-turbo"

# Contornos
contours = ...
with open('data/contours.txt', 'r') as archivo:
    contours = archivo.read()

components = [
    'Text',
    'Input',
    'Button'
]

role_classifier = f"""
Clasificar los contornos que se encuentran delimitados por ###, siendo estos conjuntos de vectores que construyen componentes web , como alguno de estos grupos: ${components}.

Lista de contornos:
###
${contours}
###

Reglas:
1) Los contornos son vectores ubicados en el espacio que construyen componentes web.
2) Los contornos puden, o no, ser agrupados para formar componentes web coherentes más complejos.
3) Deberás clasificar los contornos en uno de los grupos mencionados.
4) Si no estás seguro de la clasificación, deberás decidir entre los grupos 'Otros' o 'No clasificado'.
5) Solo deberás devolver la cantidad de componentes clasificados en cada grupo.
6) Los componentes clasificados como texto tienen que ser devueltos con el texto identificado.
"""

# Instanciar actores
classifier = InstantNeo(api_key, model, role_classifier, 0.5, 700)

# Pasos
classifier_res = classifier.run(contours)
print(classifier_res)



