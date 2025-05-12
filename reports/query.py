from config import CLIENT, MODEL, TEMPERATURE, FORMATTED_DATE

def query_perplexity() -> str:
    user_instructions = input("Enter your question for Perplexity AI: ")
    system_instructions = input("Enter system instructions for Perplexity AI or press enter to skip: ")

    messages = [
        {
            "role": "system",
            "content": system_instructions if system_instructions else ""
        },
        {
            "role": "user",
            "content": user_instructions
        }
    ]

    print(f"Sending the following request to Perplexity AI: {messages}")

    response = CLIENT.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE
    )

    output = []
    output.extend(response.choices[0].message.content, user_instructions, system_instructions)

    print(output)

    return output