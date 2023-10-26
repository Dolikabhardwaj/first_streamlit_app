import Streamlit
Streamlit.title('My Parents Little Healthy Dinner')

Streamlit.header('Breakfast Menu')
Streamlit.text('🥣Omega 3 and Blueberry oatmeal')
Streamlit.text(' 🥗 kale,Spinach and Smoothie')
Streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
Streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas as pd
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
