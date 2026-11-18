import os
from tensorflow import keras

model_path = os.path.join("animal-classification", "INPUT_model_path", "animal-cnn", "model.keras")
model = keras.models.load_model(model_path)

model.save("unpacked_keras", zipped=False)