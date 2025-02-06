import openai

def generate_summary(text: str, summary_size: str) -> str:
    # Define the maximum tokens based on the summary size
    max_tokens = {
        "short": 100,
        "medium": 200,
        "long": 300
    }.get(summary_size, 200)  # Default to medium if not specified

    messages = [
        {"role": "system", "content": "You are an assistant that summarizes texts and provides keywords."},
        {"role": "user", "content": f"Summarize the following text concisely and provide keywords:\n\n{text}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=max_tokens,
        temperature=0.7
    )

    # Extract and return the summary and keywords
    return response["choices"][0]["message"]["content"].strip()
