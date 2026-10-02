# StackAI Readiness Assessment Skill

זהו Skill מוכן להתקנה עבור Claude / Claude Code.

## מה הוא עושה

ה־Skill מנהל אבחון שיחתי של מוכנות עסק להטמעת Claude Code:

- שואל שאלה אחת בכל פעם
- מתאים את השאלות לתשובות המשתמש
- מדרג 8 ממדי מוכנות
- מחשב ציון 0–16
- מזהה Critical Blockers
- ממליץ על Pilot ראשון
- מפיק StackAI Claude Code Readiness Report
- יכול להחזיר גם JSON מובנה

## מבנה

- `SKILL.md` — הוראות הליבה
- `references/questions.md` — בנק שאלות דינמי
- `references/scoring.md` — כללי הניקוד
- `references/critical_blockers.md` — חסמים קריטיים
- `references/output-schema.json` — Schema לפלט מובנה
- `references/example-output.json` — דוגמה
- `scripts/score_readiness.py` — אימות וחישוב דטרמיניסטי
- `tests/test-cases.md` — בדיקות פונקציונליות

## התקנה ב-Claude Code

העתק את התיקייה `stackai-readiness-assessment` אל:

macOS / Linux:
`~/.claude/skills/stackai-readiness-assessment`

Windows:
`%USERPROFILE%\.claude\skills\stackai-readiness-assessment`

לאחר מכן פתח Session חדש של Claude Code.

## משפטי בדיקה

- "האם העסק שלי מוכן ל-Claude Code?"
- "תעשה לי בדיקת מוכנות להטמעת Claude Code."
- "יש לנו חברת פיתוח חיצונית. איך כדאי להתחיל Pilot?"
- "אני רוצה לבדוק אם יש לנו חסמים לפני התקנת Claude Code."

## בדיקת הסקריפט

דוגמה:

`python scripts/score_readiness.py references/example-output.json`

התוצאה צריכה להחזיר `total_score: 12` ו־`ready_after_limited_preparation`.