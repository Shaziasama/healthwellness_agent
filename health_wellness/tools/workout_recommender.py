from typing import Dict, Any, List
from context import RunContextWrapper
from guardrails import GuardrailValidator
from hooks import hook_manager


class WorkoutRecommenderTool:
    """Tool for recommending workout plans"""

    def __init__(self):
        self.name = "workout_recommender"

    def recommend_workout(self, preferences: str, goal: Dict[str, Any], context: RunContextWrapper) -> Dict[str, Any]:
        """Recommend workout plan"""
        hook_manager.log_tool_start(self.name)

        try:
            
            workout_prefs = self.parse_preferences(preferences)

            
            workout_plan = self.create_workout_plan(workout_prefs, goal)

            
            context.update_context(workout_plan=workout_plan)
            context.get_context().add_progress_log("workout_planning", "Generated workout plan")

            response = {
                "response_type": "workout_plan",
                "content": workout_plan
            }

            return GuardrailValidator.validate_output(response)

        except Exception as e:
            return {
                "response_type": "error",
                "content": {"error": str(e)}
            }

    def parse_preferences(self, preferences: str) -> Dict[str, Any]:
        """Parse workout preferences into experience level and type"""
        prefs = {
            "experience_level": "beginner",
            "workout_type": "strength"
        }

        text = preferences.lower()
        if "advanced" in text or "expert" in text:
            prefs["experience_level"] = "advanced"
        elif "intermediate" in text:
            prefs["experience_level"] = "intermediate"

        if "cardio" in text:
            prefs["workout_type"] = "cardio"

        return prefs

    def create_workout_plan(self, prefs: Dict[str, Any], goal: Dict[str, Any]) -> Dict[str, Any]:
        """Create workout plan based on preferences and goal"""

        
        strength_workouts = {
            "beginner": [
                {"day": "Monday", "focus": "Upper Body", "exercises": ["Push-ups", "Pull-ups", "Shoulder Press"], "duration": "30 minutes"},
                {"day": "Wednesday", "focus": "Lower Body", "exercises": ["Squats", "Lunges", "Calf Raises"], "duration": "30 minutes"},
                {"day": "Friday", "focus": "Full Body", "exercises": ["Burpees", "Planks", "Mountain Climbers"], "duration": "30 minutes"}
            ],
            "intermediate": [
                {"day": "Monday", "focus": "Chest & Triceps", "exercises": ["Bench Press", "Dips", "Tricep Extensions"], "duration": "45 minutes"},
                {"day": "Tuesday", "focus": "Back & Biceps", "exercises": ["Rows", "Pull-ups", "Bicep Curls"], "duration": "45 minutes"},
                {"day": "Thursday", "focus": "Legs", "exercises": ["Squats", "Deadlifts", "Lunges"], "duration": "45 minutes"},
                {"day": "Friday", "focus": "Shoulders", "exercises": ["Shoulder Press", "Lateral Raises", "Shrugs"], "duration": "45 minutes"}
            ],
            "advanced": [
                {"day": "Monday", "focus": "Chest", "exercises": ["Bench Press", "Incline Press", "Flyes"], "duration": "60 minutes"},
                {"day": "Tuesday", "focus": "Back", "exercises": ["Deadlifts", "Rows", "Pull-ups"], "duration": "60 minutes"},
                {"day": "Wednesday", "focus": "Legs", "exercises": ["Squats", "Romanian Deadlifts", "Leg Press"], "duration": "60 minutes"},
                {"day": "Thursday", "focus": "Shoulders", "exercises": ["Military Press", "Lateral Raises", "Rear Delts"], "duration": "60 minutes"},
                {"day": "Friday", "focus": "Arms", "exercises": ["Close-Grip Bench", "Tricep Dips", "Bicep Curls"], "duration": "60 minutes"}
            ]
        }

    
        cardio_workouts = {
            "beginner": [
                {"day": "Monday", "activity": "Walking", "duration": "20 minutes"},
                {"day": "Wednesday", "activity": "Cycling", "duration": "15 minutes"},
                {"day": "Friday", "activity": "Swimming", "duration": "15 minutes"}
            ],
            "intermediate": [
                {"day": "Monday", "activity": "Running", "duration": "30 minutes"},
                {"day": "Tuesday", "activity": "HIIT", "duration": "25 minutes"},
                {"day": "Thursday", "activity": "Cycling", "duration": "35 minutes"},
                {"day": "Saturday", "activity": "Long Walk", "duration": "45 minutes"}
            ],
            "advanced": [
                {"day": "Monday", "activity": "Interval Running", "duration": "40 minutes"},
                {"day": "Tuesday", "activity": "HIIT Circuit", "duration": "30 minutes"},
                {"day": "Wednesday", "activity": "Cycling", "duration": "50 minutes"},
                {"day": "Thursday", "activity": "Swimming", "duration": "40 minutes"},
                {"day": "Saturday", "activity": "Long Run", "duration": "60 minutes"}
            ]
        }

        
        workout_type = prefs.get("workout_type", "strength")
        experience = prefs.get("experience_level", "beginner")

        if workout_type == "cardio":
            weekly_plan = cardio_workouts.get(experience, cardio_workouts["beginner"])
        else:
            weekly_plan = strength_workouts.get(experience, strength_workouts["beginner"])

        return {
            "workout_type": workout_type,
            "experience_level": experience,
            "weekly_plan": weekly_plan,
            "safety_tips": [
                "Always warm up before exercising",
                "Stay hydrated",
                "Listen to your body",
                "Use proper form"
            ]
        }

