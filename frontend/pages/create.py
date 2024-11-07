import streamlit as st
from datetime import datetime
import requests

st.set_page_config(
    page_title="Create QR Code",
    page_icon=":rocket:"
)

def submit(url: str) -> dict:
    response = requests.post("http://localhost:8000/qrcode", json={"url": url, "creation_date": datetime.now().isoformat()})
    return response.json()

st.title('Create QR Code')

with st.form("form"):
    url = st.text_input("Enter the URL")
    submit_button = st.form_submit_button("Generate QR Code")
    
if submit_button:
    if (url == ""):
        st.error("URL cannot be empty!")
        st.stop()
    else:
        try:
            response = submit(url)
            if response["status"] == "success":
                st.text("QR Code generated successfully! Scan the QR Code below:")
                st.image(response['data']['path'])
                st.markdown(f"URL: {response['data']['url']}")
            else:
                st.error("Failed to generate QR Code!")
        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the QR Code generation server. Please try again later.")