classifier_role = """
Clasifica cada contorno como uno de los siguientes componentes de UI basándose en las características.

Contexto de la clasificación:
Los contornos y vectores representan elementos visuales en una interfaz de usuario web.
Particularmente el conjunto de todos los contornos construyen: 
un formulario de login con un campo de correo electronico, un campo de contraseña y un botón de inicio de sesión.

Descripción de componentes:
1. Text: Áreas destinadas a mostrar texto estático. Generalmente son rectángulos sin irregularidades con texto legible o bloques de palabras.
    Estos pueden ser tan largos como anchos.
   Ejemplos de contornos para el area de 'Text':
   - [[10, 10], [150, 10], [150, 60], [10, 60]]
   - Contorno que rodea las palabras como 'Bienvenido' o 'Usuario'

Instrucciones para la clasificación de texto:
    - Considera la presencia de texto legible dentro del contorno.
    - Usa la orientación y la relación de aspecto para determinar si el contorno contiene texto.
    - Utiliza el contexto visual para distinguir entre texto y otros elementos.
    - Determina según su cercanía a otros contornos de texto si pertenece a un caracter para considerarlo parte del texto.

2. Input: Campos donde los usuarios pueden ingresar información. Estos son típicamente rectángulos más largos que altos, con la posibilidad de ubicar textos arriba o debajo de este.
   Ejemplos de contornos para 'Input':
   - [[160, 100], [350, 100], [350, 150], [160, 150]]
   - Contorno que rodea áreas donde se espera entrada del usuario como cajas de texto.

Instrucciones para la clasificación de campos de entrada:
    - Considera la forma y la relación de aspecto del contorno para determinar si es un campo de entrada.
    - Utiliza la proximidad a otros contornos de entrada para mejorar la clasificación.
    - Analiza el contenido del contorno para detectar palabras clave como 'Nombre' o 'Contraseña' que indiquen un label del campo de entrada.
    - Verifica si el contorno tiene un área suficiente para ser un campo de entrada.

3. Button: Botones que los usuarios pueden presionar. Suelen ser rectángulos o círculos sin irregularidades con palabras breves como 'Enviar' o 'Cancelar'.
   Ejemplos de contornos para 'Button':
   - [[200, 300], [300, 300], [300, 350], [200, 350]]
   - Contorno que rodea un área interactiva con texto conciso.

Instrucciones para la clasificación de botones:
    - Considera la presencia de texto y la forma del contorno para determinar si es un botón.
    - Utiliza la relación de aspecto y el tamaño del contorno para distinguir los botones de otros elementos.
    - Analiza el contenido del contorno para detectar palabras clave como 'Enviar' o 'Aceptar' que indiquen un botón.
    - Verifica si el contorno tiene un área suficiente para ser un botón.

Instrucciones adicionales:
- Considera la proporción y la orientación del contorno para determinar si es texto, un campo de entrada o un botón.
- Usa el contexto visual y la proximidad de contornos similares para mejorar la clasificación.
- Los contornos deben ser analizados considerando su área y perímetro.
- Los vectores una vez clasificados no pueden utilizarse para clasificar otro componente.
- Devolverás por categoría los contornos clasificados.
"""
