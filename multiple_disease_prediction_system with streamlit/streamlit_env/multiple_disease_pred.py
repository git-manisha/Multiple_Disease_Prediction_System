import pickle
import streamlit as st 
from streamlit_option_menu import option_menu

# loading the saved model

with open(r"C:\Users\manis\PycharmProjects\Multiple_Disease_Prediction\diabetes_model.sav", "rb") as file:
    diabetes_model = pickle.load(file)

with open(r"C:\Users\manis\PycharmProjects\Multiple_Disease_Prediction\heart_disease_model.sav", "rb") as file:
    heart_disease_model = pickle.load(file)

with open(r"C:\Users\manis\PycharmProjects\Multiple_Disease_Prediction\parkisons_disease_model.sav", "rb") as file:
    parkisons_model = pickle.load(file)

# sidebar for nevigation
with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkisons Prediction'],
                            icons= ['activity','heart','person'],
                            default_index=0)

# Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using ML')

    #getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    # code for Prediction
    diab_dignosis = ''

    # creating a button for prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if diab_prediction[0] == 1:
            diab_dignosis = 'The person is Diabetic'
        else:
            diab_dignosis = 'The person is not Diabetic'
    
    st.success(diab_dignosis)
    

# Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')
    with col2:
        Sex = st.text_input('Sex')
    with col3:
        Cp = st.text_input('Chest Pain Type')
    
    with col1:
        Trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        Chol = st.text_input('Serum Cholstoral in mg/dl')
    with col3:
        Fbs = st.text_input('Fasting Blood Sugar>120mg/dl')
    
    with col1:
        Restecg = st.text_input('Resting Electrocardiographic result')
    with col2:
        Thalach = st.text_input('Maximum Heart Rate achived')
    with col3:
        Exang = st.text_input('Exercise Induced Angina')
    
    with col1:
        Oldpeak = st.text_input('St depression induced by exercise')
    with col2:
        Slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        Ca = st.text_input('Major vessela colored by flourosopy')
    with col1:
        Thal = st.text_input('thal:0=normal;1=fixed defect;2=reversable defect')

        # code for Prediction
    heart_dignosis = ''

    # creating a button for prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[Age,Sex,Cp,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,Ca,Thal]])

        if heart_prediction[0] == 1:
            heart_dignosis = 'The person is Heart Disease'
        else:
            heart_dignosis = 'The person is not Heart Disease'
    
    st.success(heart_dignosis)

# Parkisons Prediction Page
if(selected == 'Parkisons Prediction'):
    #page title
    st.title('Parkisons Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    
    with col1:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        rap = st.text_input('MDVP:RAP')
    
    with col1:
        ppq = st.text_input('MDVP:PPQ')
    with col2:
        ddp = st.text_input('Jitter:DDP')
    with col3:
        shimmer = st.text_input('MDVP:Shimmer')
    
    with col1:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        apq3 = st.text_input('Shimmer:APQ3')
    with col3:
        apq5 = st.text_input('Shimmer:APQ5')
    
    with col1:
        apq = st.text_input('MDVP:APQ')
    with col2:
        dda = st.text_input('Shimmer:DDA')
    with col3:
        nhr = st.text_input('NHR')
    
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        d2 = st.text_input('D2')
    
    with col1:
        ppe = st.text_input('PPE')


    parkisons_dignosis = ''

    # creating a button for prediction

    if st.button("Parkison's Test Result"):
        parkisons_prediction = parkisons_model.predict([[fo,fhi,flo,jitter_percent,jitter_abs,rap,ppq,ddp,shimmer,shimmer_db,apq3,apq5,apq,dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]])

        if parkisons_prediction[0] == 1:
            parkisons_dignosis = "The person has Parkinson's disease"
        else:
            parkisons_dignosis = "The person does not have Parkinson's disease"
    
    st.success(parkisons_dignosis)