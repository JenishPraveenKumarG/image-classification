# image-classification    
        simple image classification script using a pre-trained MobileNetV2 model to identify and classify objects 

**Steps Involved**

**1. Import Libraries:**

        Import necessary libraries and tools for deep learning, including TensorFlow, Keras, and MobileNetV2.

**2. Load Pre-Trained Model:**

        Load a pre-trained deep learning model called MobileNetV2, which can recognize objects in images.

**3. Define a Classification Function:**

        Create a function called `classify_image`. This function takes the path to an image as input.

**4. Image Processing:**

        Inside the function, load the image and prepare it for classification. Resize the image to a size that the model expects (224x224 pixels). Convert the image into a format that the model can understand.

**5. Use the Pre-Trained Model:**

        Pass the pre-processed image through the MobileNetV2 model to make predictions.

**6. Decode and Display Predictions:**

        Decode the model's predictions to get human-readable labels and confidence scores. Display the top 5 predictions with their labels and scores.

**7. Example Usage:**

        Provide the path to an image ('city.png') as an example. Call the `classify_image` function with this image.
