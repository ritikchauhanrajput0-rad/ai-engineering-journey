# Week 1 - Day 1
## Topic
Introduction to LLM APIs using Groq

---

## Objective

Learn how to connect a Python application with a Large Language Model (LLM) using the Groq API and understand the components involved in an API request.

---

## Technologies Used

- Python
- uv
- Groq SDK
- python-dotenv

---

## What I Built

A simple Python application that:

- Loads the API key from a `.env` file
- Creates a Groq client
- Sends a prompt to the Llama 3.3 70B model
- Prints the generated response

---

## Project Structure

```
day1/
│── hello_llm.py
│── README.md
│── pyproject.toml
│── .python-version
```

---

## Core Components of an LLM API Call

| Component | Description |
|-----------|-------------|
| API Key | Authentication token used to securely access the API. |
| Client | Object responsible for communicating with the LLM service. |
| Model | Specifies which AI model should generate the response. |
| Messages | List of conversation messages sent to the model. |
| Role | Identifies whether the message is from the user, assistant, or system. |
| Content | The actual prompt or response text. |
| Response | Object returned by the API containing generated text and metadata. |
| Tokens | Units of text used by the model for processing and billing. |

---

## Key Learnings

### 1. API Keys

- API keys should never be hardcoded.
- Store them securely inside a `.env` file.
- Add `.env` to `.gitignore`.

---

### 2. Virtual Environments

Virtual environments isolate project dependencies and prevent package conflicts between different Python projects.

---

### 3. LLM Request Structure

An LLM request contains:

- Model
- Messages
- Roles
- Content

The model generates a response based on these inputs.

---

### 4. Roles

- **system** → Defines assistant behavior.
- **user** → User's prompt.
- **assistant** → Previous model responses.

---

### 5. Response Object

The API returns more than just text.

It also contains:

- Generated answer
- Token usage
- Finish reason
- Model information

---

### 6. Tokens

Tokens represent pieces of text.

They are important because they affect:

- Cost
- Maximum context length
- Model performance

---

## Challenges Faced

- Setting up the API key correctly.
- Understanding how `messages` are structured.
- Managing the virtual environment.
- Loading environment variables using `python-dotenv`.

---

## Future Improvements

- Add streaming responses.
- Experiment with different models.
- Build a multi-turn chatbot.
- Learn prompt engineering techniques.

---

## Outcome

Successfully built my first Python application that communicates with an LLM using the Groq API.