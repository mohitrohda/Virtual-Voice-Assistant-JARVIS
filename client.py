import openai

# Set your OpenAI API key
openai.api_key = "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"

# Now call ChatCompletion
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)