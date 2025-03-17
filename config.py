from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")


# Environment variables
CLIENT = OpenAI(
    api_key=api_key,
    base_url="https://api.perplexity.ai"
)
