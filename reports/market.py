from config import CLIENT, MODEL, TEMPERATURE, FORMATTED_DATE

def market_research() -> str:
    SYSTEM_INSTRUCTIONS = f"""You are an experienced economist specialized in equity market research.

    Rules:
    1. The report should be written in a professional tone, free of spelling and grammatical errors.
    2. The report should be well-organized and structured.
    3. The report should include macroeconomic information relevant to the United States.
    4. The report should always include the following sections in this order: Summary, Recent News, Global Economic Policy Changes, Jobs Report (if available), Inflation Report (if available), and Upcoming Economic Events."
    5. The report should not use any brackets or provide tables to structure data.
    6. The report should always use the latest data available as of {FORMATTED_DATE}."""

    USER_INSTRUCTIONS = f"""Generate an economic research report using the latest data available as of {FORMATTED_DATE}."""
    
    ### NTD: User content should request for economic outlook data to be provided in a Pydantic JSON format
    ### Check documentation for more information: https://docs.perplexity.ai/guides/structured-outputs
    messages = [
        {
            "role": "system",
            "content": SYSTEM_INSTRUCTIONS
        },
        {
            "role": "user",
            "content": USER_INSTRUCTIONS
        }
    ]

    print(f"Creating a market research report as of {FORMATTED_DATE}.")

    response = CLIENT.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE
    )
    
    output = []
    formatted_citations = "\n".join(f"{number}. {source}" for number, source in enumerate(response.citations, start = 1))
    output.extend((response.choices[0].message.content, formatted_citations, SYSTEM_INSTRUCTIONS, USER_INSTRUCTIONS))

    print("Market research report created successfully.")
    
    return output