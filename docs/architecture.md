# StackAI — Architecture

## High-level

```text
User
  ↓
StackAI Website
  ↓
POST /start
  ↓
n8n
  ↓
StackAI Advisor
  ├── Pinecone RAG
  ├── Readiness Skill
  └── Future tools: report / lead / calendar
  ↓
Request State
  ↑
GET /status
  ↑
Website Polling
```

## Knowledge ingestion

```text
208 semantic chunks
→ parse
→ embeddings
→ Pinecone
```

## Core design decisions

1. Semantic chunking is performed before ingestion.
2. No automatic secondary text splitting by default.
3. RAG is primary for StackAI technical questions.
4. No-answer cases must not be hallucinated.
5. Diagnostic score is 0–16 with separate Critical Blockers.
6. Production write access is not a default pilot condition.
7. Human approval remains part of sensitive change control.