import streamlit as st
from PIL import Image
from model_helper import predict

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded File", width="stretch")

    # Save the uploaded image temporarily for prediction
    image_path = "temp_file.jpg"
    image.save(image_path, format="JPEG")

    # Predict vehicle damage
    prediction = predict(image_path)

    st.info(f"Predicted Class: {prediction}")
