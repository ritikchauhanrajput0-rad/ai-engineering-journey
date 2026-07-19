import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
myapi_key=os.getenv("GROQ_API_KEY")
if not myapi_key:
    raise ValueError("NO ITEM FOUND")

client =Groq(api_key=myapi_key)

model="llama-3.3-70b-versatile"
role="user"

prompt1="hi , how are you"
prompt2="explain time travel in detail"
prompt3="Write  a 1000 word essay on machine learning"

prompts=[prompt1,prompt2,prompt3]

for prompt in prompts:
    message_system={
    "role":"system",
    "content": "you are anushka sharma "
    }

    message = {
        "role": role,
        "content": prompt
    }

    messages = [message_system,message]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    usage = response.usage

    print(
        f"Prompt: {prompt}\n"
        f"Prompt Tokens: {usage.prompt_tokens}\n"
        f"Completion Tokens: {usage.completion_tokens}\n"
        f"Total Tokens: {usage.total_tokens}\n"
    )

    
# message={
#     "role":role,
#     "content":prompt
# }
# messages=[message_system, message]
# response = client.chat.completions.create(model=model,messages=messages,temperature=1)
# print(response)
# print (333333333333333333333333333333333333)
# answer=response.choices[0].message.content
# print(answer)
    