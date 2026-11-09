import streamlit as st
import os
import base64
from model_helper import predict

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload", type=["jpg", "png"])

if uploaded_file is not None:
    image_path = "temp_file.jpg"
    image_bytes = uploaded_file.getvalue()
    
    with open(image_path, "wb") as f:
        f.write(image_bytes)
        
    base64_image = base64.b64encode(image_bytes).decode('utf-8')
    mime_type = "image/png" if uploaded_file.name.lower().endswith(".png") else "image/jpeg"
    
    html_img = f'<img src="data:{mime_type};base64,{base64_image}" style="width:100%; border-radius: 10px;">'
    st.markdown(html_img, unsafe_allow_html=True)
    st.caption("Uploaded File")
    
    prediction = predict(image_path)
    st.info(f"Predicted Class: {prediction}")
    
    if os.path.exists(image_path):
        os.remove(image_path)
