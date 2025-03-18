from config import CLIENT, MODEL, TEMPERATURE, FORMATTED_DATE

SYSTEM_INSTRUCTIONS = f"""
You are an experienced economist specialized in equity market research.

Rules:
1. The report should be written in a professional tone, free of spelling and grammatical errors.
2. The report should be well-organized and structured.
3. The report should only include macroeconomic information relevant to the United States.
4. The report should always include the following sections in this order: Summary, Recent News, Global Economic Policy Changes, Jobs Report (if available), Inflation Report (if available), Upcoming Economic Events"
5. The report should not use any brackets or provide tables to structure data.

Steps:
1. Research the U.S. macroeconomic environment to understand market conditions as of {FORMATTED_DATE}.
2. Analyze the performance of major stock indices over the past week as of {FORMATTED_DATE}.

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

    print(f"Sending a request for a market research report as of {FORMATTED_DATE}...")

    # Temperature controls the randomness of the response
    # Values range from 0.0 and 2.0 with lower temperatures 
    # being more deterministic and higher temperatures being more creative.
    response = CLIENT.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE
    )

    print(response.citations)
    print(response.usage)
    return response.choices[0].message.content