import openai
import os

def analyze_text(text):
    API_KEY = os.getenv("OPENAI_API_KEY")
    openai.api_key = API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Analyze the political bias of the following text and generate a 
counterargument."},
            {"role": "user", "content": text}
        ]
    )
    return response["choices"][0]["message"]["content"]

