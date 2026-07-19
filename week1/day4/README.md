# Week 1 - Day 4: Structured Outputs with Pydantic

## Objective

Learn how to extract structured information from natural language using Groq, JSON responses, and Pydantic validation.

---

## Concepts Learned

### 1. Structured Outputs

Instead of asking an LLM for plain text, we can instruct it to return structured JSON.

This makes AI responses easier to process programmatically.

---

### 2. Pydantic Models

Created a `Ticket` model to define the expected data structure.

```python
class Ticket(BaseModel):
    name: str
    email: str
    issue: str
```

Pydantic validates the extracted data and converts it into a Python object.

---

### 3. JSON Schema

Generated a JSON schema directly from the Pydantic model.

```python
schema = Ticket.model_json_schema()
```

The schema was included in the system prompt so the model understood the required output format.

---

### 4. JSON Parsing

Converted the model's JSON response into a Python dictionary using:

```python
json.loads()
```

Then validated it using:

```python
Ticket(**data)
```

---

## Implementation

The application:

- Loads the Groq API key from a `.env` file.
- Creates a Pydantic model.
- Generates a JSON schema.
- Sends a customer ticket to the LLM.
- Receives structured JSON.
- Validates the response.
- Prints the extracted information.

---

## Experiments

I experimented with:

- Different customer tickets
- Different temperatures
- Missing fields
- Extra information not defined in the schema

### Observations

- Lower temperatures produced more consistent JSON.
- The model ignored fields not defined in the schema.
- Pydantic simplified validation and data access.

---

## Key Takeaways

- Structured outputs are much easier to integrate into software.
- JSON schemas guide the LLM toward predictable responses.
- Pydantic validates AI-generated data before it is used.
- Low temperature is better for extraction tasks.

---

## Files

```
day4/
│
├── structured_output.py
├── README.md
├── pyproject.toml
├── uv.lock
└── .env (ignored)
```

---

## Next Steps

- Learn tool calling.
- Learn function calling.
- Build multi-step AI workflows.