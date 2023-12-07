from PIL import Image
import requests

import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.title("Umma")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/8.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.subheader("She is LIna Ilola")
    st.write("She is my mother and I love her")
    st.write("My umma is a significant figure in my life,somebody who has likely assumed a critical part in molding who I am today.")
    st.write("Umma are frequently viewed as guardians,nurturers,tutors,and wellsprings of geniune love and backing.")
    st.write("They contribute immensely to their child development and advancement,offering direction,care,and intelligence alonf life's excursion.")

st.title("Appa")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/2.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.subheader("He is Jesus Ilola")
    st.write("He is my father")
    st.write("My appa is a one-of-a kind combination of events,characteristics,and influences that have created his personality.")
    st.write("He occupies a vital place in my life,providing advice,support,and love.")
    st.write("He has most certainly made a lasting impression on my life,whether via shared moments of joy,lessons learned, or silent support during difficult time.")
    st.write("Regardless of the circumstance, he is someone whose influence lives on in your thoughts, deeds, and memories, contributing to who I am today.")

st.title("Oppa")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/3.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.subheader("He's my Oldest brother")
    st.write("My oppa who is very close to me because he's sweet sometimes and we are always together at home,he also helps me with my educational needs such as daily school expenses.")


st.title("Hyeong")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/13.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.subheader("He is my Older brother")
    st.write("This my hyeong who works in cebu  city and he also has a family.")
    st.write("We are not that close because we are not always together and he has family that he should pay attention to.")
    st.write("We only talk via chat or call and he also helps in my studies, like an allowance.")

st.title("THIS IS MY FAMILY")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/14.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

   # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/13.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)


with st.container():
    st.subheader("She's my youngest sister")
    st.write("She was born on August 7,2023")
    st.write("I love her so much much much")
    
    
    









    
