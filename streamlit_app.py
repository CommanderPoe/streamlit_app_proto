import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('Dinner Chicken Dinner')

streamlit.header('Mornning Menu')
streamlit.text('🍳 Eggs with potato and bread')
streamlit.text('🥗 Tomatoes, tonno and mozarella')
streamlit.text('🍞 Bread with butten and ham')

streamlit.header('Smoothies, make your own 🥝')

streamlit.dataframe(my_fruit_list)
