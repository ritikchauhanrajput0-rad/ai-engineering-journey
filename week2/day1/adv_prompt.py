import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"


# --------------------------------------------------
# LLM FUNCTION
# --------------------------------------------------

def llm_ans(messages):

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return response.choices[0].message.content


# --------------------------------------------------
# INTERVIEWER SYSTEM PROMPT
# --------------------------------------------------

system_prompt = {
    "role": "system",
    "content": """
You are a technical interviewer conducting a software
engineering internship interview.

Rules:

- Ask one technical question at a time.
- Focus mainly on DSA topics like dynamic programming , graphs and greedy algorithm and computer science fundamentals.
- Analyze the candidate's previous answer before asking
  the next question.
- Adjust the difficulty based on the candidate's performance.
- Do not give the candidate the answer.
- Keep your responses concise.
- Behave like a professional interviewer.
"""
}


# --------------------------------------------------
# START INTERVIEW
# --------------------------------------------------

messages = [system_prompt]

print("================================")
print("      TECHNICAL INTERVIEW")
print("================================")
print("Type 'exit' whenever you want to end the interview.\n")


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    answer = llm_ans(messages)

    print("\nAI:", answer)
    print()

    messages.append({
        "role": "assistant",
        "content": answer
    })


# --------------------------------------------------
# FINAL ASSESSMENT SCHEMA
# --------------------------------------------------

class Assessment(BaseModel):

    score: float

    dsa_score: float

    problem_solving_score: float

    technical_score: float

    communication_score: float

    strengths: list[str]

    weaknesses: list[str]

    verdict: str

    recommendation: str


# --------------------------------------------------
# FINAL ASSESSMENT
# --------------------------------------------------

assessment_schema = Assessment.model_json_schema()

assessment_system_prompt = {
    "role": "system",
    "content": f"""
You are a senior technical interviewer evaluating
a completed software engineering internship interview.

Analyze the complete conversation and evaluate the
candidate objectively.

Return ONLY valid JSON matching this schema:

{assessment_schema}

Rules:

- Score the candidate from 0 to 100.
- DSA score must be from 0 to 100.
- Problem-solving score must be from 0 to 100.
- Technical knowledge score must be from 0 to 100.
- Communication score must be from 0 to 100.
- Base the assessment only on what the candidate
  demonstrated during the interview.
- Do not invent skills or knowledge.
- Give concise strengths and weaknesses.
- Give a clear final verdict.
- Recommend whether the candidate should move
  to the next interview round.
"""
}


assessment_user_prompt = {
    "role": "user",
    "content": f"""
The following is the complete interview conversation:

{messages}

Evaluate the candidate based on this conversation.
"""
}


assessment_messages = [
    assessment_system_prompt,
    assessment_user_prompt
]


response = client.chat.completions.create(
    model=model,
    messages=assessment_messages,
    response_format={
        "type": "json_object"
    }
)


# --------------------------------------------------
# PARSE ASSESSMENT
# --------------------------------------------------

raw_assessment = response.choices[0].message.content

import json

assessment_data = json.loads(raw_assessment)

assessment = Assessment(**assessment_data)


# --------------------------------------------------
# DISPLAY FINAL ASSESSMENT
# --------------------------------------------------

print("\n")
print("================================")
print("       FINAL ASSESSMENT")
print("================================")

print(f"Overall Score: {assessment.score}/100")
print(f"DSA Score: {assessment.dsa_score}/100")
print(f"Problem Solving: {assessment.problem_solving_score}/100")
print(f"Technical Knowledge: {assessment.technical_score}/100")
print(f"Communication: {assessment.communication_score}/100")

print("\nStrengths:")

for strength in assessment.strengths:
    print("-", strength)

print("\nWeaknesses:")

for weakness in assessment.weaknesses:
    print("-", weakness)

print("\nVerdict:")
print(assessment.verdict)

print("\nRecommendation:")
print(assessment.recommendation)