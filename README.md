# 🏃‍♀️ Health & Wellness Planner Agent

This is an AI-powered health and wellness assistant built using **Python** and **Streamlit**.  
It helps users set fitness goals, get meal and workout plans, track progress, and even connect with expert agents for injuries or dietary support.

---

## 🚀 Features

✅ Set fitness goals  
✅ Generate personalized meal plans  
✅ Recommend workout routines  
✅ Track progress (e.g. weight, workouts done)  
✅ Schedule check-ins  
✅ Escalate to human coach if needed  
✅ Specialized agents for nutrition and injuries  
✅ Habit tracking + Mood & energy logging  
✅ Daily wellness tips  
✅ Modern UI using Streamlit

---

## 📁 Project Structure

health_wellness/
│
├── main.py # Streamlit UI (Entry point)
├── agent.py # Main AI agent to process messages
├── context.py # Stores user session context
├── hooks.py # Logs activity, handoffs, tool usage
├── requirements.txt # Project dependencies
│
├── tools/
│ ├── goal_analyzer.py
│ ├── meal_planner.py
│ ├── workout_recommender.py
│ ├── scheduler.py
│ └── tracker.py
│
├── agents/
│ ├── escalation_agent.py
│ ├── nutrition_expert_agent.py
│ └── injury_support_agent.py
│
├── images/
│ └── shazia.jpg # Profile picture



