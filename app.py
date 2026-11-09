import streamlit as st
import os
from model_helper import predict

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_path = "temp_file.jpg"
    
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    st.image(image_path, caption="Uploaded File", use_container_width=True)
    
    prediction = predict(image_path)
    st.info(f"Predicted Class: {prediction}")
    
    if os.path.exists(image_path):
        os.remove(image_path)
