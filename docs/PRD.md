# StackAI — Product Requirements Document

**גרסה:** 1.0  
**תאריך:** 01.10.2026  
**מוצר:** StackAI Advisor + Claude Code Readiness Platform

## 1. תקציר מנהלים
StackAI הוא מוצר ושירות ייעוץ להטמעת Claude Code בעסקים קטנים ובינוניים, במיוחד בארגונים ללא צוות פיתוח פנימי העובדים עם ספקים חיצוניים. המוצר משלב Knowledge Base מבוסס RAG, סוכן StackAI Advisor, אבחון מוכנות, Readiness Report ואתר לקוח עם Polling.

## 2. הבעיה העסקית
- תלות בספקי פיתוח חיצוניים.
- בעלות חלקית על Repository, Cloud, Credentials ותיעוד.
- קושי לבצע Code Review או להבין מערכת באופן עצמאי.
- חשש מהכנסת AI ללא Security/Governance.
- שימוש נקודתי ב-AI ללא Pilot מדיד ותהליך הטמעה.

## 3. מטרות
- אבחון מוכנות 0–16 + Critical Blockers.
- Q&A מקצועי מבוסס 208 Chunks.
- Troubleshooting ממוקד.
- Pilot Recommendation.
- מעבר טבעי ל-Lead/Consultation.

## 4. קהל יעד
SMB, בעלי עסקים, מנהלי תפעול/IT, מנהלי IT וספקי פיתוח חיצוניים.

## 5. מצבי StackAI Advisor
1. Knowledge
2. Diagnostic
3. Troubleshooting
4. Commercial

## 6. RAG
- 20 מאמרי ליבה.
- 208 Chunks סמנטיים.
- `title + content` ל-Embeddings.
- Metadata נפרד: category, intent, platform, risk, audience, source_article, last_verified.
- Top 3–5 Retrieval.
- No-answer policy במקרה שאין מידע מספק.

## 7. Readiness Diagnostic
8 ממדים, כל אחד 0–2: מטרה עסקית, זמינות קוד, בעלות, אחראי פנימי, Dev/Test+Rollback, הרשאות, אבטחה, תמיכה.

**פירוש ציון:**
- 13–16: מוכן לפיילוט.
- 9–12: מוכן לאחר מספר הכנות.
- 5–8: נדרשת הכנת תשתיות ו-Governance.
- 0–4: מתחילים במיפוי.

Critical Blockers נבדקים בנפרד מהציון.

## 8. Frontend
- RTL, Responsive, Premium Advisory UX.
- CTA ראשי: בדיקת מוכנות.
- StackAI Advisor Chat.
- Quick Actions.
- Diagnostic Modal.
- Polling-ready.

## 9. Architecture
`Browser → POST /start → n8n → StackAI Advisor → Pinecone / Tools → Store Result → GET /status → Browser`

## 10. מדדי איכות
- Retrieval Pass ≥ 85%.
- Answer Pass ≥ 85%.
- No-answer Accuracy = 100% בבדיקות ייעודיות.

## 11. סטטוס
- Knowledge Base: הושלם.
- Evaluation: הושלם.
- Advisor: מתוכנן.
- Diagnostic: מתוכנן + UI.
- Report: Template הושלם.
- Frontend: V4 הושלם.
- n8n/Pinecone Integration: ממתין.
- Presentation / Demo / Skill / CLAUDE.md: ממתינים.