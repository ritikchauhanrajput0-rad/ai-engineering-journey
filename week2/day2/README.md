Key Concepts Learned
ReAct = Reasoning + Acting
Thought → Action → Observation loop
LLMs can decide which tool to use
Python can execute the selected tool
Tool results can be returned to the LLM as observations
Conversation history provides the agent with previous context
Agents can perform multi-step tasks
A maximum loop limit prevents the agent from running indefinitely
The system prompt controls agent behavior
Tool parsing is required to convert the LLM's action into executable Python
Agents are essentially an LLM + tools + control loop


Frameworks such as LangChain and LangGraph provide higher-level abstractions for building agents, but the underlying idea is still similar:



LLM
 ↓
Decision
 ↓
Tool
 ↓
Result
 ↓
LLM
 ↓
Decision
 ↓
...The main lesson from today is:

An AI agent is not simply an LLM that gives an answer. It is an LLM placed inside a loop where it can decide what action to take, use tools, observe their results, and continue until it can produce a final answer.