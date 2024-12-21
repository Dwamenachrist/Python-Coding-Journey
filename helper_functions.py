import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Access the API key from the environment variables
api_key = os.getenv('API_KEY')

# Check if the API key exists
if api_key is None:
    raise ValueError("API key not found in the environment variables.")

# Configure the Genai API key
genai.configure(api_key=api_key)


def print_llm_response(prompt):
    """
    Sends a prompt to the Gemini LLM API and returns the response.

    Args:
      prompt: The text prompt to send to the LLM.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text  # Return the response text
    except Exception as e:
        print(f"Error generating content: {e}")

