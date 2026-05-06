import streamlit as st
import requests

st.set_page_config(page_title="Student Result Prediction", layout="centered")

st.title("🎓 Student Result Prediction App")

# -------------------------
# Numeric Inputs
# -------------------------
age = st.slider("Age", 5, 100, 18)

study_hours = st.slider("Study Hours", 0.0, 24.0, 5.0)
attendance = st.slider("Attendance (%)", 0.0, 100.0, 75.0)
sleep_hours = st.slider("Sleep Hours", 0.0, 24.0, 7.0)

assignments_completed = st.number_input("Assignments Completed", min_value=0, step=1)
practice_tests_taken = st.number_input("Practice Tests Taken", min_value=0, step=1)
group_study_hours = st.slider("Group Study Hours", 0.0, 24.0, 2.0)

notes_quality_score = st.slider("Notes Quality Score", 0.0, 10.0, 5.0)
time_management_score = st.slider("Time Management Score", 0.0, 10.0, 5.0)
motivation_level = st.slider("Motivation Level", 0.0, 10.0, 5.0)
mental_health_score = st.slider("Mental Health Score", 0.0, 10.0, 5.0)

screen_time = st.slider("Screen Time", 0.0, 24.0, 4.0)
social_media_hours = st.slider("Social Media Hours", 0.0, 24.0, 3.0)

# -------------------------
# Categorical Inputs
# -------------------------
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

family_income = st.selectbox("Family Income", ["Low", "Medium", "High"])
parent_education = st.selectbox("Parent Education", ["High School", "Bachelor", "Master", "PhD"])
internet_access = st.selectbox("Internet Access", ["Yes", "No"])
device_type = st.selectbox("Device Type", ["Mobile", "Laptop", "Tablet"])
school_type = st.selectbox("School Type", ["Private", "Public"])
extracurriculars = st.selectbox(
    "Extracurricular Activities",
    ["Coding Club", "Music", "Debate", "Sports", "Arts"]
)

# -------------------------
# Submit Button
# -------------------------
if st.button("Predict Result"):
    
    data = {
        "age": age,
        "gender": gender,
        "study_hours": study_hours,
        "attendance": attendance,
        "sleep_hours": sleep_hours,
        "assignments_completed": assignments_completed,
        "practice_tests_taken": practice_tests_taken,
        "group_study_hours": group_study_hours,
        "notes_quality_score": notes_quality_score,
        "time_management_score": time_management_score,
        "motivation_level": motivation_level,
        "mental_health_score": mental_health_score,
        "screen_time": screen_time,
        "social_media_hours": social_media_hours,
        "family_income": family_income,
        "parent_education": parent_education,
        "internet_access": internet_access,
        "device_type": device_type,
        "school_type": school_type,
        "extracurriculars": extracurriculars
    }

    try:
        
        response = requests.post("https://student-result-prediction-api.onrender.com/predict", json=data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"📊 Predicted Result: {result}")
        else:
            st.error("❌ API Error")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")