# StackAI — Project Instructions for Claude Code

## 1. מטרת הפרויקט

StackAI הוא מוצר ושירות ייעוץ להטמעה ארגונית של Claude Code בעסקים קטנים ובינוניים.

המוצר מיועד במיוחד לעסקים:
- ללא צוות פיתוח פנימי.
- שעובדים עם פרילנסרים או חברות פיתוח חיצוניות.
- שרוצים יותר שליטה בקוד, בידע הטכני, בהרשאות ובנכסים הטכנולוגיים.
- שרוצים להשתמש ב-Claude Code בצורה בטוחה, מדורגת ומבוקרת.

StackAI אינו "צ'אטבוט AI כללי".
המיקוד הוא:
**Claude Code implementation, governance, security, readiness, vendor control, RAG support and ongoing operations.**

---

## 2. עקרונות מוצר

פעל תמיד לפי העקרונות הבאים:

1. **Business Problem → Process → Technology**
   - אל תתחיל מיכולת טכנולוגית ותנסה למצוא לה שימוש.
   - התחל מהבעיה העסקית ומהתהליך הקיים.

2. **Least Privilege by default**
   - אל תרחיב הרשאות ללא צורך.
   - אל תניח ש-Production Access נדרש.

3. **Human Approval for sensitive actions**
   - פעולות הרסניות, רגישות או בעלות השפעה על Production דורשות אישור אנושי.

4. **Business ownership**
   - העדף מצב שבו העסק שולט ב-Repository, Cloud, Hosting, Domain, Database, Credentials וחשבונות מרכזיים.
   - ספק חיצוני מקבל הרשאות מתאימות; הוא אינו אמור להיות נקודת הכשל היחידה.

5. **Pilot before scale**
   - התחל קטן, הפיך ומדיד.
   - הרחב רק לאחר אימות.

6. **No hallucinated business facts**
   - אין להמציא מחירים, חבילות, לקוחות, SLA, זמני אספקה או התחייבויות מסחריות שלא קיימים במקור מוסמך.

---

## 3. שפה וסגנון

ברירת המחדל של המוצר היא עברית מלאה ו-RTL.

כאשר עובדים על ממשק משתמש:
- כתוב בעברית טבעית וברורה.
- מונחים טכניים מקובלים כמו Git, MCP, Claude Code, Repository, Production ו-Pilot יכולים להישאר באנגלית.
- אל תעמיס ז'רגון טכני על בעל עסק שאינו מפתח.
- הסבר מושג טכני במשפט קצר כאשר הוא נדרש להבנת הפעולה.
- העדף ניסוח רגוע, סמכותי ומקצועי על פני ניסוח דרמטי.

---

## 4. זהות המוצר והעיצוב

הכיוון העיצובי המאושר הוא:

**Luxury Light / Premium Consulting**

מאפיינים:
- בהיר מאוד.
- לבן / שמנת / אפורים חמים.
- זהב עדין / שמפניה כ-Accent.
- הרבה White Space.
- טיפוגרפיה אלגנטית.
- מראה של חברת ייעוץ פרימיום.
- פחות "Cyber", פחות Neon, פחות Dashboard טכנולוגי.
- ממשק רגוע, נקי ומזמין.

אין להחזיר את האתר לכיוון:
- Dark Cyber.
- Neon.
- Grid טכנולוגי כבד.
- Terminal aesthetic.
- עומס אנימציות.

### גרסת האתר המאושרת

גרסת הבסיס הנוכחית:
`StackAI_Web_App_v4_UX_Polished.html`

כאשר משנים את האתר:
- שמור על הכיוון העיצובי של V4.
- שפר UX מבלי לפגוע ב-RTL.
- שמור Mobile First.
- אל תשבור את מנגנון ה-Polling העתידי.
- אל תסיר את מצב Demo אלא אם החיבור ל-n8n הושלם.

---

## 5. StackAI Advisor

StackAI Advisor הוא היועץ הדיגיטלי של המוצר.

הוא פועל בארבעה מצבים עיקריים:

1. `knowledge`
   - שאלות מקצועיות על Claude Code.

2. `diagnostic`
   - בדיקת מוכנות עסק להטמעה.

3. `troubleshooting`
   - אבחון תקלות Claude Code, Git, MCP, Permissions וכדומה.

4. `commercial`
   - פנייה לשירות, הצעת מחיר, פגישה או המשך ייעוץ.

המשתמש אינו בוחר Mode ידנית.
ה-Agent מזהה את הכוונה.

### כלל RAG

לשאלות מקצועיות בתחום StackAI:
- חפש קודם ב-Knowledge Base.
- השתמש ב-Chunks שנשלפו.
- אל תמציא מידע טכני שלא נתמך במקור.
- אם המידע לא קיים במאגר, אמור זאת במפורש.

---

## 6. Knowledge Base

מאגר הידע המרכזי כולל:

- 20 מאמרי ליבה.
- 208 Semantic Chunks.
- Metadata לכל Chunk.
- גרסת JSONL מוכנה ל-RAG/Pinecone.
- גרסת Markdown/CSV לתחזוקה.

קובץ מקור עיקרי:
`StackAI_Knowledge_Base_208.jsonl`

### מבנה Chunk

כל יחידה צריכה לשמור על מבנה לוגי דומה:

```json
{
  "id": "stk_001",
  "title": "...",
  "content": "...",
  "metadata": {
    "article_no": 1,
    "category": "...",
    "intent": "...",
    "risk": "...",
    "language": "he"
  }
}
```

### כללי Chunking

- אין לבצע Chunking מכני מחדש ללא צורך.
- 208 היחידות כבר נחתכו סמנטית.
- כל Chunk צריך להיות עצמאי.
- אין להשתמש בניסוחים כגון "כפי שנאמר לעיל".
- אין להכניס Boilerplate זהה לכל Chunk.
- Embedding צריך להתבסס על `title + content`.
- Metadata נשמר בנפרד.

---

## 7. RAG ו-Pinecone

ארכיטקטורה מתוכננת:

```text
Website
  ↓
n8n
  ↓
StackAI Advisor
  ↓
Pinecone Vector Search
  ↓
Top relevant chunks
  ↓
LLM response
```

ל-Ingestion:

```text
Knowledge Base
  ↓
Parse records
  ↓
Document per semantic chunk
  ↓
Embeddings
  ↓
Pinecone Vector Store
```

### כלל חשוב

אל תוסיף Text Splitter אוטומטי ל-208 Chunks ללא סיבה מוכחת.

המטרה הראשונית:
**208 semantic documents → approximately 208 vectors.**

---

## 8. RAG Evaluation

קיים סט בדיקות של 20 שאלות.

קובץ:
`StackAI_RAG_Evaluation_20.xlsx`

יעדי קבלה:
- Retrieval Pass: לפחות 85%.
- Answer Pass: לפחות 85%.
- No-answer / negative questions: 100% ללא Hallucination.

כאשר משנים:
- Chunking.
- Metadata.
- Embedding model.
- Retrieval logic.
- Top-K.
- System Prompt.

יש להריץ מחדש את ה-Evaluation.

---

## 9. Readiness Assessment

הערכת המוכנות בודקת 8 ממדים:

1. Business objective
2. System/source-code availability
3. Ownership of technical assets
4. Responsible internal owner
5. Development/Test and rollback
6. Access and permissions governance
7. Security, sensitive data, secrets and credentials
8. Ongoing support and operational ownership

כל ממד מקבל 0–2.

ציון מקסימלי:
`16`

פירוש:
- `13–16` — Ready for a Claude Code pilot.
- `9–12` — Ready after limited preparation.
- `5–8` — Infrastructure and governance preparation required.
- `0–4` — Start with technical and ownership mapping.

### Critical Blockers

הציון אינו גובר על חסם קריטי.

דוגמאות:
- אין גישה אמינה לקוד.
- בעלות על Repository אינה ברורה.
- יש רק Production.
- אין Rollback.
- אין אחראי פנימי.
- Credentials קריטיים נמצאים רק אצל ספק.
- מידע רגיש אינו מנוהל.
- Shared Admin credentials ללא Traceability.

כאשר קיים Blocker:
- ציין אותו בדוח.
- אל תמליץ על Write/Production Pilot לפני טיפול.
- ניתן להמליץ על Read Only, Documentation או Ownership Mapping.

---

## 10. Skill

ה-Skill הרשמי:

`stackai-readiness-assessment`

מבנהו:

```text
stackai-readiness-assessment/
├── SKILL.md
├── README_HE.md
├── references/
│   ├── questions.md
│   ├── scoring.md
│   ├── critical_blockers.md
│   ├── output-schema.json
│   └── example-output.json
├── scripts/
│   └── score_readiness.py
└── tests/
    └── test-cases.md
```

אל תשכפל את לוגיקת הניקוד בקוד נוסף ללא צורך.
אם נדרש חישוב דטרמיניסטי, העדף את:
`scripts/score_readiness.py`

---

## 11. Readiness Report

הדוח הרשמי:
**StackAI Claude Code Readiness Report**

הוא כולל:
- Readiness Score.
- Readiness Status.
- Executive Summary.
- Strengths.
- Gaps.
- Critical Blockers.
- Risks.
- Recommended Use Case.
- Required Preparation.
- Suggested Pilot.
- Prioritized Next Actions.
- Recommended StackAI Action.

קיימים:
- Template.
- Example.
- JSON Schema.

אל תשנה את סולם הניקוד ללא עדכון:
- Skill.
- PRD.
- Report Template.
- Evaluation.
- UI.

---

## 12. אתר StackAI

גרסת הבסיס:
`StackAI_Web_App_v4_UX_Polished.html`

האתר כולל:
- Hero.
- Value proposition.
- StackAI Advisor.
- Quick Actions.
- Readiness Check.
- 8-question demo assessment.
- Readiness Score.
- Demo responses.
- Polling-ready API code.
- Responsive RTL UX.

### API configuration

האתר בנוי לעבוד בשני מצבים:

`USE_MOCK_API = true`
- Demo מקומי.
- אין צורך ב-n8n.

`USE_MOCK_API = false`
- חיבור ל-n8n.

הגדרות מרכזיות:
- `START_ENDPOINT`
- `STATUS_ENDPOINT`
- `POLL_INTERVAL_MS`
- `MAX_POLL_ATTEMPTS`

### Polling contract

Start request:

```http
POST /stackai/start
```

Expected response:

```json
{
  "request_id": "req_123",
  "status": "processing"
}
```

Status:

```http
GET /stackai/status?request_id=req_123
```

Processing:

```json
{
  "status": "processing"
}
```

Completed:

```json
{
  "status": "completed",
  "answer": "..."
}
```

Failed:

```json
{
  "status": "failed",
  "error": "..."
}
```

אל תשנה את ה-Contract בלי לעדכן גם את צד n8n וגם את האתר.

---

## 13. n8n

ה-n8n טרם הושלם.

אל תניח שה-Workflows קיימים בפועל.

Workflows מתוכננים:

### Knowledge ingestion

```text
Manual Trigger
→ file/data source
→ parse records
→ optional batching
→ document loader
→ embeddings
→ Pinecone
```

### Advisor request

```text
Webhook /start
→ create request_id
→ save request state
→ invoke StackAI Advisor
→ RAG / tools
→ save answer
```

### Polling status

```text
Webhook /status
→ lookup request_id
→ return processing/completed/failed
```

### Future diagnostic/report flow

```text
Advisor
→ diagnostic state
→ structured JSON
→ readiness scoring
→ generate report
→ email / lead / consultation
```

---

## 14. אבטחה

אסור להכניס ל-Repository:
- API keys.
- Tokens.
- Passwords.
- Private keys.
- Production credentials.
- Database passwords.
- Real customer secrets.

השתמש ב:
- environment variables.
- secret manager.
- n8n credentials.
- platform-managed secrets.

### Claude Code

אל תשמור Secrets בתוך:
- `CLAUDE.md`
- Skills
- Agent definitions
- Source code
- Git history

`.gitignore` אינו מנגנון הרשאה.

---

## 15. Git ו-GitHub

כל שינוי מהותי צריך להתבצע בענף נפרד.

דפוס עבודה מועדף:

```text
main
  ↓
feature/<short-name>
  ↓
change
  ↓
review
  ↓
merge
```

כללים:
- אל תבצע Force Push ל-main.
- אל תמחק היסטוריה ללא הוראה מפורשת.
- אל תכניס Credentials.
- שמור Commits קטנים וברורים.
- לפני שינוי רחב, בדוק `git status`.
- לפני Commit, בדוק Diff.
- עבור שינויים רגישים, הצג מה הולך להשתנות לפני ביצוע.

---

## 16. קבצי מקור חשובים

כאשר קיימות גרסאות מרובות, העדף את הגרסאות הבאות:

- Website: `StackAI_Web_App_v4_UX_Polished.html`
- PRD: `StackAI_PRD_v1.0.md` / `StackAI_PRD_v1.0.docx`
- Knowledge Base: `StackAI_Knowledge_Base_208.jsonl`
- Evaluation: `StackAI_RAG_Evaluation_20.xlsx`
- Skill: `stackai-readiness-assessment/SKILL.md`
- Readiness Report Schema: `StackAI_Readiness_Report_Data_Schema.json`

גרסאות V1/V2/V3 של האתר הן Reference בלבד ואינן Source of Truth.

---

## 17. כללי שינוי

לפני שינוי:
1. זהה את קובץ המקור הנכון.
2. בדוק האם השינוי משפיע על Schema, UI, Skill או n8n.
3. שמור Backward Compatibility כאשר אפשר.
4. אל תשנה כמה מערכות בו-זמנית אם אין צורך.

אחרי שינוי:
1. ודא שאין שגיאות Syntax.
2. בדוק RTL.
3. בדוק Mobile.
4. בדוק Demo Mode.
5. אם רלוונטי — בדוק Polling contract.
6. אם רלוונטי — הרץ RAG Evaluation.
7. תעד שינוי שמשפיע על Architecture או Product Behavior.

---

## 18. Definition of Done

שינוי נחשב מוכן כאשר:

### UI
- עובד בדסקטופ ובמובייל.
- RTL תקין.
- אין Overflow.
- CTA ברור.
- מצב Loading ברור.
- Keyboard navigation סביר.
- Demo Mode ממשיך לפעול אם n8n אינו מחובר.

### RAG
- אין Chunking לא מתוכנן.
- Metadata נשמר.
- No-answer behavior אינו ממציא מידע.
- Evaluation נשמר מעל סף היעד.

### Diagnostic
- שמונת הממדים נשמרים.
- ציון 0–16 מחושב נכון.
- Blockers מדווחים בנפרד.
- Pilot מתאים לרמת הסיכון.

### Security
- אין Secrets בקוד.
- אין המלצה לא מבוקרת על Production.
- פעולות רגישות כוללות Human Approval.

---

## 19. לא לבצע ללא הוראה מפורשת

אל:
- תשנה את שם המותג StackAI.
- תשנה את סולם Readiness 0–16.
- תחליף את 208 ה-Chunks ב-Chunking חדש.
- תמציא מחירון.
- תיצור לקוחות או Testimonials פיקטיביים.
- תחבר שירות Production אמיתי.
- תשלח מיילים אמיתיים.
- תיצור Leads אמיתיים.
- תבצע Deployment ל-Production.
- תוסיף Production credentials.
- תאפשר Autonomous Production Writes.

---

## 20. מקור האמת העסקי

כאשר קיימת סתירה בין קבצים:

1. החלטה מפורשת חדשה של בעל הפרויקט.
2. ה-PRD המאושר.
3. `CLAUDE.md`.
4. Skill / Schema ספציפי לתהליך.
5. קוד קיים.
6. גרסאות ישנות / דוגמאות.

אין להסיק החלטה עסקית חדשה מתוך קוד ישן בלבד.

---

## 21. סטטוס נוכחי

הושלם:
- Product concept.
- 20 Knowledge Base articles.
- 208 semantic chunks.
- Metadata map.
- JSONL knowledge base.
- RAG evaluation set.
- StackAI Advisor design.
- Readiness assessment logic.
- Readiness report design.
- Premium website V4.
- PRD v1.0.
- `stackai-readiness-assessment` Skill.

טרם הושלם:
- n8n implementation.
- Pinecone ingestion in the live environment.
- Live RAG retrieval tests.
- Automated report generation.
- GitHub repository setup/final structure.
- Final presentation.
- Demo video.

---

## 22. עבודה עתידית

כאשר ממשיכים את הפרויקט, סדר עדיפות מומלץ:

1. Repository structure + GitHub.
2. n8n ingestion workflow.
3. Pinecone live ingestion.
4. RAG retrieval workflow.
5. Website ↔ n8n integration.
6. Diagnostic state handling.
7. Automated Readiness Report.
8. End-to-end testing.
9. Presentation.
10. Demo video.

---

## 23. עקרון אחרון

StackAI מוכרת **יכולת ארגונית**, לא התקנת תוכנה.

כל החלטת מוצר, UX, אבטחה או אוטומציה צריכה לחזק:
- שליטה.
- עצמאות.
- בטיחות.
- שקיפות.
- יכולת תחזוקה.
- ערך עסקי מדיד.