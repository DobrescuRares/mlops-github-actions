import os

import numpy as np
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ANIMALS = ["Cat", "Dog", "Panda"]

model_path = os.getenv("MODEL_PATH", "/app/model.keras")
model = tf.keras.models.load_model(model_path)


@app.post("/upload/image")
async def upload_image(img: UploadFile = File(...)):
    original_image = Image.open(img.file).convert("RGB")
    resized_image = original_image.resize((64, 64))
    images_to_predict = np.expand_dims(np.array(resized_image), axis=0)
    predictions = model.predict(images_to_predict)
    classifications = predictions.argmax(axis=1)
    return ANIMALS[classifications.tolist()[0]]