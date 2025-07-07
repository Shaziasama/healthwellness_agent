# 🏃‍♀️ Health & Wellness Planner Agent

This is an AI-powered Health & Wellness Planner app built using **Python** and **Streamlit**.  
It helps users set fitness goals, get meal/workout plans, track progress, and get help from expert agents.

---

## 📁 Project Structure and File Purpose

### 📄 `main.py`
- This is the **main Streamlit app file**.
- It shows the UI and handles user interaction like chat, goal setting, meal plan, workouts, etc.
- Tabs: Chat, Progress, Habits, Resources.

### 📄 `agent.py`
- This is the **main AI agent**.
- It decides what the user wants (goal, meal, workout, etc.).
- It also decides when to forward the user to other agents like Injury Support or Nutrition Expert.

### 📄 `context.py`
- Stores all **user session information**.
- Keeps track of: user's name, goal, diet preferences, workouts, and progress logs.

### 📄 `hooks.py`
- Tracks **app events** and logs them.
- Logs: agent start, tool usage, and agent-to-agent handoffs.

---

## 🧰 `tools/` Folder — AI Tools

Each tool helps the agent perform a specific task.

### 🛠️ `goal_analyzer.py`
- Understands and analyzes user's fitness goal.

### 🛠️ `meal_planner.py`
- Creates a **7-day meal plan** based on user's diet (vegetarian, vegan, keto, etc.).

### 🛠️ `workout_recommender.py`
- Recommends a weekly **workout routine** based on user's goal.

### 🛠️ `scheduler.py`
- Schedules **check-ins** based on frequency (daily, weekly).

### 🛠️ `tracker.py`
- Tracks user's **progress** (e.g., weight, workouts done).

---

## 👩‍⚕️ `agents/` Folder — Specialized Agents

These agents handle special situations.

### 🤝 `escalation_agent.py`
- Escalates user to a **human coach** if they ask to speak to a person.

### 🥗 `nutrition_expert_agent.py`
- Helps users with **special dietary needs** (like diabetes or allergies).

### 💪 `injury_support_agent.py`
- Helps users who have **injuries** (e.g., knee pain, back pain) and gives modified workouts.

---

## 🖼️ `images/` Folder

### 📷 `shazia.jpg`
- Your custom profile picture shown in the app sidebar.

---

## 📄 `requirements.txt`

This file includes all the Python libraries needed for the project to run.

streamlit
python-dotenv


pip install -r requirements.txt
🧪 How to Run the App
Make sure Python and pip are installed.

Open terminal in project folder.

(Optional) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # for Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run main.py
✅ App Features
🎯 Set and analyze goals

🍽️ Get personalized meal plans

💪 Get workout routines

📊 Track progress

📅 Schedule check-ins

🆘 Escalate to human coaches

🥗 Nutrition support

🤕 Injury support

✅ Habit tracker

😊 Mood & energy logging

💡 Daily wellness tips

📚 Helpful resources









