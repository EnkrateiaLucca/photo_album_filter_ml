import streamlit as st
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from PIL import Image
import numpy as np
from model import predict
import time
import cv2 as cv

labels = ['dont_keep_it', "keep_it"]

'''
# Album Photo Sorter ML App
'''
img_file_buffer = st.file_uploader("Upload an image")
if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    imageLocation = st.empty()
    image = np.array(image) 
    image = cv.resize(image, (700,666), interpolation=cv.INTER_AREA)
    imageLocation.image(image, caption="Album Photo", use_column_width=True)
    print("Classifying...")
    classification_Location = st.empty()
    classification_Location.write("Classifying....")
    imageLocation.image(image)
    prediction = predict(image)
    predicted_label = labels[prediction]
    st.write("Prediction raw:", prediction)
    st.write("Prediction: ", predicted_label)


    