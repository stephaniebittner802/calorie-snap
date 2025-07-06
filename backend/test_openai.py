from dotenv import load_dotenv
load_dotenv()
import os
import openai
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "How many calories are in a banana?"}
        ]
    )
    print("API key works! Response:")
    print(response.choices[0].message.content)
except Exception as e:
    print("API key failed:")
    print(e)