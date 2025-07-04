"""
Health & Wellness Planner Agent - Modern UI
"""
import streamlit as st
from dotenv import load_dotenv
import random
from datetime import datetime

from agent import HealthWellnessAgent
from context import UserSessionContext, RunContextWrapper

load_dotenv()

# ----- Constants -----
DAILY_TIPS = [
    "💧 Drink a glass of water first thing in the morning.",
    "🧘‍♀️ Take a 5-minute stretch break every hour.",
    "🛌 Aim for at least 7 hours of sleep tonight.",
    "🚶‍♂️ A short walk after meals helps digestion.",
    "🧠 Practice deep breathing to reduce stress.",
    "🎉 Celebrate your small wins today!",
    "🥗 Try a new healthy recipe this week.",
    "⏳ Consistency beats intensity. Small daily actions add up!",
    "😊 Remember to smile and be kind to yourself!"
]

# ----- Setup Functions -----
def get_habits():
    if 'habits' not in st.session_state:
        st.session_state.habits = [
            {'name': 'Drink 8 glasses of water', 'done': False},
            {'name': 'Walk 10,000 steps', 'done': False},
            {'name': 'Meditate 10 minutes', 'done': False},
        ]
    return st.session_state.habits

def get_mood_logs():
    if 'mood_logs' not in st.session_state:
        st.session_state.mood_logs = []
    return st.session_state.mood_logs

# ----- Streamlit Page Config -----
st.set_page_config(
    page_title="Health & Wellness Planner",
    page_icon="🏃‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----- Sidebar Styling -----
with st.sidebar:
    st.markdown(
        """
        <style>
        .st-emotion-cache-6qob1r {
            background: linear-gradient(to right, #2e2e2e, #1a1a1a);
            color: white;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.image("images/shazia.jpg", width=100)
    st.markdown("### 👤 Your Profile")

    name = st.text_input("shazia zohaib", value=st.session_state.context.get_context().name if 'context' in st.session_state else "User")
    if 'context' in st.session_state and name != st.session_state.context.get_context().name:
        st.session_state.context.update_context(name=name)

    if 'context' in st.session_state:
        goal = st.session_state.context.get_context().goal
        if goal:
            goal_display = goal.get('original_text', str(goal)) if isinstance(goal, dict) else str(goal)
            st.markdown(f"**🎯 Current Goal:** {goal_display}")

    st.markdown("**🏋️ Weekly Workouts**")
    st.progress(0.4, text="2/5 workouts done")

    st.markdown(f"> 💡 **Tip:** {random.choice(DAILY_TIPS)}")

    st.markdown("---")
    st.markdown("### ⚡ Quick Actions")
    if st.button("🎯 Set Goal"):
        st.session_state.messages.append({"role": "user", "content": "I want to set a fitness goal"})
        st.rerun()
    if st.button("🍽️ Meal Plan"):
        st.session_state.messages.append({"role": "user", "content": "I need a meal plan"})
        st.rerun()
    if st.button("💪 Workout Plan"):
        st.session_state.messages.append({"role": "user", "content": "I need a workout plan"})
        st.rerun()

# ----- Session Init -----
if 'agent' not in st.session_state:
    st.session_state.agent = HealthWellnessAgent()
if 'context' not in st.session_state:
    st.session_state.context = RunContextWrapper(UserSessionContext(name="User", uid=12345))
if 'messages' not in st.session_state:
    st.session_state.messages = []

# ----- Main App -----
st.title("🏃‍♀️ Health & Wellness Planner")
st.write("Welcome to your personal wellness assistant powered by AI!")

tabs = st.tabs(["💬 Chat", "📊 Progress", "✅ Habits", "📚 Resources"])

# ----- Chat Tab -----
with tabs[0]:
    st.header("💬 Chat Assistant")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Type your message here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.agent.process_message(prompt, st.session_state.context)
                    content = response['content']
                    st.session_state.messages.append({"role": "assistant", "content": str(content)})

                    if response['response_type'] == 'error':
                        st.error(f"❌ {content['error']}")
                    elif 'message' in content:
                        st.success(content['message'])

                    # Display structured content
                    if 'daily_plans' in content:
                        st.subheader("🍽️ 7-Day Meal Plan")
                        for day in content['daily_plans']:
                            with st.expander(f"{day['day']}"):
                                st.write(f"**Calories:** {day.get('calories', 'N/A')}")
                                for meal_type, meal in day['meals'].items():
                                    st.write(f"**{meal_type.capitalize()}:** {meal}")

                    if 'weekly_plan' in content:
                        st.subheader("💪 Workout Plan")
                        for day in content['weekly_plan']:
                            with st.expander(f"{day['day']} - {day['focus']}"):
                                st.write(f"**Exercises:** {', '.join(day['exercises'])}")
                                if 'notes' in day:
                                    st.info(f"📝 {day['notes']}")

                    if 'recommendations' in content:
                        st.subheader("📋 Recommendations")
                        for rec in content['recommendations']:
                            if isinstance(rec, dict):
                                st.write(f"- **{rec['category']}** ({rec['priority']}): {rec['recommendation']}")
                            else:
                                st.write(f"- {rec}")

                    if 'capabilities' in content:
                        st.subheader("🧠 Capabilities")
                        for cap in content['capabilities']:
                            st.write(f"✅ {cap}")

                except Exception as e:
                    st.error(f"⚠️ {str(e)}")

# ----- Progress Tab -----
with tabs[1]:
    st.header("📊 Progress Overview")
    st.info("Charts and analytics will appear here soon!")

# ----- Habits Tab -----
with tabs[2]:
    st.header("✅ Habit Tracker")
    habits = get_habits()
    for i, habit in enumerate(habits):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.write(habit['name'])
        with col2:
            checked = st.checkbox("Done", value=habit['done'], key=f"habit_{i}")
            habits[i]['done'] = checked

    new_habit = st.text_input("Add a new habit")
    if st.button("➕ Add Habit") and new_habit:
        habits.append({'name': new_habit, 'done': False})
        st.session_state.new_habit = ""
        st.experimental_rerun()

    st.subheader("📝 Mood & Energy")
    with st.form("mood_form"):
        mood = st.selectbox("Mood", ["😀 Happy", "🙂 Good", "😐 Neutral", "🙁 Low", "😞 Sad"])
        energy = st.slider("Energy Level", 1, 10, 5)
        if st.form_submit_button("Log Mood & Energy"):
            logs = get_mood_logs()
            logs.append({'date': datetime.now().strftime('%Y-%m-%d'), 'mood': mood, 'energy': energy})
            st.success("Logged successfully!")

# ----- Resources Tab -----
with tabs[3]:
    st.header("📚 Wellness Resources")
    st.markdown("- [CDC Healthy Living](https://www.cdc.gov/healthyweight/index.html)")
    st.markdown("- [WHO Physical Activity](https://www.who.int/news-room/fact-sheets/detail/physical-activity)")
    st.markdown("- [Harvard Nutrition Source](https://www.hsph.harvard.edu/nutritionsource/)")

