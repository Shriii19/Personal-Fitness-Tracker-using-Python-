import streamlit as st
import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Set up Streamlit page config
st.set_page_config(page_title="Professional Fitness Tracker", page_icon="🏋️", layout="wide", initial_sidebar_state="expanded")

# Sidebar navigation
st.sidebar.title("🏃 Personal Fitness Tracker")
st.sidebar.write("Monitor your fitness journey with real-time insights and goal tracking.")

st.sidebar.subheader("💡 Additional Features")
st.sidebar.write("- **Track Your Progress** 📈")
st.sidebar.write("- **Set Fitness Goals** 🎯")
st.sidebar.write("- **Personalized Health Tips** 🏥")
st.sidebar.write("- **Health Advice** 📌")

# Main page layout
st.title("🔥 Fitness Tracker Dashboard")
st.markdown("Stay on top of your fitness goals by predicting calories burned and analyzing progress.")

# User Input Section
st.header("🏋️ Enter Your Fitness Data")
col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider('Age', 1, 100, 25)
    bmi = st.slider('BMI', 10, 50, 20)
with col2:
    duration = st.slider('Workout Duration (min)', 1, 100, 30)
    heart_rate = st.slider('Heart Rate (BPM)', 50, 200, 100)
with col3:
    body_temp = st.slider('Body Temperature (°C)', 30, 45, 37)
    gender = st.radio("Gender", ("Male", "Female"))
    gender = 1 if gender == "Male" else 0

user_data = pd.DataFrame({
    'Age': [age],
    'BMI': [bmi],
    'Duration': [duration],
    'Heart Rate': [heart_rate],
    'Body Temp': [body_temp],
    'Gender_male': [gender]
})

st.subheader("📊 Your Input Summary")
st.dataframe(user_data.style.set_properties(**{'background-color': 'black', 'color': 'white'}))

# Prediction Section
st.header("🔥 Predicted Calories Burned")
st.write("Processing your data... Please wait.")
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.02)

# Dummy Model Training (Replace with actual model and dataset)
X_train = np.random.rand(100, 5)
y_train = np.random.randint(100, 500, 100)
model = RandomForestRegressor()
model.fit(X_train, y_train)

prediction = model.predict(user_data.drop(columns=['Gender_male'], axis=1))
st.success(f"Estimated Calories Burned: **{round(prediction[0], 2)} kcal**")

# Sidebar Features
st.sidebar.subheader("📈 Track Your Progress")
progress_data = np.random.randint(100, 500, size=7)
st.sidebar.line_chart(progress_data)

st.sidebar.subheader("🎯 Set Fitness Goals")
fitness_goal = st.sidebar.number_input("Daily Calorie Burn Goal (kcal)", min_value=100, max_value=1000, step=50, value=500)
st.sidebar.success(f"Your target is {fitness_goal} kcal per day!")

st.sidebar.subheader("🏥 Personalized Health Tips")
health_tips = [
    "💧 Stay hydrated and drink enough water throughout the day.",
    "🥗 Maintain a balanced diet rich in protein, fiber, and essential nutrients.",
    "💤 Ensure sufficient sleep and recovery to optimize performance.",
    "🏋️ Incorporate both cardio and strength training exercises.",
    "❤️ Monitor your heart rate to maintain optimal workout intensity.",
    "🧘 Practice mindfulness and stress management for overall well-being."
]
st.sidebar.info(np.random.choice(health_tips))

st.sidebar.subheader("📌 Health Advice")
advice_list = [
    "⚡ Start your day with a short stretching routine to improve flexibility.",
    "🍽️ Eat small, frequent meals to keep your metabolism active.",
    "🚶 Take at least 10,000 steps per day for overall health benefits.",
    "🏃‍♂️ Gradually increase workout intensity to prevent injuries.",
    "📉 Track your daily caloric intake and balance it with exercise.",
    "🚰 Drink a glass of water before every meal to help with digestion and hydration.",
    "🛌 Aim for at least 7-8 hours of quality sleep for better recovery.",
    "🧘‍♀️ Practice yoga or meditation to reduce stress and improve focus."
]
st.sidebar.success(np.random.choice(advice_list))

# Footer Section
st.markdown("---")
st.markdown("### 👣 Stay Consistent & Keep Moving!")
st.markdown("Developed with ❤️ for fitness enthusiasts. Keep tracking, keep improving!")
st.markdown("© 2025 Shrinivas Mudabe. All Rights Reserved.")
