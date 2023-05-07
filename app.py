import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import sklearn

loaded_model = pickle.load(open('C:/Users/ramsa/Downloads/Diabeties prediction/trained_model.sav','rb'))




st.title('Diabeties prediction in women')
st.sidebar.title('Enter the mentioned observations below ')
pregnancy=st.sidebar.number_input('Enter number of pregnancies')
glucose=st.sidebar.number_input('Enter Glucose Level')
bp=st.sidebar.number_input('Enter Blood Pressure')
insulin=st.sidebar.number_input('Enter Insulin Level')
bmi=st.sidebar.number_input('Enter BMI')
dpf=st.sidebar.number_input('Enter Diabetes Pedigree Function')
age=st.sidebar.number_input('Enter Age')


input=(pregnancy,glucose,bp,insulin,bmi,dpf,age)
input_data_as_numpy_array=np.asarray(input)
input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)

if st.sidebar.button('submit'):
    if prediction==[[0]]:
        st.subheader('The woman is not Diabetic')
        st.markdown('Precautions  to reduce the risk of developing diabetes:')
        st.write("1.Maintain a healthy weight: Excess body weight, especially around the waist, increases the risk of developing diabetes. Maintaining a healthy weight through a balanced diet and regular physical activity can help reduce this risk.")
        st.write("2.Follow a healthy diet: A healthy diet rich in whole grains, fruits, vegetables, lean protein, and healthy fats can help reduce the risk of developing diabetes. Avoiding processed foods, sugary drinks, and excessive amounts of saturated and trans fats can also help.")
        st.write("3.Exercise regularly: Regular physical activity can help reduce the risk of developing diabetes by improving insulin sensitivity, helping with weight management, and reducing inflammation. Aim for at least 150 minutes of moderate-intensity activity per week.")
        st.write("4.Avoid smoking: Smoking is a risk factor for many chronic diseases, including diabetes. Quitting smoking or avoiding smoking altogether can help reduce the risk of developing diabetes.")
        st.write("5.Manage stress: Chronic stress can contribute to the development of diabetes. Managing stress through relaxation techniques such as deep breathing, meditation, or yoga can help reduce this risk.")
        st.write("6.Get regular checkups: Regular checkups with a healthcare provider can help identify risk factors for diabetes and provide guidance on preventive measures.")
        st.write("Remember, prevention is key when it comes to diabetes. By making healthy lifestyle choices, women can reduce their risk of developing this chronic condition and improve their overall health and well-being.")
        

    else:
        st.subheader('The women is Diabetic')
        st.markdown('Take Cares')
        st.write('1.Follow a healthy eating plan: A healthy eating plan can help manage blood sugar levels, control weight, and reduce the risk of heart disease. A registered dietitian can help create a personalized eating plan.')
        st.write('2.Exercise regularly: Exercise can help control blood sugar levels, improve heart health, and help with weight management. Aim for at least 30 minutes of moderate-intensity activity most days of the week.')
        st.write('3.Monitor blood sugar levels: Regular monitoring of blood sugar levels can help identify patterns and adjust treatment accordingly.')
        st.write("4.Take medication as prescribed: Medication can help control blood sugar levels and prevent complications. It's important to take medication as prescribed by a healthcare provider.")
        st.write("5.Manage stress: Stress can affect blood sugar levels. Relaxation techniques such as deep breathing, yoga, or meditation can help manage stress.")
        st.write("6.Maintain good foot health: Diabetic women are at risk for foot problems. Inspect feet regularly, wear comfortable shoes, and report any foot problems to a healthcare provider.")
        st.write("7.Get regular checkups: Regular checkups with a healthcare provider can help monitor blood sugar levels, blood pressure, and cholesterol levels, and identify any potential complications early.")
        st.write("Remember, managing diabetes is a lifelong commitment. It's important to work closely with a healthcare provider to develop a personalized diabetes management plan.")




