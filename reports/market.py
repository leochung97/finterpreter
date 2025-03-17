from config import CLIENT

SYSTEM_INSTRUCTIONS = """
You are an experienced economist specialized in equity market research.

Rules:
1. The report should be written in a professional tone, free of spelling and grammatical errors.
2. The report should be well-organized and structured.
3. The report should include publicly sourced information.

Steps:
1. Research the macroeconomic environment to understand the current market conditions.
2. Analyze the performance of major stock indices over the past week.
3. Identify key trends and factors driving the stock market performance.
4. Analyze the performance of major sectors and industries in the stock market.
5. Provide a forecast for the stock market performance over the next 6 months based on recent macroeconomic news.
6. Analyst macroeconomic indicators and geopolitical events that could impact the stock market.
7. List any recent central bank policy changes from around the world and their implications.
8. Provide actionable trading insights.
"""

def market_research() -> str:
    ### NTD: User content should request for financials and valuation metrics to be provided in a Pydantic JSON format
    ### Check documentation for more information: https://docs.perplexity.ai/guides/structured-outputs
    messages = [
        {
            "role": "system",
            "content": SYSTEM_INSTRUCTIONS
        },
        {
            "role": "user",
            "content": "Generate an economic research report."
        }
    ]

    print("Sending messages to Perplexity API")

    # Temperature controls the randomness of the response
    # Values range from 0.0 and 2.0 with lower temperatures 
    # being more deterministic and higher temperatures being more creative.
    response = CLIENT.chat.completions.create(
        model="sonar-pro",
        messages=messages,
        temperature=0.1
    )

    ### NTD: Need to parse the response to extract citations in a clickable format
    return response.choices[0].message.content