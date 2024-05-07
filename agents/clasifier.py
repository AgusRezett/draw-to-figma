

from instantneo.core import InstantNeo
import openai


api_key = "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"
model = "gpt-3.5"


role_organizer = """Asume el papel de un """


# Instanciar actores
organizador = InstantNeo(api_key, model, role_organizer, 0.45, 700)

# Instrucciones
organizer_init_instruction = """Clasificar los contornos detectados en categorías de botones, campos de texto e imágenes."""

# Pasos
organizer_res = organizador.run(organizer_init_instruction)