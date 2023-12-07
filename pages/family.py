from PIL import Image
import requests

import streamlit as st

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.title("My Umma")

    # --- LOAD ASSETS ---
img_contact_form = Image.open("images/8.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("She is Lina Ilola")
    st.write("She is my mother and I love her")
    st.write("My umma is a significant figure in my life,somebody who has likely assumed a critical part in molding who I am today.")
    st.write("Umma are frequently viewed as guardians,nurturers,tutors,and wellsprings of geniune love and backing.")
    st.write("They contribute immensely to their child development and advancement,offering direction,care,and intelligence alonf life's excursion.")

st.title("My Appa")

img_contact_form = Image.open("images/2.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("He is Jesus Ilola")
    st.write("He is my father")
    st.write("My appa is a one-of-a kind combination of events,characteristics,and influences that have created his personality.")
    st.write("He occupies a vital place in my life,providing advice,support,and love.")
    st.write("He has most certainly made a lasting impression on my life,whether via shared moments of joy,lessons learned, or silent support during difficult time.")
    st.write("Regardless of the circumstance, he is someone whose influence lives on in your thoughts, deeds, and memories, contributing to who I am today.")

st.title("My Oppa")

img_contact_form = Image.open("images/3.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("He's my Oldest brother")
    st.write("My oppa who is very close to me because he's sweet sometimes and we are always together at home,he also helps me with my educational needs such as daily school expenses.")

st.title("My Hyeong")

img_contact_form = Image.open("images/13.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("He is my Older brother")
    st.write("This my hyeong who works in cebu  city and he also has a family.")
    st.write("We are not that close because we are not always together and he has family that he should pay attention to.")
    st.write("We only talk via chat or call and he also helps in my studies, like an allowance.")

st.title("MY FAMILY")

img_contact_form = Image.open("images/14.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

img_contact_form = Image.open("images/13.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("This is my family")
    st.write("Family is the heartbet of my existence, the constellation of individuals whose  presense shapes and colors the canvas of my life.")
    st.write("They're the unwritten chapters of my story,the constants in a world of variables,providing a mosaic of love,support,and shared  history.")
    st.write("It's the source of enduring connections that transcend time and distance ,an unbreakable bond that weaves together our joy,sorrows, triumphs,and challenges,creating a rich tapesty of shared memories and experiences.")
