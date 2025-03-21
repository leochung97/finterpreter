from config import CLIENT, MODEL, TEMPERATURE, FORMATTED_DATE

def industry_research(sector: str) -> str:
    SYSTEM_INSTRUCTIONS = f"""
    
    """

    USER_INSTRUCTIONS = f"""
    
    """

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