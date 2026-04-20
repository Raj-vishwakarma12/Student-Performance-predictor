import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model.pkl")

st.title(" Student Performance Predictor")

# Inputs
gender = st.selectbox("Gender", ["male", "female", "other"])
school_type = st.selectbox("School Type", ["public", "private"])
parent_education = st.selectbox("Parent Education",
["no formal", "high school", "diploma", "graduate", "post graduate", "phd"])

study_hours = st.slider("Study Hours", 0.0, 10.0, 5.0)
attendance = st.slider("Attendance %", 0.0, 100.0, 75.0)

internet = st.selectbox("Internet Access", ["yes", "no"])
travel_time = st.selectbox("Travel Time", ["<15 min", "15-30 min", "30-60 min", ">60 min"])
extra = st.selectbox("Extra Activities", ["yes", "no"])
study_method = st.selectbox("Study Method", ["notes", "textbook", "group study", "coaching", "online videos", "mixed"])

# Predict
if st.button("Predict"):
    input_data = pd.DataFrame([[
        gender, school_type, parent_education,
        study_hours, attendance,
        internet, travel_time, extra, study_method
    ]], columns=[
        'gender','school_type','parent_education','study_hours',
        'attendance_percentage','internet_access','travel_time',
        'extra_activities','study_method'
    ])

    prediction = model.predict(input_data)
    st.success(f"Predicted Score: {round(prediction[0], 2)}")
