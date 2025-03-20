from config import CLIENT, MODEL, TEMPERATURE, FORMATTED_DATE

SYSTEM_INSTRUCTIONS = f"""
You are an experienced equity research analyst.

Rules:
1. The report should be written in a professional tone, free of spelling and grammatical errors.
2. The report should be well-organized and structured.
3. The report should include publicly sourced information.
4. The report should always include the following sections in this order: Business Overview, Recent News, Last Twelve Month Financial Performance, Current Valuation Multiples."
5. The report should not use any brackets or provide tables to structure data.
6. The report should source financial metrics from company investor relations page, SEC filings, or reputable financial news sources.
7. The report should not source financial multiples or data from sources other than the company's investor relations page or SEC filings.
7. The report should always use the latest data available as of {FORMATTED_DATE}.
"""

def equity_research(ticker: str) -> str:
    USER_INSTRUCTIONS = f"""
    Generate a comprehensive equity research report on {ticker} using the latest data available as of {FORMATTED_DATE}.

    Include the following elements:
    1. Investment summary and rating
    2. Key financial metrics and recent performance
    3. Detailed analysis of business segments
    4. Discussion of recent product launches and technologicaal advancements
    5. Market position aand competitive landscape
    6. Forwaard-looking guidance and management commentary from most recent earnings call
    7. Valuation analysis aand price target justification
    8. Key risks and opportunities
    9. Most recently available financial tables (Income Statement, Balance Sheet, Caash Flow Statement)

    Please format the report professionally, using headers, bullet points, and tables where appropriate. Include specific numbers and percentages to support your analysis.
    """
    
    ### NTD: User content should request for financials and valuation metrics to be provided in a Pydantic JSON format
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

    print(f"Creating an equity research report on {ticker} using latest data available as of {FORMATTED_DATE}.")

    response = CLIENT.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE
    )
    
    output = []
    formatted_citations = "\n".join(f"{number}. {source}" for number, source in enumerate(response.citations, start = 1))
    output.extend((SYSTEM_INSTRUCTIONS, USER_INSTRUCTIONS, formatted_citations, response.choices[0].message.content))

    print(f"Equity research report on {ticker} created successfully.")

    return output