# StackAI Knowledge Base – הוראות ייבוא

## מה יש בחבילה
- `StackAI_Knowledge_Base_208.jsonl` – 208 רשומות. כל שורה היא אובייקט JSON עצמאי.
- `StackAI_Knowledge_Base_208.md` – גרסה קריאה לבקרה ותחזוקה.
- `StackAI_Knowledge_Base_208.csv` – גרסה שטוחה שנוחה ל-Sheets/Excel/n8n.

## מבנה רשומה
```json
{
  "id": "stk_001",
  "title": "...",
  "text": "כותרת\n\nתוכן עצמאי...",
  "metadata": {
    "article_no": 1,
    "article_title": "...",
    "category": "implementation",
    "subcategory": "...",
    "intent": "...",
    "content_type": "...",
    "difficulty": "...",
    "platform": "all",
    "risk_level": "low",
    "audience": "...",
    "source": "StackAI Knowledge Base",
    "source_article": "Article 1",
    "language": "he",
    "last_verified": "2026-10",
    "keywords": ["Claude Code", "StackAI"]
  }
}
```

## שימוש ב-n8n
1. קרא את קובץ ה-JSONL כשורות.
2. בצע Parse JSON לכל שורה.
3. העבר את `text` ל-Document/Embedding pipeline.
4. שמור את `id` כמזהה ה-Record ואת `metadata` כ-Metadata.
5. ב-Pinecone השתמש ב-Namespace נפרד, לדוגמה `stackai-kb-v1`.
6. לפני Upsert מלא, בצע ניסיון עם 5–10 Records ובדוק Retrieval.

## Retrieval מומלץ
- Embedding: השדה `text` (כותרת + גוף).
- Filter אופציונלי: `category`, `intent`, `platform`, `risk_level`.
- אין צורך להטמיע את כל ה-Metadata בתוך הטקסט.
- בשאלות Troubleshooting, ניתן להעדיף `intent=troubleshooting`.
- בשאלה על Windows, ניתן לסנן או להעלות משקל ל-`platform=windows`/`windows-wsl`.

## Versioning
הגרסה הנוכחית כוללת 208 Chunks מתוך 20 מאמרי הליבה.
`last_verified=2026-10` מציין מתי התוכן הטכני נבדק/נבנה.