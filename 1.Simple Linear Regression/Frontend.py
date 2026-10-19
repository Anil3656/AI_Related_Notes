#Import required packages
import numpy as np 
import pickle 
import streamlit as st 

#Load the saved model 
model = pickle.load(open(r'C:\Users\aneel.kumar\OneDrive - IMCS Group\Desktop\Aneel\Naresh_IT\1.Simple Linear Regression\linear_regression_model.pkl', 'rb'))

#Assign the title to App
st.title('Salary Prediction App')

#Write the description
st.write('This app predicts the salary based on years of experience using simple linear regression.')

#Add input widget for user to enter the years of experience
years_of_experience = st.number_input('Enter years of experience:', min_value=0.0, max_value=100.0)

#When this button was clicked, make predictions appear
if st.button('Predict Salary'):
    #Make predictions using trained model   
    experience_input = np.array([[years_of_experience]])
    #Convert the input to 2D array for prediction
    prediction = model.predict(experience_input)
    
    #Displayed the prediction result
    st.success(f'The predicted salary for {years_of_experience} years of experience is ${prediction[0]:,.2f}.')
#Display the model training information
st.write('The model was trained using a dataset of salaries and years of experience.')