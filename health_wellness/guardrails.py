import re
from typing import Dict, Any


class GuardrailValidator:
    """Guardrail validator"""

    @staticmethod
    def validate_goal_input(goal_text: str) -> Dict[str, Any]:
        """Validate goal input"""
        
        quantity_match = re.search(r'(\d+(?:\.\d+)?)', goal_text)
        metric_match = re.search(r'\b(kg|lbs|pounds)\b', goal_text.lower())
        duration_match = re.search(r'(\d+)\s*(days?|weeks?|months?)', goal_text.lower())

        quantity = float(quantity_match.group(1)) if quantity_match else None
        metric = metric_match.group(1) if metric_match else ""
        duration = duration_match.group(0) if duration_match else ""

    
        text_lower = goal_text.lower()
        if any(word in text_lower for word in ['lose', 'weight']):
            goal_type = "weight_loss"
        elif any(word in text_lower for word in ['gain', 'muscle']):
            goal_type = "weight_gain"
        else:
            goal_type = "fitness"

        return {
            'quantity': quantity,
            'metric': metric,
            'duration': duration,
            'goal_type': goal_type,
            'original_text': goal_text
        }

    @staticmethod
    def validate_dietary_input(diet_text: str) -> str:
        """Validate dietary input"""
        allowed_diets = ['vegetarian', 'vegan', 'keto', 'paleo', 'omnivore']
        diet_text_lower = diet_text.lower()

        for diet in allowed_diets:
            if diet in diet_text_lower:
                return diet

        return 'omnivore'

    @staticmethod
    def validate_output(response_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate output format"""
        if 'response_type' not in response_data:
            response_data['response_type'] = 'unknown'
        if 'content' not in response_data:
            response_data['content'] = {}

        return response_data

