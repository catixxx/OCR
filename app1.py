import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# 💫 Configuración general
st.set_page_config(
    page_title="✨ Reconocimiento Óptico de Caracteres",
    page_icon="🌈",
    layout="wide"
)

# 🌈 Fondo degradado estilo arcoíris + tipografía femenina
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee, #b9fbc0);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
    font-family: "Comic Sans MS", "Poppins", cursive;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
h1 {
    color: #7a42f4;
    text-align: center;
    font-weight: bold;
}
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #ffd1ff, #ffe6f7, #e0c3fc);
    border-radius: 15px;
    padding: 20px;
}
.stButton > button {
    background: linear-gradient(90deg, #a1c4fd, #c2e9fb);
    color: #333;
    border: none;
    border-radius: 30px;
    font-size: 18px;
    font-weight: bold;
    padding: 10px 30px;
    transition: all 0.3s ease;
}


