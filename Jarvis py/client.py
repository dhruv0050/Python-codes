from openai import OpenAI


client  = OpenAI(
    api_key = "sk-proj-V0UQlzmAO2q7pN5YgUpoT3BlbkFJLgkdh750mPqKoPANBSWf"
)
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)