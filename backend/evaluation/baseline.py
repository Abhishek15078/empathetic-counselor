import random


class BaselineSystem:
    """
    Simple rule-based chatbot.

    No emotion detection.
    No RAG.
    No personalization.
    No safety reasoning.
    """

    GENERIC_RESPONSES = [

        "Thank you for sharing that. Could you tell me more about your situation?",

        "I appreciate you telling me this. Would you like to explain what has been happening?",

        "That sounds like an important concern. Can you share more details?",

        "I'm here to listen. Could you tell me a little more?",

        "Thank you for opening up. What happened that led to this situation?",

        "Would you like to tell me more about what you're experiencing?",

        "I'm listening. Please continue if you'd like to share more.",

        "Can you describe your situation in a little more detail?",

        "Thank you for sharing this. What has been the most difficult part?",

        "I'd like to understand better. Could you explain a little more?"

    ]

    def generate_response(self, message):

        return random.choice(self.GENERIC_RESPONSES)