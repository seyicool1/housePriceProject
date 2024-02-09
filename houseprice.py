import pandas as pd
import seaborn as sns
# import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import warnings
import streamlit as st
import joblib
warnings.filterwarnings('ignore')

# import data
data = pd.read_csv('USA_Housing.csv')

model = joblib.load('usahousing.pkl')
st.markdown("<h1 style = 'color: #EEEFF3; text-align: center; font-family: helvetica '>HOUSE PREDICTION</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #EEEFF3; text-align: center; font-family: cursive '>Built By SEYI OLORUNHUNDO </h4>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)

st.image('pngwing.com.png')

st.markdown("<p style = 'text-align: justify;font-family: Arial black'>The predictive house price modeling project aims to leverage machine learning techniques to develop an accurate and robust model capable of predicting the market value of residential properties. By analyzing historical data, identifying key features influencing house prices, and employing advanced regression algorithms, the project seeks to provide valuable insights for homebuyers, sellers, and real estate professionals. The primary objective of this project is to create a reliable machine learning model that accurately predicts house prices based on relevant features such as location, size, number of bedrooms, amenities, and other influencing factors. The model should be versatile enough to adapt to different real estate markets, providing meaningful predictions for a wide range of properties.", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html= True)

st.sidebar.image("hseuser.png", 'Welcome User')

st.markdown("<br>", unsafe_allow_html= True)
st.dataframe(data, use_container_width=True)


input_choice = st.sidebar.radio('choose your input type', ['slider input', 'number input'])

if input_choice == 'slider input':
    area_income = st.sidebar.slider('Average Area Income', data['Avg. Area Income'].min(),data['Avg. Area Income'].max())
    house_age =st.sidebar.slider('Average House Age', data['Avg. Area House Age'].min(),data['Avg. Area House Age'].max())
    room_num = st.sidebar.slider('Average Number Of Rooms', data['Avg. Area Number of Rooms'].min(),data['Avg. Area Number of Rooms'].max())
    bedrooms = st.sidebar.slider('Number Of Bedrooms', data['Avg. Area Number of Bedrooms'].min(),data['Avg. Area Number of Bedrooms'].max())
    population = st.sidebar.slider('Area Population', data['Area Population'].min(),data['Area Population'].max())
else:
    area_income = st.sidebar.number_input('Average Area Income', data['Avg. Area Income'].min(),data['Avg. Area Income'].max())
    house_age =st.sidebar.number_input('Average House Age', data['Avg. Area House Age'].min(),data['Avg. Area House Age'].max())
    room_num = st.sidebar.number_input('Average Number Of Rooms', data['Avg. Area Number of Rooms'].min(),data['Avg. Area Number of Rooms'].max())
    bedrooms = st.sidebar.number_input('Number Of Bedrooms', data['Avg. Area Number of Bedrooms'].min(),data['Avg. Area Number of Bedrooms'].max())
    population = st.sidebar.number_input('Area Population', data['Area Population'].min(),data['Area Population'].max())


input_vars = pd.DataFrame({'Avg. Area Income': [area_income],
                           'Avg. Area House Age': [house_age],
                           'Avg. Area Number of Rooms': [room_num],
                           'Avg. Area Number of Bedrooms': [bedrooms],
                           'Area Population': [population]
                            })


st.markdown("<hr ", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<h5 style = 'margin: -30px; color: olive; font-family: helvetica '>User Input Variables</h5>", unsafe_allow_html = True)
st.dataframe(input_vars)
    



