import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Brian Joseph Lesko')

st.info('Robotics Engineer with an interest in AI, Data Science, and Real Estate')

icon_size = 20

#st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
#st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
st_button('twitter', 'https://twitter.com/BrianJosephLeko', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/brianlesko/', 'Follow me on LinkedIn', icon_size)
st_button('github', 'https://github.com/BrianLesko', 'Follow me on Github', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/brianlesko', 'Buy me a Coffee', icon_size)
