import streamlit as st
from model_helper import predict
from PIL import Image

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload", type=["jpg", "png"])

if uploaded_file:
    image_bytes = uploaded_file.getvalue()
    
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(image_bytes)

    st.image(image_bytes, caption="Uploaded File", use_container_width=True)
    prediction = predict(image_path)
    st.info(f"Predicted Class: {prediction}")
