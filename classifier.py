

from instantneo.core import InstantNeo
import openai
import pickle

api_key = "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"
model = "gpt-3.5-turbo"

# Contornos de prueba
contours_test = ...
with open('data/training/form.txt', 'r') as file:
    form = file.read()

# Contornos identificados
contours = ...
with open('data/contours.txt', 'r') as file:
    contours = file.read()

components = [
    'Text',
    'Input',
    'Button'
]

role_classifier = f"""
Clasificar los contornos que se encuentran delimitados por ###, siendo estos conjuntos de vectores que construyen componentes web , como alguno de estos grupos: ${components}.

Lista de contornos ejemplares con la descripción de su contenido: ${contours_test}.
El resultado correcto de este ejemplo es:
- Text: 1
- Input: 2
- Button: 1

Siendo el texto: "login"
El primer input: "correo"
El segundo input: "contraseña"
El botón: "enviar"

Lista de contornos a clasificar:
###
${contours}
###

Reglas:
1) Los contornos son vectores ubicados en el espacio que construyen componentes web.
2) Los contornos puden, o no, ser agrupados para formar componentes web coherentes más complejos.
3) Deberás clasificar los contornos en uno de los grupos mencionados.
5) Solo deberás devolver la cantidad de componentes clasificados en cada grupo.
7) Los contornos pueden ser letras del alfabeto latino, números o símbolos.
8) Deberás determinar por la cercanía de los contornos y sus vectores en el espacio si estos pertenecen a una palabra o a un número.
"""

# Instanciar actores
classifier = InstantNeo(api_key, model, role_classifier, 0.5, 700)

# Pasos
classifier_res = classifier.run(contours)
print(classifier_res)



