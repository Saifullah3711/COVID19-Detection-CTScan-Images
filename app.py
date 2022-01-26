from ctypes import resize
import cv2
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image


model = tf.keras.models.load_model("COVID19-Model.h5")
### load file
uploaded_file = st.file_uploader("Choose a image file", type="png")

map_dict = {0: 'Not Infected with COVID-19',
            1: 'Infected With COVID-19',
            }

if uploaded_file is not None:
    # Convert the file read to the bytes array.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    # Converting the byte array into opencv image. 0 for grayscale and 1 for bgr
    opencv_image = cv2.imdecode(file_bytes, 0) 
    # Resizing the image to (128, 128) -> The model is trained for 128x128 grayscale images
    resized = cv2.resize(opencv_image,(128,128))

    #st.image(opencv_image, channels="RGB")

    img_tensor = image.img_to_array(resized)    # (height, width, channels)
    
    # add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0) # (1, height, width, channels), 
    img_tensor /= 255.  # Scaling the image between 0 and 1
    st.image(resized, channels="RGB")



    Genrate_pred = st.button("Generate Prediction")    
    if Genrate_pred:
        prediction = model.predict(img_tensor).argmax()
        st.title("Result:-> {}".format(map_dict [prediction]))
