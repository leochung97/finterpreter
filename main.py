from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# Perplexity AI API Client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.perplexity.ai"
)

def thesis(ticker: str) -> str:
    ### NTD: User content should request for financials and valuation metrics to be provided in a Pydantic JSON format
    ### Check documentation for more information: https://docs.perplexity.ai/guides/structured-outputs
    messages = [
        {
            "role": "system",
            "content": (
                "You are an experienced equity research analyst."
                "Provide a concise and objective equity research report for the given stock ticker."
            )
        },
        {
            "role": "user",
            "content": (
                f"Generate an equity research report for {ticker}."
                "Include the following sections: Business Overview, Investment Summary,"
                "Business Description, Industry Analysis, Financial Analysis, Valuation,"
                "Investment Risks, and Comparable Companies Analysis."
            )
        }
    ]

    # Temperature controls the randomness of the response
    # Values range from 0.0 and 2.0 with lower temperatures 
    # being more deterministic and higher temperatures being more creative.
    response = client.chat.completions.create(
        model="sonar-pro",
        messages=messages,
        temperature=0.2
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    ticker = input("Please enter a stock ticker: ").upper()
    report = thesis(ticker)
    print(report)