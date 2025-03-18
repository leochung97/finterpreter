from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")


# Environment variables
CLIENT = OpenAI(
    api_key=api_key,
    base_url="https://api.perplexity.ai"
)

MODEL = "sonar-deep-research"

TEMPERATURE = 0.1

today = datetime.now()
FORMATTED_DATE = today.strftime("%m/%d/%Y")