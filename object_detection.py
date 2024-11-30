import cv2
import numpy as np
from PIL import Image

# Load YOLO model
def load_yolo_model():
    """Load the pre-trained YOLO model and configuration."""
    net = cv2.dnn.readNet("assets/yolov3.weights", "assets/yolov3.cfg")
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    return net, output_layers


# Get the class labels from coco.names
def load_labels():
    """Load class labels from the coco.names file."""
    with open("assets/coco.names", "r") as f:
        labels = [line.strip() for line in f.readlines()]
    return labels

# Perform object detection using YOLO
def detect_objects(image_file):
    """
    Perform object detection on an image using YOLOv3.

    Args:
        image_file: The file path or file-like object of the image.

    Returns:
        str: The file path of the image with detected objects.
    """
    # Load YOLO model and labels
    net, output_layers = load_yolo_model()
    labels = load_labels()

    # Open the image using PIL and convert it to a numpy array
    image = Image.open(image_file)
    image_np = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 

    # Get the height and width of the image
    height, width, channels = image_np.shape

    # Prepare the image for YOLO input
    blob = cv2.dnn.blobFromImage(image_np, 0.00392, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Post-process the detections
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:] 
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)


    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    colors = np.random.uniform(0, 255, size=(len(labels), 3))  # Random colors for each class
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = f"{labels[class_ids[i]]} ({confidences[i]:.2f})"
            color = [int(c) for c in colors[class_ids[i]]]
            image_np = cv2.rectangle(image_np, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image_np, label, (x, y - 10), font, 0.7, color, 2)

    # Save the result image
    output_path = "assets/detected_image.jpg"
    cv2.imwrite(output_path, image_np)

    return output_path
