
import streamlit as st
import pandas as pd
import pickle

with open('log_regression3.pkl', 'rb') as file:
   log_regression = pickle.load(file)

st.markdown("""
<style>
body {
    background-color: #f0f2f6;
    color: #333333;
    font-family: 'Arial', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.markdown("Author: Jason Harris")
st.markdown("""Programming 2 Final project \n Georgetown MSBA SAXA cohort""")

st.title('Logistic regression model for linkedin users')
st.image("business_handshake.png", caption="This is a sample image", width=300)
with st.form('user_input'):
    
    
    income_input = st.number_input(label = 'Enter your income', value = 0, format = "%d")
    if income_input <10000:
       income = 1.0
    elif income_input >10000 & income_input <20000:
       income = 2.0
    elif income_input > 20000 & income_input <30000:
       income = 3.0
    elif income_input > 30000 & income_input <40000:
       income = 4.0
    elif income_input > 40000 & income_input <50000:
       income = 5.0
    elif income_input > 50000 & income_input <75000:
       income = 6.0
    elif income_input > 75000 & income_input <100000:
       income = 7.0
    elif income_input > 100000 & income_input <150000:
       income = 8.0
    else:
       income = 9.0
   
    education_input = st.selectbox('Enter your education level',
                                   ('1: Less than high school (Grades 1-8 or no formal schooling)',
                                   '2: High school incomplete (Grades 9-11 or Grade 12 with NO diploma)',
                                   '3: High school graduate (Grade 12 with diploma or GED certificate)',
                                   '4: Some college, no degree (includes some community college)',
                                   '5: Two-year associate degree from a college or university',
                                   '6: Four-year college or university degree/Bachelor’s degree (e.g., BS, BA, AB)',
                                   '7: Some postgraduate or professional schooling, no postgraduate degree (e.g. some graduate school)',
                                   '8: Postgraduate or professional degree, including master’s, doctorate, medical or law degree (e.g., MA, MS, PhD, MD, JD)'))
    
    if education_input == '1: Less than high school (Grades 1-8 or no formal schooling)':
       education = 1.0
    elif education_input == '2: High school incomplete (Grades 9-11 or Grade 12 with NO diploma)':
       education = 2.0
    elif education_input == '3: High school graduate (Grade 12 with diploma or GED certificate)':
       education = 3.0
    elif education_input == '4: Some college, no degree (includes some community college)':
       education = 4.0
    elif education_input == '5: Two-year associate degree from a college or university':
       education = 5.0
    elif education_input == '6: Four-year college or university degree/Bachelor’s degree (e.g., BS, BA, AB)':
       education = 6.0
    elif education_input == '7: Some postgraduate or professional schooling, no postgraduate degree (e.g. some graduate school)':
       education = 7.0
    else:
       education = 8.0
       
    parent_input = st.selectbox('Are you a parent',('YES', 'NO'))
    if parent_input == 'YES':
       parent = 1
    else:
       parent = 0

    married_input = st.selectbox('Are you married', ('YES', 'NO'))
    if married_input == 'YES':
       married = 1
    else:
       married = 0

    gender_input = st.selectbox('What is your gender?',('MALE','FEMALE'))
    if gender_input == 'FEMALE':
       gender_female = 1
    else:
       gender_female = 0

    age = st.number_input('Enter your age',
                          min_value = 0, max_value = 99,
                          help="Please enter your age in years. Use whole numbers only with a max age of 99")
    
    button = st.form_submit_button()

if button:
   st.write('Button clicked')
   df_pred = pd.DataFrame({
        'income': income,
        'education': education,
        'parent': parent,
        'married': married,
        'gender_female': gender_female,
        'age': age}, index = ['user'])
   prediction = log_regression.predict(df_pred)[0]
   probability = log_regression.predict_proba(df_pred)[0,1]
   if prediction == 1: 
      text = f' You are a linkedin user, {round(probability * 100)}%'
   else:
      text = f' You are not a linkedin user, {round(probability*100)}%'
   #text = f' You are this kind of user {prediction}'

   st.write(text)


