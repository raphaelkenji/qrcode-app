import streamlit as st
import requests

st.set_page_config(
    page_title="Find QR Code",
    page_icon=":mag:"
)

def submit(id: int) -> dict:
    response = requests.get(f"http://localhost:8000/qrcode/{id}")
    return response.json()

st.title('Find QR Code')

with st.form("form"):
    id = st.number_input("Enter the ID", min_value=1, step=1, format="%d")
    submit_button = st.form_submit_button("Find QR Code")
    
if submit_button:
    if (id == 0):
        st.error("ID cannot be empty!")
        st.stop()
    else:
        try:
            response = submit(id)
            if response["status"] == "success":
                st.text("QR Code found! Scan the QR Code below:")
                st.image(response['data']['path'])
                st.markdown(f"URL: {response['data']['url']}")
            else:
                st.error("Failed to find QR Code!")
        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the QR Code generation server. Please try again later.")