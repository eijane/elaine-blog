from PIL import Image
import requests
#import streamlit as st


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.set_page_config(
    page_title="Multipage App",
    page_icon="wave"
)

st.title("Lalay's Blog")

import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20cfjwiyb.json")
img_contact_form = Image.open("images/1.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.subheader("Hi, I am Elaine Jane  T. Ilola :bear:")
    st.subheader("I'm the dependable listener who always brings a fresh perspective and supportive presence to your life's journey")
    
    st.subheader("This is my socials feel free to visit them.")
    st.write(" ▶ Facebook: https://www.facebook.com/profile.php?id=100070630448652")
    st.write(" ▶ Instagram: lalay287")
    st.write(" ▶Email: elaineilola41@gmail.com")
    st.write(" ▶Contact Number: 09814295294")
