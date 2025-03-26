import google.generativeai as genai
import os


genai.configure(api_key=os.getenv("API_KEY"))

class Conversation:
    def __init__(self, model_name="gemini-2.0-flash"): 
        self.history = []
        self.model = genai.GenerativeModel(model_name)

    def add_message(self, role, content):
        self.history.append({"role": role, "parts": content})

    def get_history(self):
        return self.history

    def generate_response(self, user_input):
        self.add_message("user", user_input)
        response = self.model.generate_content(self.history)
        self.add_message("model", response.text)
        return response.text


