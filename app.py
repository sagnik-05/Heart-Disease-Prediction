# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 11:29:43 2023

@author: sagnik panda
"""
import numpy as np
import pickle
import streamlit as st

# loading the saved model 
loaded_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# function for prediction system

def heart_disease_prediction(input_data):
    # age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target
    #input_data = (57,0,0,120,354,0,1,163,1,0.6,2,0,2)
    #input_data = (63,0,0,108,269,0,1,169,1,1.8,1,2,2)

    # change the input into np array
    input_np_array = np.asarray(input_data)
    # reshape the np array as we are predicting for only one data point
    reshaped_data = input_np_array.reshape(1,-1)

    prediction = loaded_model.predict(reshaped_data)
    print(prediction)

    if(prediction[0] == 0):
        return 'The person does not have heart disease'
    else:
        return 'The person has heart disease'
    
    
def main():
    
    st.set_page_config(
    page_title="Healthy Heart App",
    page_icon="❤️‍🩹",
    layout="wide",
    )
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
        background-color:#5B6467;
        background-size: 100%;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;
    }
    </style>
    """
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    # giving a title
    st.write("<h1><span style='color:#ffff;' font-family='Agdasima,Agdasima;'> Check Your Heart 🩺</span></h1>", unsafe_allow_html=True)
    st.markdown("---")
    # getting data from user
    st.write('Please provide the following information:')
   
    
    
    col1, col2 = st.columns(2)
        
    with col1:
            age = st.number_input('Age', min_value=1, max_value=100, value=25)
            sex = st.selectbox('Sex', ['Male', 'Female'])
            cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
            trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=300, value=120)
            chol = st.number_input('Cholesterol Level', min_value=0, max_value=600, value=200)
            fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['True', 'False'])
            restecg_mapping = {'Normal': 0, 'Abnormal': 1, 'Other': 2}
            restecg = st.selectbox('Resting ECG Results', list(restecg_mapping.keys()))
            restecg = restecg_mapping[restecg]
        
    with col2:
            
            thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=300, value=150)
            exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
            oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=0.0)
            slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
            ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', ['0', '1', '2', '3', '4'])
            thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])
    
    # Convert the user inputs to the input format expected by the model
    sex = 0 if sex == 'Male' else 1
    cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
    cp = cp_mapping[cp]
    fbs = 1 if fbs == 'True' else 0
    exang = 1 if exang == 'Yes' else 0
    slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
    slope = slope_mapping[slope]
    ca = int(ca)
    thal_mapping = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}
    thal = thal_mapping[thal]
    
    st.markdown("---")
    # code for prediction
    diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
    st.markdown("---")
    if diagnosis:
        st.subheader('Diagnosis:')
        if diagnosis.startswith('The person does not have heart disease'):
            st.success(diagnosis)
        else:
            st.error(diagnosis)
            

if __name__ == '__main__':
    main()
    
    
    
    
    
