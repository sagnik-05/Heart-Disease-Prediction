import numpy as np
import pickle
import streamlit as st
from streamlit_lottie import st_lottie
import requests

loaded_model = pickle.load(open(r'C:\Users\sagnik panda\Desktop\Heart-Disease-Prediction\heart_disease_model.sav', 'rb'))

def heart_disease_prediction(input_data):
    input_np_array = np.asarray(input_data)
    reshaped_data = input_np_array.reshape(1,-1)
    prediction = loaded_model.predict(reshaped_data)
    
    if prediction[0] == 0:
        return 'Congratulations! You do not have heart disease'
    else:
        return 'You may have heart disease. Please consult with a doctor immediately!'

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    st.set_page_config(
        page_title="Healthy Heart App",
        page_icon="❤️",
        layout="wide",
    )

    # Custom CSS
    st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #ff4b4b;
        border-radius: 5px;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #ff7171;
    }
    .stSelectbox {
        color: #333333;
    }
    .stNumberInput {
        color: #333333;
    }
    h1 {
        color: #ff4b4b;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    h2 {
        color: #333333;
        font-size: 24px;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Page title and description
    st.title("Check Your Heart ❤️")
    st.markdown("This app predicts the likelihood of heart disease based on your health information.")

    # Load and display Lottie animation
    lottie_heart = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_kbfzivr8.json")
    st_lottie(lottie_heart, height=300, key="heart_animation")

    st.header("Please provide the following information:")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input('Enter your name', placeholder="John Doe")
        age = st.number_input('Age', min_value=1, max_value=100, value=25)
        sex = st.selectbox('Sex', ['Male', 'Female'])
        cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
        trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=300, value=120)
        chol = st.number_input('Cholesterol Level', min_value=0, max_value=600, value=200)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['True', 'False'])

    with col2:
        restecg_mapping = {'Normal': 0, 'Abnormal': 1, 'Other': 2}
        restecg = st.selectbox('Resting ECG Results', list(restecg_mapping.keys()))
        restecg = restecg_mapping[restecg]
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=300, value=150)
        exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=0.0, format="%.1f")
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
        ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', ['0', '1', '2', '3', '4'])
        thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    # Convert user inputs
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

    if st.button('Get Heart Disease Prediction'):
        diagnosis = heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
        st.subheader('Diagnosis:')
        if diagnosis.startswith('Congratulations'):
            st.success(diagnosis)
        else:
            st.error(diagnosis)

        st.markdown("---")
        st.write("Remember, this is just a prediction. Always consult with a healthcare professional for accurate medical advice.")

if __name__ == '__main__':
    main()