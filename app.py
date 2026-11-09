import streamlit as st
from PIL import Image
import os
from model_helper import predict

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload", type=["jpg", "png"])

if uploaded_file is not None:
    image_path = "temp_file.jpg"
    
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded File", use_container_width=True)
    
    image.save(image_path)
    
    prediction = predict(image_path)
    st.info(f"Predicted Class: {prediction}")
    
    if os.path.exists(image_path):
        os.remove(image_path)
