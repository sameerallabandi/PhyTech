from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import tensorflow as tf
from matplotlib import pyplot as plt
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class_names = ['Aloe Vera','Areca Palm','Money Plant','Peace Lily','Philodendron','Rubber Plant','Snake Plant','Spider Plant','Tulsi','ZZ Plant']

@app.post("/upload-image")
async def upload_image(image: bytes = File(...)):
    try:
        contents = io.BytesIO(image)

        new_model = load_model(os.path.join('/home/sameera_rallabandi/plant_classification_m2'))
        new_image = tf.keras.preprocessing.image.load_img(contents, target_size=(224, 224))

        # Preprocess the image
        new_image_array = tf.keras.preprocessing.image.img_to_array(new_image)
        new_image_array = np.expand_dims(new_image_array, axis=0)
	
	#define class name
	#class_names = ['Aloe Vera','Areca Palm','Money Plant','Peace Lily','Philodendron','Rubber Plant','Snake Plant','Spider Plant','Tulsi','ZZ Plant']
	

        prediction = new_model.predict(new_image_array)
        predicted_label = int(np.argmax(prediction, axis=1)[0])
        predicted_class_name = class_names[predicted_label]

        # Return the predicted label as a JSON object
        return {"predicted_class_name": predicted_class_name}

    except Exception as e:
        # Return an error message if an exception occurs
        return {"error": str(e)}

@app.get("/ping")
async def ping():
    return {"message": "pong"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1234)
