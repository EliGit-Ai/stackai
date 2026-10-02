# StackAI RAG Evaluation

ערכת בדיקה של 20 שאלות עבור ה־RAG.

הקבצים כוללים:
- Expected Top-1 chunk
- Acceptable chunks
- Expected category
- Required answer content
- Failure criteria
- Manual Retrieval / Answer scoring

## יעדי קבלה

- Retrieval Pass ≥ 85%
- Answer Pass ≥ 85%
- No-answer / Negative: 100% ללא Hallucination

הרץ מחדש Evaluation לאחר שינוי משמעותי ב־Chunking, Metadata, Embeddings, Top-K, Retrieval logic או System Prompt.