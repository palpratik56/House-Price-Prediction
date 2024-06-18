import pickle
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

regmodel=pickle.load(open('best_model.pkl','rb'))

# Load the dataset
path = 'C:/Users/PRATIK PAL/Desktop\Self Study\ML\datasets\Housing.csv'
df = pd.read_csv(path)

##taking input
st.header('Welcome to Boston House Price Prediction Web App')
a = st.number_input('Area')
be = st.number_input('Bedrooms', min_value=1, step=1)
ba = st.number_input('Bathrooms', min_value=1, step=1)
sto = st.number_input('Storeys',min_value=1, step=1)
mr = st.selectbox('Mainrioad', options=df.mainroad.unique())
gu = st.selectbox('Guestroom', options=df.guestroom.unique())
bs = st.selectbox('Basement', options=df.basement.unique())
hw = st.selectbox('Hot water', options=df.hotwaterheating.unique())
ac = st.selectbox('AC', options=df.airconditioning.unique())
prk = st.number_input('Parking', min_value=0, step=1)
pfa = st.selectbox('Prefered area', options=df.prefarea.unique())
fs = st.selectbox('Furnishing status', options=df.furnishingstatus.unique())

# area	bedrooms	bathrooms	stories	mainroad	guestroom	basement	hotwaterheating	airconditioning	parking	prefarea	furnishingstatus
input = pd.DataFrame(dict(
  area = [a], bedrooms = [be], bathrooms = [ba], stories = [sto], mainroad = [mr], 
  guestroom = [gu], basement = [bs], hotwaterheating= [hw], airconditioning = [ac], 
  parking = [prk], prefarea = [pfa], furnishingstatus = [fs]
  ))

categorical_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus']
le = LabelEncoder()

#load the model to process the given input on pressing predict
if st.button('Predict'):
    # Encode categorical variables
    for column in categorical_columns:
      input[column] = le.fit_transform(input[column])
    input_pre = StandardScaler().fit_transform(input)
    pred = regmodel.predict(input_pre)[0]

    st.info(f'The predicted price is {pred:.0f}$')
   
    