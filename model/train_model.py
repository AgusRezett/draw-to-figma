from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint
import os

# Ruta al archivo de pesos descargados
local_weights_file = os.path.abspath('model/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5')

# Verificar si el archivo de pesos existe
if not os.path.exists(local_weights_file):
    raise FileNotFoundError(f"No se pudo encontrar el archivo de pesos en la ruta: {local_weights_file}")

# Definir el modelo sin pesos
base_model = MobileNetV2(weights=None, include_top=False, input_shape=(224, 224, 3))

# Cargar los pesos manualmente
base_model.load_weights(local_weights_file)

# Congelar las capas del modelo base
for layer in base_model.layers:
    layer.trainable = False

# Agregar capas adicionales
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
# Asegúrate de que el número de neuronas en la capa de salida coincida con el número de clases
predictions = Dense(12, activation='softmax')(x)  # Cambia 10 a 12

# Definir el modelo completo
model = Model(inputs=base_model.input, outputs=predictions)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Preparar los datos con aumentación
data_gen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,  # Utiliza el 20% de los datos para la validación
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Ruta a tu carpeta de datos
data_dir = 'model/data'

# Generador de datos de entrenamiento
train_generator = data_gen.flow_from_directory(
    data_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='training'  # Especificar que es el subconjunto de entrenamiento
)

# Generador de datos de validación
validation_generator = data_gen.flow_from_directory(
    data_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='validation'  # Especificar que es el subconjunto de validación
)

# Entrenar el modelo con un callback para guardar el mejor modelo
checkpoint = ModelCheckpoint('modelo_entrenado.keras', monitor='val_loss', save_best_only=True, mode='min')
model.fit(train_generator, epochs=10, validation_data=validation_generator, callbacks=[checkpoint])