# -*- coding: utf-8 -*-
"""
Created on Sat May 29 04:51:00 2021
@author: MuhammadAli
"""

from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

#with st.echo(code_location='below'):
def predict_rating(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    
    return predictions_data['Label'][0]
    
model = load_model('diamond_random_forest_regressor')


st.title('Diamond Price Prediction Web App')
st.write('This is a web app to predict the price of the diamond based on\
        several features that you can see in the sidebar. Please adjust the\
        value of each feature. After that, click on the Predict button at the bottom to\
        see the prediction of the regressor.')

                        
#Carat Weight = st.sidebar.number_input(label = 'Carat Weight',
 #                       value = 2.0)
                        
Cut = st.sidebar.selectbox(
    "Cut",
    ('Ideal', 'Very Good', 'Fair', 'Good', 'Signature-Ideal')
)

Color = st.sidebar.selectbox(
    "Color",
    ('H', 'E', 'G', 'D', 'F', 'I')
)

Clarity = st.sidebar.selectbox(
    "Clarity",
    ('SI1', 'VS1', 'VS2', 'VVS2', 'VVS1', 'IF', 'FL')
)

Polish = st.sidebar.selectbox(
    "Polish",
    ('VG', 'ID', 'EX', 'G')
)

Symmetry = st.sidebar.selectbox(
    "Symmetry",
    ('EX', 'ID', 'VG', 'G')
)

Report = st.sidebar.selectbox(
    "Report",
    ('GIA', 'AGSL')
)


# 'Carat Weight':Carat Weight,
features = { 
            'Cut':Cut,
            'Color':Color,
'Clarity':Clarity,
'Polish':Polish,
'Symmetry':Symmetry,
'Report':Report}


features_df  = pd.DataFrame([features])

st.table(features_df)  

if st.button('Predict'):
    
    prediction = predict_rating(model, features_df)
    
    st.write(' Based on feature values, the car star rating is '+ str(int(prediction)))
    
