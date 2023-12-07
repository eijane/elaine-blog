from PIL import Image
import requests

import streamlit as st

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.title("MY HOBBIES")


    # --- LOAD ASSETS ---
img_contact_form = Image.open("images/9.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("I LOVE DANCING")
    st.write("The dance to me is good because it is one to relieve my stress.")
    st.write("Dancing is also help to exercise to me.")
    
  # --- LOAD ASSETS ---
img_contact_form = Image.open("images/17.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

 # --- LOAD ASSETS ---
img_contact_form = Image.open("images/18.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

     # --- LOAD ASSETS ---
img_contact_form = Image.open("images/19.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("I LOVE TABLE TENNIS/PINGPONG")
    st.write("One of the sports i love is Table Tennis because it can relieve my stress too.")
    st.write("Thanks God because he gave me such wonderful skills, that would  be beneficial to me.")
    
