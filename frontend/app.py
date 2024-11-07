import streamlit as st

def main():
    # TODO: Find a reason why sidebars in streamlit aren't aligning properly
    
    with st.sidebar:
        st.page_link('pages/find.py', label='Find QR Code', icon='🔍')
        st.page_link('pages/create.py', label='Create QR Code', icon='🚀')
        
    st.title('QR Code Generator')
    
    st.markdown('This is a "simple" QR code generator app using FastAPI and Streamlit.')
    st.markdown('[Github](https://github.com/raphaelkenji/qrcode-app)')
    
if __name__ == '__main__':
    main()