import streamlit as st
from PIL import Image
import io
import os
import base64
from model_helper import predict

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload", type=["jpg", "png"])

if uploaded_file is not None:
    image_path = "temp_file.jpg"
    
    image = Image.open(uploaded_file)
    
    image.thumbnail((800, 800)) 
    
    image.save(image_path, format="JPEG")
    
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    html_img = f'<img src="data:image/jpeg;base64,{img_str}" style="width:100%; border-radius: 10px;">'
    st.markdown(html_img, unsafe_allow_html=True)
    st.caption("Uploaded File")
    
    with st.spinner("Analyzing damage... Please wait."):
        prediction = predict(image_path)
        
    st.info(f"Predicted Class: {prediction}")
    
    if os.path.exists(image_path):
        os.remove(image_path)
