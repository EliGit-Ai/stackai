# StackAI

**מומחי הטמעת Claude Code בארגונים**

StackAI הוא פרויקט AI DEV שמדגים מוצר מלא להטמעת Claude Code בעסקים קטנים ובינוניים — במיוחד עסקים ללא צוות פיתוח פנימי שעובדים עם ספקי פיתוח חיצוניים.

המוצר משלב אתר לקוח, StackAI Advisor, מאגר ידע RAG, אבחון מוכנות, Skill ייעודי, Readiness Report ותכנון אינטגרציה ל־n8n + Pinecone.

## הבעיה העסקית

עסקים רבים תלויים בספקי פיתוח חיצוניים ומחזיקים מעט שליטה ישירה בקוד, ב־Repository, ב־Credentials ובידע הטכני. StackAI נועדה לעזור להם להכניס את Claude Code בצורה מבוקרת, להגדיל שקיפות ושליטה ולהתחיל ב־Pilot קטן, בטוח ומדיד.

## מה כבר קיים בפרויקט

- אתר StackAI ב־HTML יחיד, RTL ורספונסיבי.
- StackAI Advisor — אפיון מלא של התנהגות הסוכן.
- Knowledge Base של 20 מאמרי ליבה ו־208 Semantic Chunks.
- JSONL מוכן להזנה ל־Pinecone.
- ערכת RAG Evaluation עם 20 שאלות.
- Readiness Assessment עם ציון 0–16 ו־Critical Blockers.
- Skill מלא: `stackai-readiness-assessment`.
- Readiness Report — Template + Example + JSON Schema.
- PRD מלא.
- `CLAUDE.md` שמגדיר את חוקי העבודה בפרויקט.

## מבנה ה־Repository

```text
StackAI/
├── README.md
├── CLAUDE.md
├── .gitignore
├── .env.example
├── PROJECT_STATUS.md
│
├── website/
│   ├── index.html
│   └── README.md
│
├── knowledge-base/
│   ├── StackAI_Knowledge_Base_208.jsonl
│   ├── StackAI_Knowledge_Base_208.md
│   ├── StackAI_Knowledge_Base_208.csv
│   ├── StackAI_Chunking_Map.xlsx
│   └── README.md
│
├── evaluation/
│   ├── StackAI_RAG_Evaluation_20.xlsx
│   ├── StackAI_RAG_Evaluation_20.csv
│   └── README.md
│
├── skills/
│   └── stackai-readiness-assessment/
│
├── docs/
│   ├── PRD.md
│   ├── StackAI_PRD_v1.0.pdf
│   ├── StackAI_PRD_v1.0.docx
│   ├── architecture.md
│   └── reports/
│
├── n8n/
│   ├── README.md
│   └── workflows/
│
├── presentation/
└── demo/
```

## הפעלת האתר המקומי

האתר כרגע עובד גם ללא n8n באמצעות Demo Mode.

1. פתח את `website/index.html` בדפדפן.
2. בצע בדיקת מוכנות או שאל שאלה ב־StackAI Advisor.
3. כל עוד `USE_MOCK_API = true`, התשובות מופקות מקומית לצורך הדגמה.

כאשר מחברים את n8n:

```javascript
USE_MOCK_API: false
```

ויש להגדיר:

- `START_ENDPOINT`
- `STATUS_ENDPOINT`

## RAG

מאגר הידע כבר חתוך ל־208 Semantic Chunks. אין לבצע Text Splitter נוסף כברירת מחדל.

זרימת ה־Ingestion המתוכננת:

```text
Knowledge Base
→ Parse records
→ Document per chunk
→ Embeddings
→ Pinecone
```

יעד ראשוני: כ־208 Documents / Vectors.

## StackAI Advisor

הסוכן פועל בארבעה מצבים:

- `knowledge`
- `diagnostic`
- `troubleshooting`
- `commercial`

לשאלות מקצועיות הוא אמור להשתמש ב־RAG לפני תשובה. כאשר המידע אינו קיים במאגר, עליו לומר זאת ולא להמציא מידע.

## Readiness Assessment

הערכת המוכנות בודקת 8 ממדים, כל אחד בציון 0–2.

- 13–16 — מוכן ל־Pilot.
- 9–12 — מוכן לאחר מספר הכנות.
- 5–8 — נדרשת הכנת תשתיות ו־Governance.
- 0–4 — מתחילים במיפוי.

Critical Blockers נבדקים בנפרד מהציון.

## Skill

ה־Skill נמצא תחת:

```text
skills/stackai-readiness-assessment/
```

הוא כולל:
- `SKILL.md`
- בנק שאלות.
- Rubric לניקוד.
- Critical Blockers.
- JSON Schema.
- דוגמת Output.
- Script לחישוב ציון.
- Test Cases.

## אבטחה

אין להכניס ל־Repository:

- API Keys
- Tokens
- Passwords
- Private Keys
- Production Credentials
- Database Passwords
- מידע לקוחות אמיתי

השתמש ב־Environment Variables, n8n Credentials או Secret Manager.

## מסמכי Source of Truth

- אתר: `website/index.html`
- PRD: `docs/PRD.md`
- Knowledge Base: `knowledge-base/StackAI_Knowledge_Base_208.jsonl`
- Evaluation: `evaluation/StackAI_RAG_Evaluation_20.xlsx`
- Skill: `skills/stackai-readiness-assessment/SKILL.md`
- חוקי עבודה: `CLAUDE.md`

## סטטוס

הפרויקט נמצא בשלב **Prototype / Integration Ready**.

החלקים שעדיין מיועדים להשלמה:

- n8n workflows בפועל.
- Pinecone live ingestion.
- Live RAG retrieval tests.
- Website ↔ n8n integration.
- Automated report generation.
- Presentation.
- Demo video.

ראו `PROJECT_STATUS.md` לפרטים.