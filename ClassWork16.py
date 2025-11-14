#executing a python program on a web page
#using streamlit
#if red line "pip install streamlit" on terminal

#st.title()
#st.header()
#st.divider()
#st.markdown()
#st.text()

import streamlit as st
from PIL import Image

# col1, col2 = st.columns((4,5))
#
# with col1:
st.title("My Resume")
st.header("Abigail Stucker")

# with col2:
image = Image.open('20230531_155405.jpg')
st.image(image, width=400)

st.divider()

st.markdown("**About Me**")
st.text("I am an academic, a mathematician, and a runner")
st.text("I am currently a student at JBU")

#Education
st.markdown("**Education:**")
st.text("I am currently studying mathematics and Spanish as a student at JBU")
#Work Experience
st.markdown("**Work Experience:**")
st.text("I have worked as a piano teacher, and volunteered tutoring elementary students in math and english.")
#projects
st.markdown("**Projects:**")
st.text("I have participated and won a all girls high school hackathon.")
#Hobbies
st.markdown("**Hobbies**")
st.text("I am currently participation in my schools cross country and track team")

st.markdown("**contact me:**")
st.text_input("Your Name: ")
st.text_input("Your email: ")
st.text_area("Please input the information or questions you have for me below.")
st.button("Send Message")

