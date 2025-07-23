import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px
from datetime import datetime, timedelta

# Set up Streamlit page config
st.set_page_config(
    page_title="FitMetrics Pro",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern color scheme
PRIMARY_COLOR = "#FF4B4B"
SECONDARY_COLOR = "#0F9D58"
BG_COLOR = "#0E1117"
CARD_COLOR = "#192841"

# Apply custom styling
st.markdown(f"""
    <style>
    :root {{
        --primary: {PRIMARY_COLOR};
        --secondary: {SECONDARY_COLOR};
    }}
    
    .main {{
        background-color: {BG_COLOR};
        color: white;
    }}
    
    .stButton>button {{
        background-color: var(--primary) !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
    }}
    
    .stSlider .st-c7 {{
        background-color: var(--primary) !important;
    }}
    
    .stRadio [role=radiogroup] label [data-testid=stMarkdownContainer] p {{
        font-size: 16px !important;
    }}
    
    .card {{
        background-color: {CARD_COLOR};
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }}
    
    .metric-value {{
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        color: var(--primary) !important;
    }}
    
    .progress-container {{
        height: 8px;
        background: #2c3e50;
        border-radius: 4px;
        margin: 10px 0;
    }}
    
    .progress-bar {{
        height: 100%;
        background: var(--primary);
        border-radius: 4px;
    }}
    
    .feature-card {{
        transition: transform 0.3s;
        border-radius: 10px;
        overflow: hidden;
    }}
    
    .feature-card:hover {{
        transform: translateY(-5px);
    }}
    
    footer {{
        text-align: center;
        padding: 20px;
        margin-top: 40px;
        color: #aaa;
    }}
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/6979/6979285.png", width=80)
    st.title("FitMetrics Pro")
    st.markdown("### Track. Analyze. Transform.")
    st.markdown("Monitor your fitness journey with AI-powered insights")
    
    # User profile section
    st.subheader("👤 Your Profile")
    user_name = st.text_input("Name", "Alex Johnson")
    fitness_level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
    
    # Features with icons
    st.subheader("✨ Premium Features")
    features = [
        {"icon": "📈", "name": "Performance Analytics"},
        {"icon": "🎯", "name": "Smart Goal Setting"},
        {"icon": "🧠", "name": "AI Health Insights"},
        {"icon": "🏆", "name": "Achievement Badges"},
        {"icon": "🤝", "name": "Community Challenges"},
        {"icon": "📊", "name": "Body Composition"}
    ]
    
    cols = st.columns(2)
    for i, feature in enumerate(features):
        with cols[i % 2]:
            with st.container():
                st.markdown(f"""
                    <div class='feature-card' style='background:{CARD_COLOR};padding:15px;margin-bottom:10px;'>
                        <div style="font-size:24px">{feature['icon']}</div>
                        <div>{feature['name']}</div>
                    </div>
                """, unsafe_allow_html=True)

# Main page layout
st.title("🔥 Fitness Intelligence Dashboard")
st.markdown("Leverage data-driven insights to optimize your fitness journey")

# User Input Section
with st.container():
    st.header("📋 Fitness Profile")
    col1, col2, col3 = st.columns([1,1,1])
    
    with col1:
        st.subheader("Personal Stats")
        age = st.slider('Age', 1, 100, 28, help="Your current age")
        weight = st.number_input('Weight (kg)', 40, 200, 75)
        height = st.number_input('Height (cm)', 120, 220, 175)
        
    with col2:
        st.subheader("Activity Metrics")
        duration = st.slider('Workout Duration (min)', 1, 180, 45)
        heart_rate = st.slider('Heart Rate (BPM)', 50, 200, 125)
        steps = st.slider('Daily Steps', 1000, 25000, 8500)
        
    with col3:
        st.subheader("Body Composition")
        body_fat = st.slider('Body Fat %', 5, 50, 18)
        muscle_mass = st.slider('Muscle Mass %', 30, 90, 65)
        gender = st.radio("Gender", ("Male", "Female", "Other"))
        
    # Calculate BMI
    bmi = weight / ((height/100) ** 2)
    st.info(f"**Your BMI:** {bmi:.1f} - {'Healthy' if 18.5 <= bmi <= 24.9 else 'Needs improvement'}")

# Prediction Section
with st.container():
    st.header("🔥 Calories Burned Prediction")
    
    # Simulate processing
    with st.spinner("Analyzing your metrics with AI..."):
        time.sleep(1.5)
    
    # Create metrics cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div class="card">
                <h3>Estimated Calories</h3>
                <div class="metric-value">412 kcal</div>
                <div class="progress-container">
                    <div class="progress-bar" style="width: 65%"></div>
                </div>
                <p>65% of daily goal</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
            <div class="card">
                <h3>Metabolic Rate</h3>
                <div class="metric-value">1,850 kcal</div>
                <div class="progress-container">
                    <div class="progress-bar" style="width: 82%"></div>
                </div>
                <p>Daily energy expenditure</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
            <div class="card">
                <h3>Fitness Score</h3>
                <div class="metric-value">86/100</div>
                <div class="progress-container">
                    <div class="progress-bar" style="width: 86%"></div>
                </div>
                <p>Excellent condition</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Recommendation
    st.success("💡 **AI Recommendation:** Increase cardio duration by 15% to reach your calorie target faster. Consider adding HIIT workouts 3x/week.")

# Visualization Section
with st.container():
    st.header("📊 Performance Analytics")
    
    # Generate fitness data
    dates = [datetime.now() - timedelta(days=i) for i in range(7, 0, -1)]
    activity_data = pd.DataFrame({
        'Date': dates,
        'Calories Burned': np.random.randint(300, 600, 7),
        'Workout Duration': np.random.randint(20, 90, 7),
        'Steps': np.random.randint(5000, 15000, 7),
        'Heart Rate': np.random.randint(110, 160, 7)
    })
    
    # Create tabs for different visualizations
    tab1, tab2, tab3 = st.tabs(["Weekly Trend", "Body Composition", "Performance Metrics"])
    
    with tab1:
        fig = px.line(activity_data, x='Date', y='Calories Burned', 
                      title='Weekly Calories Burned', markers=True)
        fig.update_layout(plot_bgcolor=BG_COLOR, paper_bgcolor=BG_COLOR, font_color='white')
        st.plotly_chart(fig, use_container_width=True)
        
    with tab2:
        body_data = pd.DataFrame({
            'Metric': ['Body Fat', 'Muscle Mass', 'Hydration', 'Bone Density'],
            'Value': [18, 65, 72, 92],
            'Target': [15, 70, 80, 95]
        })
        fig = px.bar(body_data, x='Metric', y=['Value', 'Target'], barmode='group',
                     title='Body Composition Analysis')
        fig.update_layout(plot_bgcolor=BG_COLOR, paper_bgcolor=BG_COLOR, font_color='white')
        st.plotly_chart(fig, use_container_width=True)
        
    with tab3:
        fig = px.scatter(activity_data, x='Workout Duration', y='Calories Burned', 
                         size='Heart Rate', color='Steps',
                         title='Workout Efficiency Analysis')
        fig.update_layout(plot_bgcolor=BG_COLOR, paper_bgcolor=BG_COLOR, font_color='white')
        st.plotly_chart(fig, use_container_width=True)

# Health Insights
with st.container():
    st.header("💡 AI-Powered Health Insights")
    
    cols = st.columns(2)
    with cols[0]:
        with st.expander("📌 Nutritional Recommendations", expanded=True):
            st.markdown("""
            - **Increase protein intake** to 1.8g/kg body weight for muscle recovery
            - **Hydration target:** 3L water daily (currently at 2.1L)
            - **Add superfoods:** Chia seeds, blueberries, spinach
            - **Supplement suggestion:** Omega-3 and Vitamin D3
            """)
            
    with cols[1]:
        with st.expander("🏋️ Workout Optimization", expanded=True):
            st.markdown("""
            - **Optimal workout window:** 6:00-8:00 AM (based on chronotype)
            - **Recovery suggestion:** Add yoga 2x/week for flexibility
            - **New exercise:** Try kettlebell swings for core activation
            - **Progress plateau:** Increase weights by 5% next week
            """)
    
    st.button("🔄 Generate New Recommendations", use_container_width=True)

# Footer Section
st.markdown("---")
st.markdown("""
    <footer>
        <p>Developed with ❤️ using Streamlit | FitMetrics Pro v2.0</p>
        <p>© 2025 Shrinivas Mudabe. All Rights Reserved. | Privacy Policy | Terms of Service</p>
    </footer>
""", unsafe_allow_html=True)
