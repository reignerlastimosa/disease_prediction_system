

import pickle
import streamlit as st
from streamlit_option_menu import option_menu




diabetes_model = pickle.load(open('./Saved models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('./Saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('./Saved models/parkinsons_model.sav','rb'))


st.markdown(
    """
    <style>
    .sidebar-content .widget-item-label {
        color: green;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    
    selected = option_menu('DocAI: Disease Prediction System',
                           ['Diabetes',
                            'Heart Disease',
                            'Parkinsons'],
                           icons = ['activity','heart','person'],
                           default_index = 0)

if selected == 'Diabetes':
    st.title('Diabetes Prediction')

    # Define input fields
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    # Check if all fields are filled before prediction
    if st.button('Diabetes Test Result'):
        if all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            # Convert input values to float for prediction
            inputs = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]

            # Make prediction
            diab_prediction = diabetes_model.predict([inputs])

            # Determine diagnosis based on prediction
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is Diabetic'
            else:
                diab_diagnosis = 'The person is Not Diabetic'
        else:
            st.error("Please fill in all required fields.")

    st.success(diab_diagnosis)

    
    
    
            

if(selected == 'Heart Disease'):
    
   
    st.title('Heart Disease Prediction')
    
    age = st.number_input('Age of the Person')
    sex = st.number_input('Sex of the Person')
    cp = st.number_input('Chest pain types')
    trestbps = st.number_input('Resting Blood Pressure')
    chol = st.number_input('Serum Cholestoral in mg/dl')
    fbs = st.number_input('Fasting blood sugar > 120 mg/dl')
    restecg = st.number_input('Resting Electrocardiographic results')
    thalach = st.number_input('Maximum Heart Rate achieved')
    exang = st.number_input('Exercise Induced Angina')
    oldpeak = st.number_input('ST depression induced by exercise')
    slope = st.number_input('Slope of the peak exercise ST segment')
    ca = st.number_input('Mjor vessels colored by flourosopy')
    thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    

    heart_diagnosis = ''
    

    
    if st.button('Heart Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The person is suffering from Heart disease'
            
        else:
            heart_diagnosis = 'The person is Not suffering from Heart disease'
            
            
    st.success(heart_diagnosis)
    

if(selected == 'Parkinsons'):
    st.title('Parkinsons Prediction')

    # Define input fields
    fo = st.text_input('MDVP:Fo(Hz)')
    fhi = st.text_input('MDVP:Fhi(Hz)')
    flo = st.text_input('MDVP:Flo(Hz)')
    Jitter_percent = st.text_input('MDVP:Jitter(%)')
    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    RAP = st.text_input('MDVP:RAP')
    PPQ = st.text_input('MDVP:PPQ')
    DDP = st.text_input('Jitter:DDP')
    Shimmer = st.text_input('MDVP:Shimmer')
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    APQ3 = st.text_input('Shimmer:APQ3')
    APQ5 = st.text_input('Shimmer:APQ5')
    APQ = st.text_input('MDVP:APQ')
    DDA = st.text_input('Shimmer:DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    
    # Check if all fields are filled before prediction
    if st.button('Parkinsons Test Result'):
        if all([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]):
            # Convert input values to float for prediction
            inputs = [float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB), float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]
            
            # Make prediction
            parkinsons_prediction = parkinsons_model.predict([inputs])
            
            # Determine diagnosis based on prediction
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = 'The person is suffering from Parkinsons disease'
            else:
                parkinsons_diagnosis = 'The person is Not suffering from Parkinsons disease'
        else:
            st.error("Please fill in all required fields.")
                
    st.success(parkinsons_diagnosis)

        
        