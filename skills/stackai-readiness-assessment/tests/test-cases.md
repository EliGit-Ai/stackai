# Functional Test Cases

## Test 1 — External vendor, business owns assets

Prompt:
> אנחנו עסק קטן. חברת פיתוח חיצונית מתחזקת את המערכת, אבל ה־GitHub והענן בבעלות שלנו. אני רוצה לדעת אם אנחנו מוכנים ל־Claude Code.

Expected:
- Skill triggers.
- One question at a time.
- External vendor is not treated as an automatic problem.
- Ownership can score high if business control is confirmed.

## Test 2 — Vendor-only repository

Prompt:
> הספק שלנו מחזיק את הקוד אצלו ואין לנו גישה ל־GitHub.

Expected:
- Identify ownership/source-access problem.
- Ask whether code/history/documentation can be obtained.
- Flag critical blocker if business cannot independently access source.
- Recommend ownership mapping / read-only or transition work before write pilot.

## Test 3 — No Test environment

Prompt:
> יש לנו רק Production ואין סביבת בדיקות.

Expected:
- Score Dev/Test & rollback as 0 or 1 depending rollback evidence.
- Do not recommend write-enabled pilot.
- Suggest read-only work or creation of safe environment.

## Test 4 — Sensitive data

Prompt:
> המערכת מכילה מידע פיננסי של לקוחות.

Expected:
- Ask follow-up about access controls and secrets.
- Do not assume security is adequate.
- Least privilege and no broad Production access.

## Test 5 — Strong readiness

Prompt:
> יש לנו GitHub ארגוני בבעלותנו, Dev/Test, PRs, rollback, owner פנימי, הרשאות אישיות, secrets manager ו-Support מסודר. המטרה היא Code Review על ספק חיצוני.

Expected:
- Avoid redundant questioning once evidence covers dimensions.
- Likely score 13–16.
- Recommend a bounded pilot, not unrestricted autonomy.

## Test 6 — Non-technical owner

Prompt:
> אני מנכ"ל ולא מבין Git. האם זה אומר שאנחנו לא מוכנים?

Expected:
- Do not penalize merely for non-technicality.
- Explain that an internal owner does not need to be a developer.
- Assess actual ownership/access/governance instead.

## Test 7 — Unknown information

Prompt:
> אני לא יודע מי מחזיק את ה־Repository.

Expected:
- Keep ownership unknown.
- Ask the minimum question needed.
- Do not fabricate.

## Test 8 — Output request

Prompt:
> תן לי עכשיו את התוצאה גם כ־JSON.

Expected:
- Return human-readable report plus JSON conforming to output-schema.json.
- total_score must equal sum of the eight dimensions.