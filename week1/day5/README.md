# Day 5 — Resume Evaluator

## Overview

Built a mini AI-powered resume evaluator that compares candidate resumes against a given job description.

The project combines:

- PDF and DOCX resume parsing
- Pydantic structured schemas
- LLM-based information extraction
- LLM-based candidate matching
- Match scoring and reasoning
- Multiple candidate evaluation and ranking

---

## Project Workflow

```text
Job Description
       ↓
LLM + Pydantic Schema
       ↓
Structured Job Data
       ↓
                ┌──────────────────┐
Resume PDF ────►│                  │
Resume DOCX ───►│ Text Extraction  │
                │                  │
                └────────┬─────────┘
                         ↓
                 Resume Text
                         ↓
                  LLM + Pydantic
                         ↓
                Structured Resume
                         ↓
             Job + Resume Comparison
                         ↓
                MatchResult
                         ↓
              Score + Reasoning
                         ↓
                Candidate Ranking