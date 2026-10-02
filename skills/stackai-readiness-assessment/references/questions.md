# StackAI Readiness — Adaptive Question Bank

Use these questions adaptively. Do not ask them all mechanically.

## 1. Development model

Primary:
- מי מטפל כיום בפיתוח או בתחזוקת המערכות שלכם — עובד פנימי, פרילנסר, חברת פיתוח חיצונית, או שאין כרגע גורם קבוע?

If external:
- האם ה־GitHub / GitLab / Repository נמצא בבעלות העסק או בבעלות הספק?
- האם העסק יכול לקבל את הקוד, היסטוריית Git, תיעוד Deployment והגישה לחשבונות ללא תלות בספק?

## 2. Business objective

Primary:
- מה היית רוצה ש־Claude Code יעזור לכם לעשות קודם?

If unclear:
- האם הצורך קרוב יותר להבנת מערכת קיימת, Code Review לספק, תיקון באגים, שינויים קטנים, תיעוד או אוטומציה?

## 3. System and source-code availability

- באיזו מערכת או פרויקט תרצו להתחיל?
- האם קוד המקור נמצא ב־Repository מסודר?
- האם לעסק יש גישה אליו?

## 4. Ownership

- מי הבעלים של ה־Repository?
- מי הבעלים של Hosting / Cloud / Domain / Database / CI-CD?
- האם קיימת רשימת נכסים וחשבונות?

## 5. Development/Test and rollback

- האם קיימת סביבת Development או Test נפרדת מ־Production?
- אם שינוי משתבש, האם קיימת דרך ברורה לחזור לגרסה קודמת?
- האם משתמשים ב־Branches / Pull Requests או משנים ישירות Production?

## 6. Internal owner

- מי יהיה האדם בתוך העסק שאחראי על Claude Code?
- האם אותו אדם יכול לאשר גישה, להבין את מטרת ה־Pilot ולקבל החלטות מול הספק?

## 7. Permissions and credentials

- מי מחזיק כיום בהרשאות ל־Repository, Hosting, Cloud, Database ו־Production?
- האם משתמשים בחשבונות אישיים או בחשבונות ארגוניים?
- האם קיימים Shared Admin Credentials?

## 8. Security

Primary:
- האם המערכת מכילה מידע רגיש — לקוחות, מידע כספי, מידע רפואי, Secrets או מידע עסקי רגיש?

If yes:
- האם ידוע מי רשאי לגשת למידע?
- האם Secrets ו־Credentials נשמרים בנפרד מהקוד?
- האם קיימת סביבת Test עם מידע שאינו Production?

## 9. Ongoing support

- מי יטפל בהרשאות, עדכונים, תקלות ושינויים לאחר ההטמעה?
- האם יש תהליך מסודר ל־Onboarding ו־Offboarding?

## Stop rule

Stop asking questions once all eight scoring dimensions have enough evidence.

Typical conversation length: 8–15 questions.