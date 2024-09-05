import numpy as np
import pickle
import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Heart Disease Prediction App",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# Custom CSS for both light and dark mode
st.markdown("""
    <style>
    :root {
        --background-color: #ffffff;
        --text-color: #333333;
        --button-color: #4a90e2;
        --button-hover-color: #357abd;
        --success-color: #28a745;
        --error-color: #dc3545;
        --warning-color: #ffc107;
        --secondary-bg: #f8f9fa;
    }

    [data-testid="stAppViewContainer"] {
        background-color: var(--background-color);
        color: var(--text-color);
    }

    .stButton>button {
        background-color: var(--button-color);
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: var(--button-hover-color);
    }

    .stTextInput>div>div>input {
        background-color: var(--secondary-bg);
    }

    .stSelectbox>div>div>div {
        background-color: var(--secondary-bg);
    }

    .stNumberInput>div>div>input {
        background-color: var(--secondary-bg);
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --background-color: #0e1117;
            --text-color: #f0f2f6;
            --button-color: #4a90e2;
            --button-hover-color: #357abd;
            --success-color: #28a745;
            --error-color: #dc3545;
            --warning-color: #ffc107;
            --secondary-bg: #262730;
        }
    }

    .pulse {
        animation: pulse 2s infinite;
        display: inline-block;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# (The rest of the Python code remains unchanged)

def main():
    current_time = datetime.now().strftime("%B %d, %Y")

    # App header
    st.title('Heart Disease Prediction Web App')
    st.markdown('---')

    # User input section
    st.subheader("Patient Information")
    col1, col2 = st.columns(2)
    
    # (User input code remains unchanged)

    # Prediction button
    if st.button('Get Heart Disease Test Result'):
        diagnosis = heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
        st.subheader('Diagnosis:')
        if diagnosis == "No heart disease detected":
            st.markdown(f'<p style="color: var(--success-color); font-weight: bold;">Dear {user_name}, no heart disease detected.</p>', unsafe_allow_html=True)
            st.balloons()
            st.markdown("### Stay healthy and take care! 💪😊👌")
        else:
            st.markdown(f'<p style="color: var(--error-color); font-weight: bold;">Dear {user_name}, heart disease detected.</p>', unsafe_allow_html=True)
            display_heart_disease_animation()
            st.markdown('<p style="color: var(--warning-color); font-weight: bold;">Please consult a cardiologist for proper evaluation and management. 🧑‍⚕️</p>', unsafe_allow_html=True)
        
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