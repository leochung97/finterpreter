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
                
                "Rules:"
                "1. The report should be written in a professional tone, free of spelling and grammatical errors."
                "2. The report should be well-organized and structured."
                "3. The report should include publicly sourced information."
                
                "Steps:"
                "1. Research the company and industry to understand the business model and competitive landscape."
                "2. Analyze the company's financial statements over the past 3 fiscal years to assess financial performance."
                "3. Calculate and provide industry-specific valuation metrics such as Price to Earnings (P/E), Price to Sales (P/S), and Price to Book (P/B) ratios."
                "4. For technology companies, provide Price to Earnings Growth (PEG) ratio and forward year multiples."
                "5. Identify comparable companies and compare their valuation metrics to the target company's."
                "6. Provide a recommendation to buy, sell, or hold the stock based on your report."
                "7. Provide all of the citations used in a list."
            )
        },
        {
            "role": "user",
            "content": (
                f"Generate an equity research report for {ticker}."
            )
        }
    ]

    print("Sending the following as a message:")
    print(messages)

    # Temperature controls the randomness of the response
    # Values range from 0.0 and 2.0 with lower temperatures 
    # being more deterministic and higher temperatures being more creative.
    response = client.chat.completions.create(
        model="sonar-pro",
        messages=messages,
        temperature=0.1
    )

    print("Received the following response:")
    print(response)

    ### NTD: Need to parse the response to extract citations in a clickable format
    return response.choices[0].message.content

if __name__ == "__main__":
    ticker = input("Please enter a stock ticker: ").upper()
    report = thesis(ticker)
    print(report)