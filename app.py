import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_student_model.pkl")

st.title("Student Pass Prediction")
st.write("Enter student learning information to get a prediction.")

hours = st.number_input("Hours studied", min_value=0.0, value=5.0)
attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=85)
practice = st.number_input("Practice tests", min_value=0, value=4)
sleep = st.number_input("Sleep hours", min_value=0.0, max_value=24.0, value=7.0)
method = st.selectbox("Study method", ["video", "group", "self"])

if st.button("Predict"):
    student = pd.DataFrame([{
        "hours_studied": hours,
        "attendance": attendance,
        "practice_tests": practice,
        "sleep_hours": sleep,
        "study_method": method
    }])

    prediction = model.predict(student)[0]

    if prediction == 1:
        st.success("Prediction: PASS")
    else:
        st.warning("Prediction: FAIL")

st.caption("Educational demonstration using synthetic data only. Do not use for real student decisions.")
