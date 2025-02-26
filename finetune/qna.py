from openai import OpenAI
client = OpenAI(
  api_key="your_key_here"
)

completion = client.chat.completions.create(
    model="ft:gpt-4o-2024-08-06:personal::",
    messages=[
        {"role": "user", "content": "Can you tell me more about USTH and all about them!"}
    ]
)

print(completion.choices[0].message)
