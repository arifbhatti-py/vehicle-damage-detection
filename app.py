import streamlit as st
from PIL import Image
import os
from model_helper import predict

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload", type=["jpg", "png"])

if uploaded_file is not None:
    image_path = "temp_file.jpg"
    
    uploaded_file.seek(0)
    image = Image.open(uploaded_file).convert("RGB")
    
    st.image(image, caption="Uploaded File", use_column_width=True)
    
    image.save(image_path)
    
    prediction = predict(image_path)
    st.info(f"Predicted Class: {prediction}")
    
    if os.path.exists(image_path):
        os.remove(image_path)
