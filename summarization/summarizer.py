import openai

def generate_summary(text: str) -> str:
    messages = [
        {"role": "system", "content": "You are an assistant that summarizes texts and provides keywords."},
        {"role": "user", "content": f"Summarize the following text concisely and clearly, and provide keywords:\n\n{text}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=300,
        temperature=0.7
    )

    # Extract the content of the summary and keywords
    result = response["choices"][0]["message"]["content"].strip()
    return result
