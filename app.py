import streamlit as st
import pandas as pd

st.write("""
# Multiplication App

This app performs multiplication of 2 given numbers
""")
#Get Input

st.header('User Input Parameters')


first_number = st.number_input("Enter the first number")
second_number = st.number_input("Enter the second number")


data = {"First number": first_number, "Second number": second_number}
data_df = pd.DataFrame(data, index=[0])

st.subheader('User Inputs')
st.write(data_df.to_dict())

answer = first_number * second_number

st.subheader('Result of the multiplication')
st.write(f"{first_number} x {second_number} = {answer}")

