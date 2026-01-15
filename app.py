import streamlit as st
import pandas as pd

from utils.bmi import calculate_bmi
from utils.workout import generate_workout
from utils.diet import generate_diet
from utils.progress import save_progress, load_progress
from utils.calorie import calorie_estimation
from utils.wearable import fetch_wearable_data

st.set_page_config(page_title="AI Fitness Planner", layout="wide")

st.title("🏋️ Personalized Workout & Diet Planner with AI")

# ----- SIDEBAR INPUT -----
st.sidebar.header("User Profile")

age = st.sidebar.number_input("Age", 15, 60)
weight = st.sidebar.number_input("Weight (kg)")
height = st.sidebar.number_input("Height (cm)")
goal = st.sidebar.selectbox("Goal", ["Weight Loss", "Muscle Gain", "Stay Fit"])
diet = st.sidebar.selectbox("Diet", ["Vegetarian", "Non-Vegetarian"])

# ----- BMI -----
if height > 0 and weight > 0:
    bmi, status = calculate_bmi(weight, height)
    st.info(f"📊 **BMI:** {bmi} ({status})")
else:
    st.warning("Enter height and weight to calculate BMI")
weight = st.sidebar.number_input("Weight (kg)", min_value=30, value=60)
height = st.sidebar.number_input("Height (cm)", min_value=120, value=165)


# ----- AI CALORIES -----
calories = calorie_estimation(weight, height, age, goal)
st.success(f"🔥 Recommended Daily Calories: **{calories} kcal**")

# ----- GENERATE PLANS -----
if st.button("Generate Fitness Plan"):
    st.subheader("🏃 Workout Plan")
    st.text(generate_workout({"goal": goal}))

    st.subheader("🥗 Diet Plan")
    st.text(generate_diet({"diet": diet}))

# ----- PROGRESS TRACKING -----
st.subheader("📅 Weekly Progress Tracking")

if st.button("Save Today's Weight"):
    save_progress(weight)
    st.success("Progress saved successfully!")

progress = load_progress()
if progress:
    df = pd.DataFrame(progress)
    st.line_chart(df.set_index("date")["weight"])

# ----- WEARABLE DATA -----
st.subheader("⌚ Wearable Device Data (Live Simulation)")
wearable = fetch_wearable_data()

col1, col2, col3 = st.columns(3)
col1.metric("Steps", wearable["steps"])
col2.metric("Calories Burned", wearable["calories_burned"])
col3.metric("Heart Rate", wearable["heart_rate"])

