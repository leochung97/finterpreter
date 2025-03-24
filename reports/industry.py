from config import CLIENT, MODEL, TEMPERATURE, FORMATTED_DATE

def industry_research(sector: str) -> str:
    SYSTEM_INSTRUCTIONS = f"""You are an experienced {sector} analyst.

    Rules:
    1. The response should be provided in markdown format.
    2. The report should be professional, well-organized and structured.
    3. The report should include publicly sourced information.
    4. The report should always include the following sections in this order: Industry Overview, Recent Industry News, Last Twelve Month Stock Performance of the Sector ETF.
    5. The report should include an appendix that explains any industry-specific jargon used in the report.
    6. Always include research and information from consulting firms such as Boston Consulting Group, McKinsey, Bain & Company, Deloitte, PwC, and EY-Parthenon. This list is not exclusive - include any other consulting firms that have relevant information on the {sector}."""

    USER_INSTRUCTIONS = f"""Write a research report on {sector} using the latest data available as of {FORMATTED_DATE}. Include an overview of the sector, any recent trends and news, and the {sector}'s ETF price performance over the past twelve months."""

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

    print(f"Creating an industry research report on {sector} using latest data available as of {FORMATTED_DATE}.")

    response = CLIENT.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE
    )
    
    output = []
    formatted_citations = "\n".join(f"{number}. {source}" for number, source in enumerate(response.citations, start = 1))
    output.extend((response.choices[0].message.content, formatted_citations, SYSTEM_INSTRUCTIONS, USER_INSTRUCTIONS))

    print(f"Industry research report on {sector} created successfully.")

    return output