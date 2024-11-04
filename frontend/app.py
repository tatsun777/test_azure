# frontend/app.py
import streamlit as st
import requests

st.title("FastAPI と Streamlit のアプリケーション")
response = requests.get("http://backend:8000/")
if response.status_code == 200:
    st.write(response.json())
else:
    st.write("FastAPIからの応答がありません")
