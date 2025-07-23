import streamlit as st
import numpy as np
import pandas as pd
import time
from sklearn.ensemble import RandomForestRegressor

# -------------- Page Config --------------
st.set_page_config(
    page_title="Fitness Tracker",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------- Sidebar ---------
with st.sidebar:
    st.title("🏃‍♂️ Fitness Tracker")
    st.markdown("Track your health goals, stay informed, and motivated.")
    st.markdown("---")

    st.subheader("✨ Features")
    st.markdown("""
    - 📈 Track Your Progress  
    - 🎯 Set Fitness Goals  
    - 🧠 Personalized Tips  
    - 📌 Smart Health Advice  
    """)
    st.markdown("---")

    st.subheader("📈 Progress Chart")
    progress_data = np.random.randint(100, 500, size=7)
    st.line_chart(progress_data)

    st.subheader("🎯 Calorie Goal")
    goal = st.number_input("Set Your Daily Goal (kcal)", 100, 1000, step=50, value=500)
    st.success(f"🎉 Daily Goal: **{goal} kcal**")

    st.subheader("💡 Tip of the Day")
    st.info(np.random.choice([
        "💧 Stay hydrated.",
        "🥗 Eat balanced meals.",
        "💤 Sleep 7–8 hours daily.",
        "🏃 Mix cardio and strength.",
        "🧘 Reduce stress daily."
    ]))

    st.subheader("📌 Health Advice")
    st.success(np.random.choice([
        "⚡ Start your day with stretches.",
        "🍽️ Eat small, frequent meals.",
        "🚶 Walk 10,000 steps daily.",
        "🏃 Gradually increase intensity.",
        "📉 Track your calories.",
        "🛌 Prioritize quality sleep.",
    ]))

# --------- Main Section ---------
st.title("🔥 Personal Fitness Dashboard")
st.markdown("Stay motivated with predictive insights and smarter fitness tracking.")

# --------- Input Section ---------
st.header("🏋️ Enter Your Daily Data")

col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input("Age", 1, 100, 25)
    bmi = st.slider("BMI", 10.0, 50.0, 22.0)
with col2:
    duration = st.slider("Workout Duration (min)", 10, 180, 45)
    heart_rate = st.slider("Heart Rate (BPM)", 50, 200, 110)
with col3:
    body_temp = st.slider("Body Temp (°C)", 30.0, 45.0, 37.0)
    gender = st.radio("Gender", ["Male", "Female"])
    gender_val = 1 if gender == "Male" else 0

# --------- Summary ---------
user_input = pd.DataFrame({
    "Age": [age],
    "BMI": [bmi],
    "Duration": [duration],
    "Heart Rate": [heart_rate],
    "Body Temp": [body_temp],
    "Gender": [gender_val]
})

st.subheader("📋 Summary of Your Input")
st.dataframe(user_input.style.set_properties(**{
    'background-color': '#111', 'color': '#FFF'
}))

# --------- Prediction Section ---------
st.header("🔥 Calories Burned (Predicted)")
st.info("Analyzing your data...")

progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)

# Dummy model (for demo)
X_train = np.random.rand(100, 5)
y_train = np.random.randint(100, 600, 100)
model = RandomForestRegressor()
model.fit(X_train, y_train)

prediction = model.predict(user_input.drop(columns=['Gender']))
st.success(f"🔥 Estimated Calories Burned: **{round(prediction[0], 2)} kcal**")

# --------- Footer ---------
st.markdown("---")
st.markdown("### 👣 Keep Moving, Keep Growing!")
st.markdown("Crafted with ❤️ by **Shrinivas Mudabe** | © 2025")
