import streamlit as st
from PIL import Image
import io
import os
from model_helper import predict

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload", type=["jpg", "png"])

if uploaded_file is not None:
    image_path = "temp_file.jpg"
    
    image_bytes = uploaded_file.getvalue()
    with open(image_path, "wb") as f:
        f.write(image_bytes)
    
    display_image = Image.open(io.BytesIO(image_bytes))
    st.image(display_image, caption="Uploaded File", use_container_width=True)
    
    prediction = predict(image_path)
    st.info(f"Predicted Class: {prediction}")
    
    if os.path.exists(image_path):
        os.remove(image_path)
