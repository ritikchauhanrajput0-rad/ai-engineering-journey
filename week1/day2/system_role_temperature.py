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
prompt="do you know hardik pandya"

message_system={
    "role":"system",
    "content": "you are MAHIEKA SHARMA"
}

message={
    "role":role,
    "content":prompt
}
messages=[message_system, message]
response = client.chat.completions.create(model=model,messages=messages)
# print(response)
print (333333333333333333333333333333333333)
answer=response.choices[0].message.content
print(answer)
    