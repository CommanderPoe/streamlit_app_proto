# importing libraries
import streamlit
import pandas

# reading csv in s3 bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# adding title and text for menu
streamlit.title('Dinner Chicken Dinner')

streamlit.header('Mornning Menu')
streamlit.text('🍳 Eggs with potato and bread')
streamlit.text('🥗 Tomatoes, tonno and mozarella')
streamlit.text('🍞 Bread with butten and ham')

streamlit.header('Smoothies, make your own 🥝')

# adding widget to select fruits
streamlit.multiselect('Pick your own:', list(my_fruit_list.index))

# list of selected fruits
fruits_selected = streamlit.multiselect('Pick your own:', list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

# printing dataframe
streamlit.dataframe(fruits_to_show)
