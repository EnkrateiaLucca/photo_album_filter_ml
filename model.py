from tensorflow import keras
import numpy as np
import cv2 as cv


def predict(image):
    model = keras.models.load_model("./album_image_sorter_inception/")
    image = cv.resize(image, (150,150), interpolation=cv.INTER_AREA)
    print(image.shape)
    img = image.reshape(1,150, 150, 3)
    img = img / 255.0
    prediction = model.predict(img)
    
    if prediction>0.5:
        return 1
    else:
        return 0


