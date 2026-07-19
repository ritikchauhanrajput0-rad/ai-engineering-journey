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

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema()

response_format={
    "type":"json_object"
}

system_prompt=f"""
Exteact the personal information from the 
ticket strictly based on thi schema
and return output in json format
{schema}
"""

message_system={
    "role":"system",
    "content": system_prompt
}

text="hello my name is ritik and i " \
"have problem with " \
"the education ministry . my address is delhi" \
"my email is abc@gmail.com" \
"and my contact is xyxyz"

prompt=f"""
This is a customer ticket please extract the 
personal information from this
{text}
"""

message={
    "role":role,
    "content":prompt
}
messages=[message_system,message]
response = client.chat.completions.create(
    model=model,messages=messages,
    temperature=2,
    response_format=response_format)
print(response)
print (333333333333333333333333333333333333)
answer=response.choices[0].message.content
print(answer)

## to read this output as prompt

import json 
raw_json =answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name )
print(ticket.email )
print(ticket.issue )
    