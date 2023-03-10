# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 12:16:03 2023

@author: My Acer
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle



# Loading the trained model
pickle_in = open(r"C:\Users\My Acer\Downloads\classifier2.pkl", 'rb') 
classifier = pickle.load(pickle_in)



html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Customer Churn Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True)


st.sidebar.header('User Input Parameters')

def user_input_features():
    account_length = st.sidebar.number_input('Insert how long the account has been active')
    voice_plan = st.sidebar.selectbox("Dose the customer have voicemail plan service",('1','0'))
    voice_messages = st.sidebar.number_input("Insert number of voicemail messages")
    intl_plan = st.sidebar.selectbox("Does the customer have intrnational plan service",('1','0'))
    intl_calls = st.sidebar.number_input("Insert number of international calls")
    intl_charge = st.sidebar.number_input("Insert charges of international calls")
    day_calls = st.sidebar.number_input("Insert number of calls during day time")
    day_charge = st.sidebar.number_input("Insert charges of calls during day time")
    eve_calls = st.sidebar.number_input("Insert number of calls during evening time")
    eve_charge = st.sidebar.number_input("Insert charges of calls during eveining time")
    night_calls = st.sidebar.number_input("Insert number of calls during night time")
    night_charge = st.sidebar.number_input("Insert charges of calls during night time")
    customer_calls = st.sidebar.number_input("Insert number of calls to customer service")
    Total_Calls = st.sidebar.number_input("Insert total number of calls")
    Total_Mins = st.sidebar.number_input("Insert total number of calling minutes")
    Total_Charge = st.sidebar.number_input("Insert total charges of calling")
    data = {'account_length' : account_length,
            'voice_plan' : voice_plan,
            'voice_messages' : voice_messages,
            'intl_plan' : intl_plan,
            'intl_calls' : intl_calls, 
            'intl_charge' : intl_charge,
            'day_calls' : day_calls,
            'day_Charge' : day_charge,
            'eve_calls' : eve_calls,
            'eve_charge' :eve_charge,
            'night_calls' : night_calls,
            'night_charge' : night_charge,
            'customer_calls' : customer_calls,
            'Total_Calls' : Total_Calls,
            'Total_Mins' : Total_Mins, 
            'Total_Charge' : Total_Charge}
    features = pd.DataFrame(data,index=[0])
    
    prediction = classifier.predict(
        [[account_length, voice_plan, voice_messages, intl_plan, intl_calls, intl_charge, day_calls, day_charge, eve_calls, eve_charge, night_calls, night_charge, customer_calls, Total_Calls, Total_Mins, Total_Charge ]])
    
    
    if st.button('Predict'):
           if prediction == 1:
               st.warning('Yes, the customer will terminate the service.')
           else:
               st.success('The customer is happy with Services.')
    
    return features 


df = user_input_features()
st.write(df)    
    
    
    
    
    










        
