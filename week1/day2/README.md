# Day 2 - System Role & Temperature

## Objective

Learn how to control the behavior of an LLM using:
- System Role
- Temperature

## What I Learned

### System Role

- Defines the assistant's personality and behavior.
- Acts as instructions that the model follows throughout the conversation.
- Examples:
  - Helpful tutor
  - Strict interviewer
  - Python mentor
  - Travel assistant

### Temperature

Controls randomness in the model's response.

| Temperature | Behavior |
|-------------|----------|
| 0.0 | Very deterministic |
| 0.3 | Mostly consistent |
| 0.7 | Balanced |
| 1.0 | More creative |
| 1.5+ | Highly random |

## Code Changes

- Added a system message.
- Experimented with different temperature values.
- Compared outputs for the same prompt.

## Key Takeaways

- System role changes *how* the model answers.
- Temperature changes *how creative* the answer becomes.
- Both parameters are essential for building AI applications.