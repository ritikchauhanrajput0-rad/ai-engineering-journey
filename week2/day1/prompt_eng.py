import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api ket not found")

client =Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

def llm_ans(prompt):
    message={
        "role":"user",
        "content":prompt

    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    ans=response.choices[0].message.content
    return ans


bad_prompt="""
#role
you are a tech hiring officer in microsoft
#task
you have to take interview for a software intern at nsut
#constraint
Ask technically challenging questions appropriate for a software engineering intern.
Evaluate the candidate's answer for correctness and reasoning.

#output
give the output in not more than two lines
Example:
Candidate: "Good morning, my name is Ritik and I have good DSA skills."

Assistant:
"Good morning Ritik. Explain how a hash map works and give its average time complexity."
#fallback
if the student is not maintaining the decorem make him go outside 

good morning ir my name is ritik i have good dsa skills




"""

print(llm_ans(bad_prompt))