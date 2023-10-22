# Import necessary libraries

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np

# Load a pre-trained model (MobileNetV2)

model = MobileNetV2(weights='imagenet')

# Define a function to classify an image
def classify_image(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Use the pre-trained model to classify the image
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=5)[0]

    # Display the top predictions
    for label, description, score in decoded_predictions:
        print(f"{description}: {score:.2f}")

# Example usage
image_path = 'plastic.jpg'
classify_image(image_path)
