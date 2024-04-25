import pandas as pd
import numpy as np
import pickle
import streamlit as st
import time


pkl = pickle.load(open('pipe.pkl','rb'))


with st.form("my_form", clear_on_submit=True):
    carat = st.number_input("Carat", value=0.0, step=0.01)
    
    cut_options = ['Ideal','Premium','Good','Very Good','Fair']
    cut = st.selectbox("Select cut of a diamond",options= cut_options)
    
    color_options = ['D','E','F','G','H','I','J']
    color = st.selectbox("Select a color option",options= color_options)
    
    clarity_options = ['IF','VVS1','VVS2','VS1','VS2','SI1','SI2','I1']
    clarity = st.selectbox("Select a clarity option",options= clarity_options)
 
    depth = st.number_input("Depth", value=0.0, step=0.5)
    table = st.number_input("Table", value=0.0, step=0.5)

    submitted = st.form_submit_button("Predict")

if submitted:
    test_input = np.array([[carat, cut, color, clarity, depth, table]]).reshape(1,6)

    test_input_df = pd.DataFrame(test_input.tolist(), columns=['carat','cut','color','clarity','depth','table'])

    result = pkl.predict(test_input_df)
        
    success_message = st.success(f"Predicted price: {np.floor(result[0])} USD")

