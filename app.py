import numpy as np
import pickle
import streamlit as st
from datetime import datetime

# Set page config to force light mode
st.set_page_config(
    page_title="Heart Disease Prediction App",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# Force light mode
st.markdown("""
    <style>
        .stApp {
            background-color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Loading the saved model
loaded_model = pickle.load(open('heart_disease_model.sav', 'rb'))

def heart_disease_prediction(input_data):
    input_np_array = np.asarray(input_data)
    reshaped_data = input_np_array.reshape(1,-1)
    prediction = loaded_model.predict(reshaped_data)
    
    return "No heart disease detected" if prediction[0] == 0 else "Heart disease detected"

def get_user_name():
    return st.text_input("Enter the Patient name")

def display_heart_disease_animation():
    st.markdown("""
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .pulse {
        animation: pulse 2s infinite;
        display: inline-block;
    }
    </style>
    <div style='text-align: center;'>
        <h2 class='pulse' style='color: #FF5733;'>⚠️ Heart Disease Detected ⚠️</h2>
    </div>
    """, unsafe_allow_html=True)

def main():
    current_time = datetime.now().strftime("%B %d, %Y")
    
    # Custom CSS
    st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF7171;
    }
    </style>
    """, unsafe_allow_html=True)

    # App header
    st.title('Heart Disease Prediction Web App')
    st.markdown('---')

    # User input section
    st.subheader("Patient Information")
    col1, col2 = st.columns(2)
    
    with col1:
        user_name = get_user_name()
        age = st.number_input('Age', min_value=1, max_value=100, value=25)
        sex = st.selectbox('Sex', ['Male', 'Female'])
        cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, max_value=300, value=120)
        chol = st.number_input('Cholesterol Level (mg/dl)', min_value=0, max_value=600, value=200)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['False', 'True'])
    
    with col2:
        restecg = st.selectbox('Resting ECG Results', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=300, value=150)
        exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=0.0, format="%.1f")
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
        ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', ['0', '1', '2', '3'])
        thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    st.markdown("---")

    # Convert user inputs
    sex = 1 if sex == 'Male' else 0
    cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
    cp = cp_mapping[cp]
    fbs = 1 if fbs == 'True' else 0
    restecg_mapping = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Left Ventricular Hypertrophy': 2}
    restecg = restecg_mapping[restecg]
    exang = 1 if exang == 'Yes' else 0
    slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
    slope = slope_mapping[slope]
    ca = int(ca)
    thal_mapping = {'Normal': 1, 'Fixed Defect': 2, 'Reversible Defect': 3}
    thal = thal_mapping[thal]

    # Prediction button
    if st.button('Get Heart Disease Test Result'):
        diagnosis = heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
        st.subheader('Diagnosis:')
        if diagnosis == "No heart disease detected":
            st.success(f"Dear {user_name}, no heart disease detected.")
            st.balloons()
            st.markdown("### Stay healthy and take care! 💪😊👌")
        else:
            st.error(f"Dear {user_name}, heart disease detected.")
            display_heart_disease_animation()
            st.warning("### Please consult a cardiologist for proper evaluation and management. 🧑‍⚕️")
        
        # Display health tips
        st.subheader("Heart Health Tips")
        tips = [
            "Maintain a heart-healthy diet rich in fruits, vegetables, whole grains, and lean proteins.",
            "Exercise regularly, aiming for at least 150 minutes of moderate-intensity activity per week.",
            "Manage stress through relaxation techniques like meditation or deep breathing exercises.",
            "Quit smoking and limit alcohol consumption.",
            "Monitor your blood pressure and cholesterol levels regularly."
        ]
        for tip in tips:
            st.markdown(f"- {tip}")

    # Footer
    st.markdown("---")
    st.markdown(f"Created by [Your Name] | Last updated: {current_time}")

if __name__ == '__main__':
    main()