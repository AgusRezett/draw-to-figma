import cv2
import numpy as np

# Cargar YOLO
net = cv2.dnn.readNet("model/yolov3.weights", "model/yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Cargar las etiquetas de las clases (modifica según tus clases)
with open("model/coco.names", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

def detect_objects(image_path):
    # Cargar imagen
    image = cv2.imread(image_path)
    height, width, channels = image.shape

    # Crear un blob
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Mostrar información en la pantalla
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Ajusta el umbral de confianza según sea necesario
                # Objeto detectado
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Coordenadas del cuadro delimitador
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Aplicar supresión no máxima para eliminar cajas redundantes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    detected_components = []
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(class_names[class_ids[i]])
            confidence = confidences[i]
            color = (0, 255, 0)
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            detected_components.append({
                "label": label,
                "confidence": confidence,
                "box": (x, y, w, h)
            })

    print(f"Componentes detectados: {detected_components}")

    return detected_components