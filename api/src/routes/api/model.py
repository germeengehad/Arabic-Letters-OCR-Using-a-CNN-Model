from typing import Any, List
from fastapi import APIRouter, Body , Depends, HTTPException
from fastapi.encoders import jsonable_encoder
import schemas
from schemas.input import ImageInput
from pydantic import BaseModel
#----------------------------
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image_dataset_from_directory ,image
import keras
from PIL import Image
import pandas as pd
import seaborn
import os
from tensorflow.keras.layers import Dropout
import pickle
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras import layers, models
import shutil
from fastapi import FastAPI
import base64
from PIL import Image
from io import BytesIO
from keras.preprocessing import image
from keras.models import load_model
import pickle
#-------------------------------------------
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
import base64
from PIL import Image
import numpy as np
from io import BytesIO
import pickle

router = APIRouter(
    prefix="/CNN_model",
    tags=["CNN_model"]
)


def preprocess_image(base64_image):
    decoded_image = base64.b64decode(base64_image)
    img = Image.open(BytesIO(decoded_image))
    if img.size != (32, 32):
        img = img.resize((32, 32))
    img_array = np.array(img)
    if len(img_array.shape) == 2:
        img_array = np.stack((img_array,) * 3, axis=-1)
    img_array = img_array / 255.0
    return img_array

def get_class_name(predicted_class):
    class_names = {
        0: 'ا', 1: 'ب', 2: 'ت', 3: 'ث', 4: 'ج', 5: 'ح', 6: 'خ', 7: 'د', 8: 'ذ', 9: 'ر',
        10: 'ز', 11: 'س', 12: 'ش', 13: 'ص', 14: 'ض', 15: 'ط', 16: 'ظ', 17: 'ع', 18: 'غ',
        19: 'ف', 20: 'ق', 21: 'ك', 22: 'ل', 23: 'لا', 24: 'م', 25: 'ن', 26: 'ه', 27: 'و', 28: 'ي'
    }
    return class_names.get(predicted_class, 'Unknown')

def load_trained_model():
    # Load the saved model
    model_path = "./static/Arabic_letters_model.h5"
    model = load_model(model_path)
    return model

def predict_letter(image_data, model):
    predictions = model.predict(np.expand_dims(image_data, axis=0))
    predicted_class_index = np.argmax(predictions)
    detected_letter = get_class_name(predicted_class_index)
    probability = float(predictions[0][predicted_class_index])
    return {"detected_letter": detected_letter, "probability": probability}

@router.post("/predict")
async def predict(base64_image: str = Body(...)):
    try:
        image_data = preprocess_image(base64_image)
        model = load_trained_model()
        prediction_result = predict_letter(image_data, model)
        return prediction_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))