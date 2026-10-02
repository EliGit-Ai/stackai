# n8n Workflows

התיקייה מיועדת ל־Workflow exports של StackAI.

## 1. Knowledge Ingestion

```text
Manual Trigger
→ Load knowledge-base JSONL
→ Parse records
→ Optional batching
→ Default Data Loader / document mapping
→ Embeddings
→ Pinecone Vector Store
```

כל Chunk סמנטי הוא Document אחד. אין להוסיף Text Splitter אוטומטי כברירת מחדל.

## 2. Advisor Start

```text
Webhook /stackai/start
→ validate input
→ generate request_id
→ persist status=processing
→ invoke StackAI Advisor
→ RAG/tools
→ save answer
→ status=completed
```

Expected initial response:

```json
{
  "request_id": "req_123",
  "status": "processing"
}
```

## 3. Advisor Status

```text
Webhook /stackai/status
→ lookup request_id
→ return processing / completed / failed
```

Completed response:

```json
{
  "status": "completed",
  "answer": "..."
}
```

## 4. Future Diagnostic / Report

```text
Advisor
→ diagnostic state
→ structured JSON
→ readiness score
→ generate report
→ email / lead / consultation
```

כאשר Workflows יהיו מוכנים, שמור כאן את קבצי ה־JSON export שלהם.