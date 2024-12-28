import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set the OpenAI API key globally
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIChatbot:
    """
    A class to interact with the OpenAI Chat API.
    """

    def __init__(self, model: str = "gpt-3.5-turbo"):
        """
        Initialize the OpenAI Chatbot class with a model.
        """
        self.model = model

    def get_response(self, prompt: str, temperature: float = 0.7, max_tokens: int = 300) -> str:
        """
        Send a prompt to OpenAI API and return the response.

        Args:
            prompt (str): User input for the chatbot.
            temperature (float): Level of randomness in the response.
            max_tokens (int): Maximum length of the response.

        Returns:
            str: The chatbot's response.
        """
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for music production."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            # Access the content of the first choice correctly
            return response.choices[0].message.content.strip()
        except openai.OpenAIError as e:
            return f"OpenAI API Error: {str(e)}"
        except Exception as e:
            return f"Unexpected Error: {str(e)}"
