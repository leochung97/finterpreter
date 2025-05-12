from config import CLIENT, MODEL, TEMPERATURE, FORMATTED_DATE

def query_perplexity() -> str:
    user_instructions = input("Enter your question for Perplexity AI: ")
    system_instructions = input("Enter system instructions for Perplexity AI or press enter to skip: ")

    # Check for user_instructions
    if not user_instructions:
        print("A question is required to query Perplexity AI.")
        return
    
    # Check for system_instructions or set to default
    if not system_instructions:
        system_instructions = "Provide a comprehensive and detailed response to the user's question in markdown format."

    messages = [
        {
            "role": "system",
            "content": system_instructions
        },
        {
            "role": "user",
            "content": user_instructions
        }
    ]

    response = CLIENT.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE
    )

    output = []
    output.extend((response.choices[0].message.content, user_instructions, system_instructions))

    print("Sending query to Perplexity AI...")

    print(response.choices[0].message.content)

    return output