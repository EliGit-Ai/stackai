# StackAI Knowledge Base — 208 Semantic Chunks

מאגר ידע מוכן ל-RAG/Pinecone. כל יחידה עצמאית ומכילה כותרת, תוכן ו-Metadata.


---

# מאמר 1: Claude Code לעסק קטן ובינוני – מה זה, מה הוא יודע לעשות ואיפה הוא נותן ערך

## stk_001 — מהו Claude Code ולמה הוא רלוונטי לעסק קטן ובינוני

Claude Code הוא כלי Agentic AI של Anthropic שעובד מתוך סביבת הפרויקט ויכול לקרוא קבצים, להבין Codebase, לערוך קוד, להריץ פקודות ולעבוד עם Git וכלים חיצוניים. לעסק קטן ובינוני הערך אינו רק כתיבת קוד: הוא יכול לקצר זמן הבנה, תחזוקה, Debug ותיעוד גם כאשר רוב הפיתוח נעשה בידי ספק חיצוני. StackAI בוחנת את הערך לפי בעיה עסקית מוגדרת ולא לפי עצם קיומו של הכלי.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_002 — Claude Code כ-Agent לעומת צ'אט AI רגיל

צ'אט AI רגיל מקבל טקסט שהמשתמש שולח אליו ומחזיר תשובה. Claude Code פועל בתוך סביבת העבודה: הוא יכול לקרוא קבצים רלוונטיים, לחפש בקוד, להציע ולבצע שינויים, להריץ בדיקות ולעבוד עם Git בכפוף להרשאות. לכן הוא מתאים יותר לתהליכי פיתוח ותפעול מתמשכים. עם זאת, היכולת לבצע פעולות מחייבת Permissions, Governance ואישור אנושי לפעולות רגישות.

**Metadata:** `category=implementation` · `subcategory=agents` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_003 — עבודה עם Codebase קיים: קריאה, שינוי, Debug ו-Git

Claude Code יכול להיכנס ל-Codebase קיים, למפות מבנה תיקיות, לאתר נקודות כניסה, להבין זרימות נתונים ולסייע ב-Debug לפני שנוגעים בקוד. לאחר מכן ניתן לעבוד ב-Branch ייעודי, לבצע שינוי, להריץ Tests ולבדוק Git diff. StackAI ממליצה להתחיל בחקירה ותכנון, ורק לאחר הבנה לעבור לעריכה. כך השינוי נשאר ניתן לביקורת ול-Rollback.

**Metadata:** `category=implementation` · `subcategory=git` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_004 — CLAUDE.md, MCP, Skills ו-Hooks כמערכת הרחבה של Claude Code

CLAUDE.md מספק ל-Claude הוראות והקשר קבועים על הפרויקט; MCP מחבר אותו למערכות וכלים חיצוניים; Skills הופכים נהלים חוזרים ל-Workflows; Hooks מפעילים בדיקות ואוטומציות סביב אירועים. ארבעת הרכיבים משלימים זה את זה ואינם מחליפים Permissions או Sandbox. בארגון נכון, הם יוצרים שכבת עבודה עקבית במקום להסתמך בכל פעם על Prompt ידני.

**Metadata:** `category=implementation` · `subcategory=mcp` · `intent=implementation` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_005 — הערך של Claude Code בעסק ללא צוות פיתוח פנימי

בעסק ללא צוות פיתוח פנימי, Claude Code יכול לעזור לבעל תפקיד טכני להבין את המערכת, לבדוק עבודת ספק, להכין אפיונים, לתעד, לטפל בשינויים קטנים ולהפיק תמונת מצב על הקוד. המטרה אינה בהכרח להחליף את חברת הפיתוח אלא להפחית חוסר שקיפות ותלות בידע שנמצא רק אצל הספק. העבודה צריכה להישאר בתוך Repository ותהליכים שבשליטת העסק.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_006 — הפחתת תלות בספק פיתוח חיצוני באמצעות Claude Code

תלות בספק פיתוח נוצרת כאשר הקוד, ה-GitHub, ה-Cloud, ה-Secrets והתיעוד נמצאים אצל הספק. Claude Code יכול לסייע להחזיר ידע לארגון באמצעות מיפוי Codebase, יצירת Documentation, CLAUDE.md, Runbooks ו-Skills. אבל קודם צריך לוודא בעלות וגישה לנכסים. StackAI משתמשת ב-Claude ככלי לשיקום עצמאות טכנולוגית, לא כתחליף להסדרה חוזית והרשאתית.

**Metadata:** `category=implementation` · `subcategory=vendor_management` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_007 — עקרון StackAI: מתחילים מהבעיה העסקית ולא מהטכנולוגיה

עקרון StackAI הוא להתחיל מהבעיה העסקית: זמן טיפול ארוך, תלות בספק, חוסר תיעוד, עלויות תחזוקה או קושי בביצוע שינויים. רק לאחר שמוגדר יעד ניתן לבחור כיצד Claude Code משתלב. אם אין Use Case ברור, אין הצדקה להוסיף MCP, Agents או אוטומציות רק משום שהן אפשריות. הצלחה נמדדת בערך עסקי, איכות, סיכון ועלות.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 2: בדיקת מוכנות העסק להטמעת Claude Code – מדריך ושאלון StackAI

## stk_008 — למה לבצע Readiness Assessment לפני התקנת Claude Code

Readiness Assessment מונע מצב שבו מתקינים Claude Code לפני שהעסק מוכן מבחינת בעלות, גישה, נתונים, אבטחה ותהליך עבודה. לפני התקנה StackAI בודקת מי מחזיק את הקוד, האם יש Git, האם קיימת סביבת Test, מי המשתמשים ומהו Use Case הראשון. המטרה היא לזהות פערים מראש ולהחליט אם אפשר להתחיל Pilot או שצריך קודם להכין תשתית.

**Metadata:** `category=implementation` · `subcategory=installation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_009 — הגדרת המטרה העסקית וה-Use Case הראשון

Use Case ראשון צריך לפתור כאב עסקי מוגדר ולהיות קטן מספיק לפיילוט. לדוגמה: הבנת Codebase, טיפול בבאגים קטנים, יצירת Documentation או Code Review. יש להגדיר מדד הצלחה כגון זמן טיפול, שעות ספק או איכות. StackAI נמנעת מפיילוט עמום מסוג 'נראה מה Claude יודע לעשות', משום שקשה למדוד ממנו ערך או להחליט אם להרחיב את ההטמעה.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_010 — בדיקת בעלות על המערכת, הקוד וה-Repository

לפני ההטמעה בודקים מי הבעלים של Source Code, Repository, Cloud, Domain, Database ו-CI/CD. אם הקוד נמצא בחשבון של ספק חיצוני בלבד, זהו סיכון המשכיות עסקית. StackAI מעדיפה שהעסק יחזיק Organization וחשבונות מרכזיים, והספק יקבל גישה מוגבלת לפי צורך. Claude Code אינו פותר בעיית בעלות; הוא דורש אותה כדי לעבוד בצורה ארגונית נכונה.

**Metadata:** `category=implementation` · `subcategory=cost` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_011 — זיהוי המשתמשים, הספק החיצוני והאחראי הפנימי

יש לזהות מי ישתמש ב-Claude Code בפועל, מי מאשר שינויים, מי אחראי על Production ומי הספק החיצוני. גם בעסק קטן צריך Owner פנימי שמבין מי מורשה למה. אם אין אדם שמקבל אחריות על ההטמעה, קשה לנהל Permissions, Offboarding ושינויים. StackAI מגדירה Roles ברורים לפני Pilot ולא משאירה את המערכת תלויה במפתח יחיד.

**Metadata:** `category=implementation` · `subcategory=vendor_management` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_012 — מיפוי רגישות המידע ונתוני הלקוחות

מיפוי מידע בודק איזה תוכן Claude עשוי לראות: Source Code, פרטי לקוחות, מסמכים, PII, מידע פיננסי או נתונים רגישים אחרים. השאלה אינה רק האם המידע קיים, אלא האם הוא נחוץ ל-Use Case. ככל שניתן, משתמשים ב-Test Data, Masking או Read-only access. מידע שאינו נדרש אינו צריך להיכנס ל-Context או להיות נגיש דרך MCP.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_013 — בדיקת Credentials, הרשאות וגישות קיימות

יש למפות Credentials שכבר קיימים במחשב ובכלים: GitHub CLI, SSH, AWS/Azure/GCP, Database, VPN, kubectl, Environment Variables ו-MCP Tokens. Claude אינו צריך לראות את הסוד עצמו כדי להשתמש ב-CLI שכבר מאומת. לכן בדיקת מוכנות כוללת Access Paths קיימים, לא רק קבצי .env. הרשאות רחבות מדי מצומצמות לפני הפיילוט.

**Metadata:** `category=implementation` · `subcategory=security` · `intent=implementation` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_014 — בדיקת סביבת Development, Test ויכולת Rollback

Pilot בריא דורש סביבת Development או לפחות Branch נפרד, Version Control, גיבוי ודרך Rollback. לפני ש-Claude מבצע שינוי צריך לדעת כיצד לבדוק אותו וכיצד להחזיר מצב קודם. אם המערכת חיה רק ב-Production ללא Git או Backup אמין, StackAI תעדיף לטפל קודם בתשתית ולא להתחיל אוטומציה על מערכת שאי אפשר לשחזר בבטחה.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_015 — בדיקת יכולת תמיכה וליווי לאחר ההטמעה

מוכנות אינה רק התקנה. צריך לדעת מי מטפל בבעיה לאחר Go-Live, מי מעדכן Skills ו-CLAUDE.md, מי בודק MCP ו-Permissions ומתי מתקיימת Review תקופתית. StackAI מגדירה Support Owner, תהליך Escalation וליווי חודשי או פנימי. בלי תחזוקה, Configurations נוטים לסטות וההרשאות להתרחב עם הזמן.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_016 — שאלון StackAI: 26 שאלות אבחון בשיחה דינמית

שאלון StackAI בנוי כשיחה דינמית ולא כטופס ארוך שממלאים בלי הקשר. הסוכן שואל שאלה אחת בכל פעם על העסק, המערכת, הבעלות, הספק, הנתונים, המשתמשים, הרשאות, סביבות, Rollback ויעד הפיילוט. תשובות קודמות קובעות מה לשאול הלאה. המטרה היא להפיק תמונת מצב שניתן לתרגם לתוכנית הטמעה ולא רק לציון מספרי.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_017 — StackAI Readiness Score והפקת דוח מוכנות

StackAI Readiness Score מדרג שמונה תחומים: יעד עסקי, גישה למערכת, בעלות על הקוד, משתמש אחראי, סביבת Test, Permissions, Security ותמיכה. כל תחום מקבל 0–2 נקודות, עד 16. 13–16 מתאים בדרך כלל ל-Pilot; 9–12 דורש הכנות; 5–8 מצביע על עבודת תשתית; 0–4 מחייב מיפוי בסיסי. הציון מלווה תמיד בהמלצות ולא מחליף שיקול מקצועי.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 3: כיצד לבחור מודל חשבון, התחברות והרשאות ל-Claude Code בעסק

## stk_018 — העסק צריך לשלוט בחשבון ובסביבת Claude Code

בסביבה עסקית החשבון, ה-Organization וה-Configuration צריכים להיות בשליטת העסק, לא של ספק חיצוני או עובד יחיד. StackAI מעדיפה שכל משתמש יתחבר בזהות משלו ושחשבונות מרכזיים יהיו בבעלות החברה. כך ניתן לבצע Audit, Offboarding ושינוי ספק בלי לאבד שליטה. חשבון Claude הוא חלק מנכסי ה-IT ולא רק כלי אישי של המפתח.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_019 — חשבון עבודה לעומת חשבון אישי

חשבון אישי מתאים לניסוי פרטי, אך בפרויקט עסקי כדאי להפריד בין שימוש אישי לעבודה. הפרדה מצמצמת ערבוב Credentials, Billing ו-Configuration ומאפשרת Offboarding ברור. Claude Code תומך בסביבות קונפיגורציה נפרדות, וניתן להשתמש ב-CLAUDE_CONFIG_DIR כאשר יש צורך להפריד הגדרות. StackAI מתעדת איזה חשבון משמש בכל תחנת עבודה.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_020 — Claude for Teams ו-Enterprise בסביבה עסקית

כאשר יש מספר עובדים, Claude for Teams או Enterprise מאפשרים ניהול ארגוני מרכזי יותר לעומת חשבון אישי. הבחירה תלויה במספר המשתמשים, מדיניות אבטחה, צורך ב-Admin Controls ובמודל החיוב. StackAI אינה מניחה שכל עסק צריך Enterprise; היא בוחרת מסלול שמתאים לגודל, לסיכון ולדרישות ניהול הזהויות.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_021 — Claude Console ומודלי API לעבודה ארגונית

Claude Console מתאים לארגונים שעובדים עם API ומפתחות או צריכים מודל צריכה לפי שימוש. במקרה כזה נדרש ניהול מסודר של API Keys, Projects ו-Billing. אין לשתף Key אחד בין כל העובדים. עדיף זהות נפרדת, Secret Management ויכולת ביטול. StackAI מפרידה בין Authentication של Claude Code לבין Credentials של מערכות עסקיות אחרות.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_022 — Amazon Bedrock, Google Cloud ו-Microsoft Foundry כחלופות תשתית

Claude Code יכול לפעול גם דרך ספקי ענן נתמכים כגון Amazon Bedrock, Google Cloud ו-Microsoft Foundry בהתאם לסביבה ולמדיניות הארגון. מסלול כזה עשוי להתאים כאשר החברה כבר מנהלת Identity, Networking ו-Billing בענן מסוים. הבחירה אינה רק טכנית: צריך לבדוק Governance, אזור, IAM, עלויות ותמיכה לפני החלטה.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_023 — ניהול Credentials ללא שיתוף API Keys בין עובדים

אין להשתמש ב-API Key משותף שמודבק בכל מחשב. Shared Keys מקשים על Audit ועל ביטול גישה כאשר עובד עוזב. StackAI מעדיפה Login אישי או Service Identity ייעודית, Secret Store והרשאות מצומצמות. Credentials אינם נכנסים ל-Git, CLAUDE.md או Skill. אם Key נחשף, מבטלים ומחליפים אותו ולא מסתפקים במחיקתו מהקובץ.

**Metadata:** `category=configuration` · `subcategory=security` · `intent=configuration` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_024 — בדיקת Login, Logout ו-Status ב-Claude Code

לאימות סביבת Login ניתן להשתמש ב-/status כדי לראות את מצב החשבון וה-Configuration. בעת הצורך מבצעים /logout ואז /login מחדש. אם קיימים Environment Variables כמו ANTHROPIC_API_KEY, צריך לבדוק שהם אינם גורמים לשימוש במסלול Authentication אחר מהמתוכנן. StackAI מתעדת את שיטת ההתחברות כחלק מ-Configuration Baseline.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_025 — Offboarding וניהול גישה כאשר עובד או ספק עוזב

Offboarding כולל יותר מניתוק חשבון Claude. יש להסיר GitHub, Cloud, MCP, VPN, SSH, Database ו-Tokens ולבדוק Credentials שהעובד או הספק הכיר. זהות אישית מקלה על ביטול גישה בלי לפגוע בשאר המשתמשים. StackAI שומרת Checklist של כניסה ויציאה כדי למנוע הרשאות שנשארות פעילות לאחר שינוי תפקיד או ספק.

**Metadata:** `category=configuration` · `subcategory=vendor_management` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 4: התקנת Claude Code בעסק – מדריך מלא ל-Windows, macOS ו-Linux

## stk_026 — דרישות מערכת לפני התקנת Claude Code

לפני התקנת Claude Code יש לוודא מערכת הפעלה נתמכת, משאבי מחשב סבירים, Terminal פעיל וגישה לרשת הנדרשת. בעסק יש לבדוק גם Proxy, Firewall, Certificate Inspection ויכולת התחברות לחשבון. StackAI מתעדת את מערכת ההפעלה ושיטת ההתקנה כדי שתמיכה ועדכונים בעתיד יהיו עקביים.

**Metadata:** `category=installation` · `subcategory=installation` · `intent=installation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_027 — התקנת Claude Code ב-Windows באמצעות PowerShell

ב-Windows ניתן להתקין Native דרך PowerShell באמצעות הפקודה הרשמית של Anthropic. לאחר ההתקנה יש לפתוח Terminal חדש ולבדוק `claude --version`. אם הפקודה אינה מזוהה, בודקים את `%USERPROFILE%\.local\bin` ואת PATH. StackAI מעדיפה Native Install כאשר הוא מתאים לסביבה ולא מתקינה מספר גרסאות במקביל.

**Metadata:** `category=installation` · `subcategory=installation` · `intent=installation` · `risk=low` · `platform=windows` · `last_verified=2026-10`

## stk_028 — התקנת Claude Code ב-Windows באמצעות CMD ו-WinGet

ב-Windows ניתן להתקין גם דרך CMD או WinGet. WinGet מתאים במיוחד כאשר ה-IT כבר מנהל תוכנות דרך Package Manager, משום שהעדכון נעשה באמצעות `winget upgrade Anthropic.ClaudeCode`. חשוב לבחור שיטה אחת עיקרית ולהימנע ממצב שבו Native, npm ו-WinGet מתקינים עותקים שונים וה-Terminal מפעיל גרסה לא צפויה.

**Metadata:** `category=installation` · `subcategory=installation` · `intent=installation` · `risk=low` · `platform=windows` · `last_verified=2026-10`

## stk_029 — התקנת Claude Code ב-macOS וב-Linux באמצעות Native Installer

ב-macOS וב-Linux ניתן להשתמש ב-Native Installer הרשמי. לאחר ההתקנה מאמתים את הגרסה ואת מיקום הבינארי ומריצים `claude doctor`. בסביבה ארגונית יש לבדוק גם Proxy, CA ארגוני והרשאות תיקייה. StackAI מתעדת את שיטת ההתקנה ואת Release Channel כחלק מה-Baseline.

**Metadata:** `category=installation` · `subcategory=installation` · `intent=installation` · `risk=low` · `platform=macos-linux` · `last_verified=2026-10`

## stk_030 — התקנת Claude Code באמצעות Homebrew ומנהלי חבילות

Homebrew ומנהלי חבילות של Linux יכולים להתאים לארגונים שכבר מנהלים תוכנות בדרך זו. היתרון הוא Lifecycle מוכר של התקנה ועדכון, אך יש לזכור שעדכונים עוברים דרך מנהל החבילות ולא תמיד דרך מנגנון Native. StackAI בוחרת שיטה שמתיישבת עם ניהול התחנות של הלקוח.

**Metadata:** `category=installation` · `subcategory=installation` · `intent=installation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_031 — התקנת Claude Code באמצעות npm ומתי להשתמש בה

התקנת npm עדיין יכולה להתאים לסביבות מסוימות, אך Native Installer הוא בדרך כלל המסלול המועדף. כאשר משתמשים ב-npm יש לבדוק גרסת Node נתמכת ולהימנע מ-`sudo npm install -g`, שעלול ליצור בעיות הרשאות. חשוב לוודא שאין במקביל Native Claude אחר ב-PATH.

**Metadata:** `category=installation` · `subcategory=installation` · `intent=installation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_032 — אימות ההתקנה באמצעות claude --version ו-claude doctor

לאחר התקנה מריצים `claude --version` כדי לוודא שהפקודה מזוהה ושהגרסה צפויה. לאחר מכן `claude doctor` בודק את סביבת ההתקנה וה-Configuration. ב-StackAI ההתקנה אינה נחשבת מלאה עד ששתי הבדיקות תקינות ונבדקה גם התחברות בתוך Claude באמצעות `/status`.

**Metadata:** `category=installation` · `subcategory=installation` · `intent=installation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_033 — Git for Windows והגדרת Git Bash עבור Claude Code

ב-Windows עבודה עם Git דורשת סביבת Git תקינה. Git for Windows מספק Git Bash וכלי Git נפוצים, ובמקרים מסוימים ניתן להגדיר `CLAUDE_CODE_GIT_BASH_PATH` אם Claude אינו מוצא את Git Bash. לאחר ההתקנה יש לבדוק `git --version`, זהות Git ויכולת לעבוד מול ה-Repository העסקי.

**Metadata:** `category=installation` · `subcategory=git` · `intent=installation` · `risk=low` · `platform=windows` · `last_verified=2026-10`

## stk_034 — Windows Native לעומת WSL2 עבור Claude Code

Windows Native מתאים לעבודה עם כלים ונתיבים של Windows. WSL2 מתאים כאשר הפרויקט מבוסס Linux, משתמש ב-toolchain של Linux או דורש Sandbox נתמך. יש גם שיקולי ביצועים: פרויקט ב-`/home` בתוך WSL לרוב מהיר יותר מפרויקט כבד על `/mnt/c`. StackAI בוחרת סביבת עבודה לפי הפרויקט ולא לפי העדפה כללית.

**Metadata:** `category=installation` · `subcategory=installation` · `intent=installation` · `risk=low` · `platform=windows` · `last_verified=2026-10`

## stk_035 — Login והפעלה ראשונה לאחר ההתקנה

בהפעלה הראשונה מריצים `claude`, משלימים Authentication ובודקים `/status`. לאחר מכן פותחים את הפרויקט מתיקיית ה-Root ומתחילים במשימת קריאה והבנה לפני עריכה. StackAI ממליצה ליצור Branch לפיילוט ולוודא שאין גישה ישירה ל-Production בשלב הראשון.

**Metadata:** `category=installation` · `subcategory=installation` · `intent=installation` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_036 — עדכון Claude Code ובחירת Stable לעומת Latest

Claude Code מתעדכן בקצב גבוה. ניתן להשתמש ב-`claude update` בהתקנה מתאימה, או במנהל החבילות כאשר ההתקנה בוצעה דרך WinGet/Homebrew. בארגון יציב StackAI נוטה להעדיף Stable Channel ולבדוק גרסאות חדשות לפני Rollout רחב. גרסה נוכחית נרשמת בכל Support Ticket.

**Metadata:** `category=installation` · `subcategory=installation` · `intent=installation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_037 — Troubleshooting להתקנה: PATH, Proxy, Firewall והתקנות כפולות

אם ההתקנה נכשלת, בודקים לפי הסדר: האם הבינארי קיים, האם PATH כולל את תיקיית ההתקנה, האם קיימות התקנות כפולות, האם Proxy/Firewall מאפשרים גישה והאם TLS Inspection דורש CA ארגוני. אין להתחיל בהתקנה מחדש לפני שאוספים סימפטום מדויק ומריצים `claude doctor` כאשר אפשר.

**Metadata:** `category=installation` · `subcategory=troubleshooting` · `intent=troubleshooting` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 5: הפעלה ראשונה של Claude Code בעסק – מדריך עבודה בטוח ומבוקר

## stk_038 — Checklist לפני הפעלה ראשונה של Claude Code בפרויקט

לפני Session ראשון בודקים שה-Repository נכון, `git status` נקי או מובן, קיימת דרך Rollback, ויש Branch או סביבת Development. צריך לדעת מי המשתמש, מה Use Case ומה אסור לגעת בו. StackAI אינה מתחילה Session ראשון מול Production או מערכת שאין לה Version Control בלי סיבה מוצדקת.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_039 — יצירת Branch לפיילוט לפני עבודה עם Claude

בפיילוט מומלץ ליצור Branch ייעודי, למשל `git switch -c stackai-pilot`. כך כל שינוי של Claude מופרד מ-main וניתן לראות אותו ב-diff, למחוק אותו או לפתוח ממנו Pull Request. Branch אינו תחליף ל-Backup, אבל הוא שכבת הבקרה הבסיסית לעבודה בטוחה עם קוד.

**Metadata:** `category=configuration` · `subcategory=pilot` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_040 — בדיקת /status והסביבה בתחילת Session

בתחילת Session מריצים `/status` כדי לוודא חשבון, Settings Sources וסביבה צפויים. אם יש Managed Settings, צריך לראות שהם נטענו. במידת הצורך בודקים גם `/permissions` ו-`/mcp`. StackAI משתמשת בבדיקה הזו כחלק מ-Smoke Test לפני שמאפשרים עבודה משמעותית.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_041 — התחלה ב-Read Only והבנת הפרויקט לפני שינוי

הפעולה הראשונה עם Codebase חדש צריכה להיות קריאה: בקש מ-Claude למפות את הפרויקט, להסביר Architecture, לזהות נקודות כניסה ולציין כיצד מריצים Tests. אל תבקש מיד 'תקן הכול'. Read-only exploration מקטין סיכון ומאפשר לזהות הנחות שגויות לפני שהן הופכות לשינויים בקוד.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_042 — Plan Mode לתכנון שינוי בלי לערוך קוד

Plan Mode מאפשר ל-Claude לחקור ולבנות תוכנית בלי להתחיל לערוך את Source Code. הוא מתאים לשינוי מורכב, מערכת לא מוכרת או רכיב רגיש. בקש תוכנית עם קבצים מושפעים, סיכונים ובדיקות. רק לאחר Review של התוכנית עוברים ל-Implementation. Plan Mode אינו מחליף Deny Rules או הפרדת Production.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_043 — יצירת CLAUDE.md ראשוני באמצעות /init ובדיקת /context

`/init` יכול ליצור CLAUDE.md התחלתי על בסיס הפרויקט, אך אין לקבל אותו אוטומטית כמסמך ארגוני סופי. עוברים עליו, מוסיפים Business Rules, Git Workflow וגבולות. `/context` עוזר לוודא אילו Memory Files נטענו בפועל. StackAI מעדיפה CLAUDE.md קצר ומפורש על פני מסמך ארוך שמערבב נהלים, סודות ותיעוד.

**Metadata:** `category=configuration` · `subcategory=claude_md` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_044 — בדיקת /permissions לפני הרחבת האוטונומיה

לפני שמרחיבים אוטונומיה פותחים `/permissions` ובודקים Allow, Ask ו-Deny. בשלב Pilot עדיף שמשימות משמעותיות יבקשו אישור ושפעולות כמו Production, Secrets או Push רגיש יהיו חסומות או מוגבלות. עם הזמן ניתן לאשר פעולות בטוחות שחוזרות על עצמן, אך לא מתוך עייפות מ-Prompts.

**Metadata:** `category=configuration` · `subcategory=permissions` · `intent=configuration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_045 — מודל E-P-I-V של StackAI: Explore, Plan, Implement, Verify

מודל E-P-I-V של StackAI הוא Explore → Plan → Implement → Verify. Explore מבין את המערכת; Plan מגדיר שינוי וסיכון; Implement מבצע בתוך Branch ובגבולות; Verify בודק diff, tests ותוצאה עסקית. המודל נועד למנוע מעבר ישיר מבקשה עמומה לעריכת קוד וליצור Workflow שקל ללמד משתמשים חדשים.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 6: חיבור Claude Code לפרויקט קיים ול-Git/GitHub – מדריך StackAI

## stk_046 — Git כשכבת Audit, היסטוריה ו-Rollback עבור Claude Code

Git הוא שכבת הבקרה המרכזית לעבודה עם Claude Code: הוא מתעד היסטוריה, מאפשר diff, Branches ו-Rollback. לפני שינוי משמעותי צריך לדעת מה מצב ה-Repository, מה השתנה ומי אישר. StackAI משתמשת ב-Git כדי להפוך פעולות של Claude לשקופות וניתנות לביקורת, ולא כתחליף ל-Backup או ל-Review אנושי.

**Metadata:** `category=git_governance` · `subcategory=git` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_047 — בעלות העסק על Repository ו-GitHub Organization

בפרויקט עסקי ה-Repository צריך להיות תחת GitHub Organization שבשליטת העסק ככל שהדבר אפשרי מבחינה חוזית וטכנית. ספק הפיתוח מקבל גישה לפי צורך, אך הבעלות נשארת אצל הלקוח. כך החלפת ספק אינה דורשת העברת נכס מרכזי. StackAI בודקת Organization Owners, Repository Roles ויכולת Offboarding כחלק מההטמעה.

**Metadata:** `category=git_governance` · `subcategory=git` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_048 — בדיקת Git config, clone ו-remote לפני תחילת עבודה

לפני עבודה עם Claude בודקים `git config`, את זהות המשתמש, `git remote -v` ואת ה-Branch הפעיל. אם צריך, מבצעים clone מחשבון העסק ולא מעותק לא ברור במחשב. חשוב לוודא שה-Remote מצביע ל-Repository הרשמי ושאין Credential של ספק או משתמש לשעבר שממשיך לשמש בלי ידיעה.

**Metadata:** `category=git_governance` · `subcategory=git` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_049 — Branch Workflow מומלץ לעבודה עם Claude Code

Workflow מומלץ הוא Branch לכל משימה: יוצרים Branch, נותנים ל-Claude להבין ולבצע, מריצים Tests, בודקים `git diff`, ואז Commit ו-Pull Request. אין לעבוד ישירות על main כברירת מחדל. Branch מאפשר לבודד שינוי ולבצע Review לפני Merge, במיוחד כאשר Claude מבצע מספר פעולות במהירות.

**Metadata:** `category=git_governance` · `subcategory=git_governance` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_050 — הגנה על main באמצעות Pull Requests ו-Review

הגנה על main באמצעות Branch Protection או Rulesets מצמצמת את הסיכון ל-Push ישיר או Merge ללא בדיקות. ניתן לדרוש Pull Request, Review אנושי ו-Status Checks. StackAI מעדיפה שהמדיניות תאכף ב-GitHub ולא רק ב-CLAUDE.md, משום שכלל טכני אמיתי חזק יותר מהנחיה התנהגותית.

**Metadata:** `category=git_governance` · `subcategory=git_governance` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_051 — שימוש ב-GitHub CLI ל-PR ולעבודה עם Claude

GitHub CLI (`gh`) מאפשר ל-Claude לעבוד עם Issues ו-Pull Requests כאשר המשתמש מאומת והרשאות Bash מתאימות. אפשר למשל ליצור PR לאחר בדיקה. יש לבדוק `gh auth status` כי Claude יכול להשתמש בזהות שכבר מחוברת. אם הזהות בעלת Admin, זהו Access Path שצריך להכיר ולצמצם לפי צורך.

**Metadata:** `category=git_governance` · `subcategory=git` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_052 — Git Worktrees לעבודה מקבילית ומבודדת

Git Worktrees מאפשרים לפתוח כמה עצי עבודה של אותו Repository על Branches שונים. זה שימושי כאשר Claude או Agents עובדים במקביל על משימות נפרדות בלי להתנגש בקבצים. כל Worktree צריך Ownership ברור ו-Branch משלו. בסיום העבודה מאחדים דרך Git ו-Pull Requests ולא על ידי העתקת קבצים ידנית.

**Metadata:** `category=git_governance` · `subcategory=git` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_053 — CI/CD, GitHub Actions ורציפות ידע בפרויקט

CI/CD מוסיף שכבת אימות שאינה תלויה רק ב-Claude: Lint, Tests, Security Scan ו-Build יכולים לרוץ על Pull Request. התיעוד ב-README, CLAUDE.md ובתיקיית docs שומר ידע גם כאשר ספק מתחלף. StackAI רואה ב-GitHub Control Plane לפיתוח: הקוד, הבדיקות, הביקורת וההיסטוריה נשארים אצל העסק.

**Metadata:** `category=git_governance` · `subcategory=git` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 7: עבודה עם מתכנת או חברת פיתוח חיצונית באמצעות Claude Code – מודל StackAI

## stk_054 — שלושת גבולות ה-Governance: בעלות, גישה וסמכות

בניהול ספק חיצוני צריך להפריד בין Ownership, Access ו-Authority. העסק צריך להחזיק בנכסים ובהרשאות המרכזיות; הספק מקבל גישה למה שנדרש; והסמכות לפעולות רגישות כמו Merge או Production מוגדרת בנפרד. ערבוב של שלושת הרבדים יוצר תלות וסיכון Offboarding.

**Metadata:** `category=git_governance` · `subcategory=cost` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_055 — Asset Inventory לפני עבודה עם ספק פיתוח חיצוני

לפני הטמעה ממפים נכסים: Repository, Domain, Hosting, Database, Cloud, CI/CD, API Keys, Automation ו-Documentation. לכל נכס מציינים Owner, Admin בפועל ותלות בספק. המיפוי מגלה במהירות מצב שבו ספק מחזיק נכס קריטי שאין לעסק גישה אליו. StackAI משתמשת במפה לתכנון מעבר מבוקר ולא להעברה פזיזה.

**Metadata:** `category=git_governance` · `subcategory=vendor_management` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_056 — בדיקת בעלות חוזית וטכנית על הקוד והמערכות

בעלות טכנית אינה בהכרח בעלות משפטית. גם אם אפשר להעביר Repository, צריך לבדוק חוזים וזכויות בקוד, תשתית ורכיבים צד שלישי. Claude Code אינו משנה זכויות קניין רוחני. StackAI מפרידה בין בדיקה טכנית לבין החלטות חוזיות וממליצה להסדיר את הבעלות לפני מהלך שינוי ספק.

**Metadata:** `category=git_governance` · `subcategory=cost` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_057 — Outside Collaborator ו-Least Privilege לספק חיצוני

GitHub מאפשר לתת לספק Outside Collaborator או Role מתאים ברמת Repository. עקרון Least Privilege אומר שאין לתת Admin אם מספיק Write או Maintain. כך הספק יכול לפתח ולפתוח Pull Requests בלי לשלוט ב-Organization כולו. הרשאה נבדקת מחדש כאשר תפקידו משתנה או כאשר הפרויקט מסתיים.

**Metadata:** `category=git_governance` · `subcategory=vendor_management` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_058 — מדיניות Claude Code והרשאות עבור מפתח חיצוני

גם Claude Code של ספק חיצוני צריך Policy: אילו Repositories מותר לקרוא, האם Push מותר, לאילו MCP Servers יש גישה ומה חסום. אפשר להתחיל ב-Plan/Ask ולהגדיר Deny לפעולות קריטיות. CLAUDE.md לבדו אינו גבול אבטחה; Permissions ו-Managed Settings צריכים לאכוף כללים שלא אמורים להיות ניתנים לעקיפה.

**Metadata:** `category=git_governance` · `subcategory=git_governance` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_059 — Managed Settings ככלי שליטה מול ספקי פיתוח

Managed Settings מאפשרות לארגון להגדיר מדיניות שחלה גם כאשר משתמש או ספק משנה הגדרות מקומיות. ניתן לשלוט ב-Permissions, MCP, Hooks, Login, Models ו-bypass. עבור ספקים חיצוניים זה מאפשר הפרדה בין חופש עבודה בתוך הפרויקט לבין גבולות שאינם נתונים למשא ומתן בכל Session.

**Metadata:** `category=git_governance` · `subcategory=settings` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_060 — תיעוד, Handover והעברת ידע בין ספקים

Handover טוב כולל Architecture, Setup, Build, Tests, Deployment, Rollback, Integrations, Environment Variables, Known Issues ו-Open Work. CLAUDE.md ו-Skills יכולים לשמר נהלים שחיו רק בראש הספק. StackAI בודקת האם מפתח חדש מסוגל להתחיל עבודה מתוך ה-Repository והמסמכים בלי להיות תלוי בשיחת ידע ארוכה.

**Metadata:** `category=git_governance` · `subcategory=vendor_management` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_061 — Offboarding ושירות StackAI Claude Code Vendor Transition

Offboarding כולל הסרת GitHub, Cloud, VPN, Database, MCP, SSH, API Tokens ו-Deploy Keys, לצד Review של Branches ו-PRs פתוחים. StackAI Claude Code Vendor Transition הוא תהליך אפשרי שממפה נכסים, מעביר שליטה, בונה Documentation ו-CLAUDE.md, מסדיר Permissions ומכין כניסה של ספק חדש.

**Metadata:** `category=git_governance` · `subcategory=vendor_management` · `intent=governance` · `risk=medium` · `platform=all` · `last_verified=2026-10`


---

# מאמר 8: CLAUDE.md ארגוני – איך מלמדים את Claude Code את העסק, הפרויקט וכללי העבודה

## stk_062 — מהו CLAUDE.md ומה תפקידו בארגון

CLAUDE.md הוא קובץ הוראות והקשר ש-Claude Code קורא כדי להבין כיצד לעבוד בפרויקט. הוא מתאים ל-Architecture קצרה, Commands, Git Workflow, Business Rules וכללי עבודה קבועים. המטרה היא להוציא ידע מהראש של מפתח יחיד ולהפוך אותו לזיכרון ארגוני בתוך ה-Repository.

**Metadata:** `category=configuration` · `subcategory=claude_md` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_063 — CLAUDE.md כהנחיה ולא כגבול אבטחה

CLAUDE.md הוא Guidance ולא Security Boundary. אפשר לכתוב 'אל תבצע push ל-main', אבל אכיפה אמיתית צריכה להיות ב-Permissions, Managed Settings, GitHub Rulesets, Sandbox או Hooks. StackAI משתמשת ב-CLAUDE.md כדי לכוון התנהגות ובכלים טכניים כדי למנוע פעולות שאסור שיתרחשו.

**Metadata:** `category=configuration` · `subcategory=security` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_064 — Scopes של CLAUDE.md: Managed, User, Project ו-Local

CLAUDE.md יכול להופיע ברמות שונות: Managed ברמת הארגון, User, Project ו-Local. הבחירה קובעת מי מקבל את ההוראה והאם היא משותפת ב-Git. הוראות קריטיות לכלל הארגון מתאימות לרמה מנוהלת; ידע פרויקטלי מתאים ל-Repository; התאמות אישיות או זמניות נשמרות Local.

**Metadata:** `category=configuration` · `subcategory=claude_md` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_065 — יצירת CLAUDE.md באמצעות /init ובדיקתו עם /context

`/init` יכול ליצור CLAUDE.md התחלתי על בסיס Codebase, ולאחר מכן צריך לבצע Review ידני. `/context` מציג אילו Memory Files נטענו בפועל. אם הוראה אינה משפיעה, קודם בודקים טעינה ורק אחר כך ניסוח. StackAI אינה מקבלת קובץ שנוצר אוטומטית כמסמך Governance בלי התאמה לעסק.

**Metadata:** `category=configuration` · `subcategory=claude_md` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_066 — מבנה מומלץ ל-CLAUDE.md ארגוני

מבנה מומלץ כולל: Overview, Architecture, Commands, Tests, Git Workflow, Security, Protected Areas, Business Rules, Documentation ו-Definition of Done. אין להכניס סודות, מפתחות או סיסמאות. כאשר Procedure ארוך, עדיף להעביר אותו ל-Skill ולהשאיר ב-CLAUDE.md רק את ההפניה והעיקרון.

**Metadata:** `category=configuration` · `subcategory=claude_md` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_067 — כתיבת הוראות קצרות, מפורשות וניתנות לבדיקה

הוראות טובות הן קצרות, מפורשות וניתנות לבדיקה. 'כתוב קוד טוב' חלש; 'הרץ npm test לפני Commit' חזק יותר. יש להימנע מסתירות ומהוראות שחוזרות בכמה מקומות. StackAI מעדיפה מסמך ממוקד, משום ש-Context עמוס מקשה על המודל לזהות מה באמת חשוב.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_068 — שימוש ב-.claude/rules לכללים מודולריים ותלויי נתיב

`.claude/rules/` מאפשר לפצל כללים לפי נושא או Paths. לדוגמה, כללי Database יכולים לחול רק על `db/**` או `migrations/**`. זה שומר על CLAUDE.md קצר ומפחית חשיפה של הוראות לא רלוונטיות. כללים מודולריים צריכים עדיין להיות מתועדים ולעבור Review כמו קוד.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_069 — Auto Memory לעומת הוראות ארגוניות מפורשות

Auto Memory יכול לשמר תובנות שנלמדו במהלך עבודה, אך אינו תחליף למדיניות מפורשת. הוראות קריטיות, Security Rules ו-Business Rules צריכים להיכתב באופן יזום ב-CLAUDE.md או Rules. StackAI אינה מסתמכת על זיכרון אוטומטי כדי לשמור ידע שאסור שייעלם או ישתנה ללא Review.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_070 — תחזוקה, Audit ועדכון CLAUDE.md לאורך זמן

CLAUDE.md צריך לעבור תחזוקה כאשר Architecture, Commands, ספקים או Business Rules משתנים. סימן טוב לעדכון הוא טעות שחוזרת שוב ושוב. שינויים משמעותיים במסמך משותף צריכים לעבור Git Review. במסמך מיושן Claude עלול לפעול לפי מידע שהיה נכון בעבר ולכן תחזוקה היא חלק מ-Operations.

**Metadata:** `category=configuration` · `subcategory=claude_md` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 9: settings.json ו-Managed Settings – שליטה ארגונית ב-Claude Code

## stk_071 — Scopes של settings.json: User, Project, Local ו-Managed

Claude Code קורא Settings ממספר Scopes: User, Project, Project Local ו-Managed. User מתאים להעדפות אישיות; Project משותף לצוות; Local להתאמה אישית שאינה נכנסת ל-Git; Managed למדיניות ארגונית. StackAI מתעדת מה שייך לכל Scope כדי למנוע ערבוב בין העדפה פרטית לבין Policy.

**Metadata:** `category=configuration` · `subcategory=settings` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_072 — סדר קדימות של Settings ב-Claude Code

בסדר הקדימות המרכזי Managed גובר על Command Line, אחריו Project Local, Project ואז User, עם חריגים מסוימים שבהם כללי אבטחה מחמירים מתמזגים. אם שינוי ב-settings.json 'לא עובד', צריך לבדוק מקור בעל קדימות גבוהה יותר. `/status` הוא כלי מרכזי לזיהוי מקורות ההגדרה הפעילים.

**Metadata:** `category=configuration` · `subcategory=settings` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_073 — JSON Schema וכתיבת settings.json תקין

מומלץ להוסיף `$schema` מתאים לקובץ settings.json כדי לקבל Validation ועזרה בעורך. הקובץ חייב להיות JSON תקין: אין Comments או Trailing Commas. Settings Error יכול לגרום לקובץ לא להיטען כמצופה. לפני הפצה ארגונית StackAI בודקת את ה-JSON ומריצה `claude doctor`.

**Metadata:** `category=configuration` · `subcategory=settings` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_074 — שימוש ב-/status ו-/config לאבחון Settings

`/status` עוזר לראות Setting Sources ו-Environment, ו-`/config` משמש לשינוי אפשרויות אישיות מסוימות. ניתן גם להשתמש ב-`--settings` לשינוי זמני בסשן. בעת Troubleshooting מתחילים במקור האפקטיבי ולא רק בקובץ שהמשתמש חושב שהוא ערך.

**Metadata:** `category=configuration` · `subcategory=settings` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_075 — הפצת Managed Settings דרך Admin Console, MDM או קובץ מנוהל

Managed Settings ניתן להפיץ דרך מנגנוני ניהול ארגוניים כגון Admin Console, MDM, Registry או קובץ מנוהל, בהתאם לפלטפורמה ולתוכנית. הן מיועדות לכללים שלא אמורים להיות ניתנים לשינוי מקומי. StackAI משתמשת בהן עבור Security Baseline, MCP Policy, Login, Models ו-Version Governance.

**Metadata:** `category=configuration` · `subcategory=settings` · `intent=configuration` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_076 — ניהול Permissions דרך Settings

Permissions יכולות להיות מוגדרות ב-Settings באמצעות Allow, Ask ו-Deny. כללי Deny חשובים צריכים להיות ברמה מנוהלת כאשר הארגון אינו רוצה שמשתמש יסיר אותם. יש להימנע מ-Wildcards רחבים מדי, במיוחד ב-Bash. המדיניות נבדקת בפועל ולא רק בקריאת JSON.

**Metadata:** `category=configuration` · `subcategory=permissions` · `intent=configuration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_077 — ניהול MCP, Plugins ו-Hooks דרך Settings

Settings יכולים לנהל MCP, Plugins ו-Hooks: אילו Servers מותרים, האם נדרש Managed-only, אילו Hooks פועלים ואילו Plugins זמינים. אלה רכיבים שמרחיבים את יכולת Claude ולכן הם חלק ממדיניות האבטחה. שינוי בהם צריך לעבור Review ו-Test כמו שינוי תשתיתי.

**Metadata:** `category=configuration` · `subcategory=mcp` · `intent=configuration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_078 — כפיית Login, Models וגרסאות מאושרות

ארגון יכול לכפות Login Method, Organization, Models זמינים וטווחי Version. זה מסייע למנוע עבודה עם חשבון אישי, Model לא מאושר או גרסה שאינה תואמת Policy. StackAI מגדירה רק מה שנדרש; Governance יעיל אינו אומר לנעול כל אפשרות ללא סיבה עסקית.

**Metadata:** `category=configuration` · `subcategory=configuration` · `intent=configuration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_079 — Troubleshooting ל-Settings Drift ו-Configuration Baseline

Configuration Drift נוצר כאשר Local Settings, Overrides או שינויים זמניים נשארים לאורך זמן. Troubleshooting כולל `/status`, `claude doctor`, בדיקת JSON ומקורות בעלי קדימות גבוהה יותר. StackAI שומרת Configuration Baseline או Golden Configuration כדי להשוות מצב נוכחי למצב מאושר.

**Metadata:** `category=configuration` · `subcategory=troubleshooting` · `intent=troubleshooting` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 10: Permissions ו-Sandboxing ב-Claude Code – כיצד שולטים במה ש-Claude רשאי לבצע

## stk_080 — Allow, Ask ו-Deny: מודל ההרשאות של Claude Code

Claude Code משתמש בשלושה סוגי Permission Rules: Allow מאפשר פעולה בלי Prompt נוסף, Ask דורש אישור, ו-Deny חוסם. בסדר ההערכה Deny גובר על Ask ו-Allow, ו-Ask גובר על Allow. StackAI משתמשת ב-Allow רק לפעולות בטוחות וחוזרות, ב-Ask לשינוי משמעותי וב-Deny לפעולות שאינן צריכות להיות זמינות.

**Metadata:** `category=permissions_security` · `subcategory=permissions_security` · `intent=security` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_081 — ניהול הרשאות באמצעות /permissions

`/permissions` מציג את כללי ההרשאה הפעילים ואת מקורם. זהו המסך הראשון כאשר Tool מתנהג אחרת מהמצופה. במהלך Pilot בודקים אילו Prompts חוזרים ואילו Rules ניתן לצמצם. StackAI אינה ממליצה ללחוץ 'אל תשאל שוב' בלי להבין איזה כלל נוצר ובאיזה Scope הוא נשמר.

**Metadata:** `category=permissions_security` · `subcategory=permissions` · `intent=security` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_082 — כתיבת Bash Permission Rules מדויקים והימנעות מ-Wildcards רחבים

Bash Permission Rules צריכים להיות מדויקים. `Bash(git status)` מצומצם יותר מ-`Bash(git *)`. Wildcard רחב יכול לאפשר פקודות שלא התכוונו לאשר, ווריאציות של Shell עלולות לעקוף Pattern פשוט. לפעולה קריטית משתמשים ב-Deny ממוקד, Hook או Sandbox לפי הצורך ולא רק ב-Pattern נוח.

**Metadata:** `category=permissions_security` · `subcategory=permissions` · `intent=security` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_083 — חסימת קריאת .env וקבצים רגישים

קבצי `.env`, Private Keys, Credentials וקבצים רגישים אחרים יכולים להיחסם באמצעות Read Deny Rules. `.gitignore` אינו חוסם קריאה על ידי Claude. יש לזהות Paths רגישים בפרויקט ולבדוק בפועל שהגישה נחסמת. אם Claude צריך רק שמות משתנים, עדיף להשתמש ב-`.env.example` ללא ערכי סוד.

**Metadata:** `category=permissions_security` · `subcategory=permissions_security` · `intent=security` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_084 — Default, AcceptEdits ו-Plan Permission Modes

Permission Modes קובעים התנהגות ברירת מחדל. Default/Manual מתאים להתחלה; `acceptEdits` מצמצם Prompts לעריכות קבצים; `plan` מתאים לחקירה ותכנון בלי שינוי Source. StackAI מתחילה בדרך כלל ב-Plan/Manual ומרחיבה רק לאחר שה-Workflow והסיכונים מובנים.

**Metadata:** `category=permissions_security` · `subcategory=permissions` · `intent=security` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_085 — dontAsk ו-Auto Mode באוטומציות

`dontAsk` מתאים לסביבה לא אינטראקטיבית שבה פעולה שלא אושרה מראש צריכה להידחות במקום להמתין למשתמש. Auto Mode, כאשר זמין, יכול להעריך פעולות באמצעות מנגנון נוסף. אף אחד מהם אינו תחליף ל-Deny Rules ברורים ול-Sandbox כאשר פעולה אסורה לחלוטין.

**Metadata:** `category=permissions_security` · `subcategory=permissions_security` · `intent=security` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_086 — bypassPermissions ומתי אסור להשתמש בו

`bypassPermissions` או דילוג על Prompts מעניקים אוטונומיה רחבה ועלולים לאפשר פעולות שהמשתמש היה עוצר ידנית. StackAI אינה משתמשת במצב זה כברירת מחדל במחשב עבודה. אם יש צורך באוטומציה מלאה, עושים זאת בסביבה מבודדת עם Credentials מינימליים, Network מוגבל ו-Audit.

**Metadata:** `category=permissions_security` · `subcategory=permissions` · `intent=security` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_087 — מהו Sandbox ומה ההבדל בינו לבין Permissions

Permissions עונות על השאלה האם Claude רשאי לנסות פעולה; Sandbox מגביל לאן התהליך שהופעל יכול להגיע ברמת Filesystem ו-Network. לדוגמה, גם אם `npm test` מותר, Sandbox יכול למנוע מהתהליך לקרוא תיקיות מחוץ לפרויקט או להתחבר לכל האינטרנט. שתי השכבות משלימות זו את זו.

**Metadata:** `category=permissions_security` · `subcategory=security` · `intent=security` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_088 — Filesystem Isolation בתוך Sandbox

Filesystem Isolation מגביל כתיבה וקריאה של תהליכים בתוך Sandbox לאזורים מוגדרים, כגון Working Directory ונתיבים מאושרים. Additional Directories ניתנים רק אם Use Case דורש. StackAI אינה פותחת את כל הדיסק 'לנוחות', משום שכל נתיב נוסף מרחיב את שטח החשיפה.

**Metadata:** `category=permissions_security` · `subcategory=security` · `intent=security` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_089 — Network Isolation ו-Domain Allowlist

Network Isolation יכול להגביל Domains שאליהם תהליכים מתחברים. אפשר לעבוד עם Allowed Domains ו-Strict Allowlist בהתאם לסביבה. זה חשוב משום שחסימת WebFetch אינה בהכרח חוסמת `curl` דרך Bash. StackAI משתמשת ברשת מצומצמת במיוחד בסביבות שמפעילות Packages, Scripts או תוכן לא מהימן.

**Metadata:** `category=permissions_security` · `subcategory=permissions_security` · `intent=security` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_090 — הגנת Credentials ו-Protected Paths ב-Sandbox

Sandbox יכול לצמצם חשיפת Credential Files ו-Environment Variables ולהגן על Paths מערכתיים. יש לזכור ש-Credentials זמינים גם דרך Tools שכבר מאומתים במערכת. לכן StackAI משלבת Sandbox עם Identity מצומצמת ולא מניחה שהסתרת קובץ יחיד מספיקה.

**Metadata:** `category=permissions_security` · `subcategory=security` · `intent=security` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_091 — StackAI Permission Baseline ו-Verification מעשי

StackAI Baseline לפיילוט כולל בדרך כלל Read, `git status`, `git diff`, Tests ו-Lint ב-Allow; עריכות, Dependencies ו-Write MCP ב-Ask; Secrets, Production ופעולות הרסניות ב-Deny. לאחר ההגדרה מבצעים Verification: פעולה מותרת צריכה לעבוד, פעולה אסורה להיחסם, ופעולת Ask להציג Prompt כצפוי.

**Metadata:** `category=permissions_security` · `subcategory=permissions` · `intent=security` · `risk=medium` · `platform=all` · `last_verified=2026-10`


---

# מאמר 11: MCP לעסקים – חיבור Claude Code למערכות, מידע וכלים ארגוניים

## stk_092 — מהו MCP ולמה הוא חשוב ל-Claude Code בארגון

MCP הוא Model Context Protocol, תקן שמאפשר ל-Claude Code להתחבר למערכות וכלים מחוץ לפרויקט. דרך MCP אפשר לקרוא מידע, להפעיל פעולות ולעבוד עם שירותים כמו CRM, GitHub, Drive או APIs פנימיים. StackAI מחברת מערכת רק כאשר קיים Use Case עסקי ברור, ולא בגלל ש'אפשר לחבר'.

**Metadata:** `category=mcp_integrations` · `subcategory=mcp` · `intent=integration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_093 — MCP Tools, Resources ו-Prompts

MCP Server יכול לחשוף Tools, Resources ו-Prompts. Tools הם פעולות ש-Claude מפעיל; Resources הם מידע שניתן לקרוא; Prompts הם תהליכים מוכנים. StackAI מתעדת כל יכולת לפי מטרה, Input, Output ו-Side Effect. כך ניתן להבדיל בין כלי קריאה בטוח לבין פעולה שמשנה נתון עסקי.

**Metadata:** `category=mcp_integrations` · `subcategory=mcp` · `intent=integration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_094 — Remote MCP לעומת Local MCP

Remote MCP רץ כשירות מרוחק, לרוב דרך HTTP, ומתאים לשירות משותף, API מרכזי או מספר משתמשים. Local MCP רץ כתהליך מקומי, לרוב דרך stdio, ומתאים ל-Script פנימי, Pilot או גישה למערכת מקומית. הבחירה מושפעת מאבטחה, תחזוקה, רשת ומודל Authentication.

**Metadata:** `category=mcp_integrations` · `subcategory=mcp` · `intent=integration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_095 — הוספת Remote MCP Server באמצעות HTTP

Remote MCP Server ניתן להוסיף באמצעות `claude mcp add --transport http NAME URL`. לאחר מכן בודקים `claude mcp list`, `claude mcp get NAME` ובתוך Claude את `/mcp`. Server מרוחק צריך Authentication ו-TLS מתאימים, ו-StackAI בודקת מי מפעיל אותו ומי אחראי לעדכונים.

**Metadata:** `category=mcp_integrations` · `subcategory=mcp` · `intent=integration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_096 — הוספת Local MCP Server באמצעות stdio

Local MCP Server ניתן להוסיף עם `--transport stdio` ולהפעיל למשל Node או Python script. היתרון הוא Setup מהיר וגישה לכלים מקומיים; החיסרון הוא תלות בתחנת העבודה וב-Dependencies. StackAI מתעדת את Command, הנתיבים וה-Credentials ומעדיפה Absolute Paths כאשר Relative Path עלול להשתנות לפי Working Directory.

**Metadata:** `category=mcp_integrations` · `subcategory=mcp` · `intent=integration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_097 — MCP Scopes וקובץ .mcp.json

MCP יכול להיות מוגדר ב-Scope של Local, Project או User. Project MCP נשמר בדרך כלל ב-`.mcp.json` ויכול להיכנס ל-Git כדי לשתף Configuration, אבל לא Secrets. Server שמגיע מה-Repository דורש Trust/Approval. StackAI בוחרת Scope לפי מי שצריך את החיבור ולא לפי נוחות.

**Metadata:** `category=mcp_integrations` · `subcategory=mcp` · `intent=integration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_098 — Authentication ו-Credentials ב-MCP

Remote MCP עשוי להשתמש ב-OAuth, Token, API Key או Header אחר. Credentials אינם נשמרים ב-`.mcp.json` שנכנס ל-Git. עדיף OAuth או Secret Management עם זהות נפרדת ויכולת Revocation. StackAI בודקת `/mcp` ו-Login Flow ומוודאת שה-Credential מוגבל למינימום ההרשאות.

**Metadata:** `category=mcp_integrations` · `subcategory=security` · `intent=integration` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_099 — MCP Wrapper צר לעומת גישה ישירה ל-SQL או API

לעיתים עדיף לבנות MCP Wrapper שמציע `get_customer` או `get_open_invoices` במקום לתת ל-Claude `execute_sql` או `call_any_api`. Tool צר קל יותר להבין, לאבטח ולבדוק. StackAI מעדיפה ממשק עסקי מוגדר על פני יכולת כללית וחזקה שמרחיבה את הסיכון ואת הסיכוי לטעות.

**Metadata:** `category=mcp_integrations` · `subcategory=mcp` · `intent=integration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_100 — סיווג MCP Tools ל-Read, Write ו-Destructive

כל MCP Tool מסווג כ-Read, Write או Destructive. לדוגמה `search_customer` הוא Read; `create_task` הוא Write; `delete_customer` הוא Destructive. הסיווג קובע Permission ואישור אנושי. Tool הרסני לא חייב להיות חשוף בכלל גם אם ה-API המקורי תומך בו.

**Metadata:** `category=mcp_integrations` · `subcategory=mcp` · `intent=integration` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_101 — Rollout מדורג ל-MCP: Read Only עד Automation

Rollout של MCP נעשה בשלבים: תחילה Read-only, אחר כך פעולות Write בסיכון נמוך, אחר כך Sensitive Write עם Approval, ורק לבסוף Automation אם קיימת הצדקה. תהליך מדורג מאפשר למדוד שימוש ולגלות פערים לפני של-Claude יש יכולת רחבה על מערכת עסקית.

**Metadata:** `category=mcp_integrations` · `subcategory=mcp` · `intent=integration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_102 — אבטחת MCP וסיכון Prompt Injection

MCP שמחזיר תוכן חיצוני חשוף לסיכון Prompt Injection. טקסט שנקרא מ-Ticket, Document או Web אינו הופך להוראה מהימנה. לכן Tool Access צריך להישאר מצומצם גם אם Claude קורא תוכן זדוני. StackAI משלבת Limited Tools, Permissions, Human Approval ו-Network Controls.

**Metadata:** `category=mcp_integrations` · `subcategory=security` · `intent=integration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_103 — Managed MCP ואישור Servers בארגון

בארגון ניתן להגביל אילו MCP Servers מותרים באמצעות Managed Settings ורשימות Allowed/Denied או Managed Servers. המטרה היא למנוע התקנת Server אקראי שמקבל מידע עסקי. Server חדש עובר Review של מקור, Tools, Authentication, Data Access ותחזוקה לפני אישור.

**Metadata:** `category=mcp_integrations` · `subcategory=mcp` · `intent=integration` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_104 — שילוב MCP עם n8n ו-Troubleshooting לחיבורים

MCP יכול להפעיל n8n Workflow במקום לקבל Credentials ישירים לכל המערכות. לדוגמה Tool בשם `create_new_lead` מפעיל Workflow שמעדכן CRM ושולח הודעה. אם החיבור נכשל, בודקים `claude mcp list`, `/mcp`, Authentication, Network, Permissions ו-Logs. StackAI שומרת Runbook לכל Integration.

**Metadata:** `category=mcp_integrations` · `subcategory=troubleshooting` · `intent=troubleshooting` · `risk=medium` · `platform=all` · `last_verified=2026-10`


---

# מאמר 12: Skills ארגוניים ב-Claude Code – הפיכת תהליכי עבודה ליכולות קבועות

## stk_105 — מהו Skill ולמה הוא שימושי בארגון

Skill הוא תהליך עבודה או ידע מקצועי שחוזר על עצמו ו-Claude Code יכול להפעיל לפי צורך. במקום להסביר בכל פעם כיצד לבצע Code Review, אפשר ליצור Skill שמגדיר את השלבים וה-Output. בארגון Skills הופכים Checklists וניסיון של עובדים ליכולת קבועה בתוך הפרויקט.

**Metadata:** `category=automation` · `subcategory=skills` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_106 — CLAUDE.md לעומת Skill: ידע קבוע מול תהליך רב-שלבי

CLAUDE.md מתאים להוראות וידע שצריכים להיות זמינים כמעט תמיד; Skill מתאים ל-Procedure רב-שלבי שנטען כשצריך. אם CLAUDE.md מתחיל להכיל מדריך Release של עשרות שורות, עדיף להעביר אותו ל-Skill. ההפרדה חוסכת Context ושומרת על הוראות הבסיס קצרות.

**Metadata:** `category=automation` · `subcategory=skills` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_107 — מיקומי Skills ברמת User, Project ו-Organization

Skills יכולים להיות ברמת User, Project או Organization, בהתאם למיקום ולאופן ההפצה. Project Skills תחת `.claude/skills/<name>/SKILL.md` מתאימים לנהלים של Repository ויכולים להיכנס ל-Git. StackAI בוחרת Scope לפי מי שצריך את ה-Skill ומי אחראי לתחזוקתו.

**Metadata:** `category=automation` · `subcategory=skills` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_108 — מבנה SKILL.md ו-Frontmatter בסיסי

SKILL.md כולל Frontmatter כמו name ו-description ולאחריו הוראות התהליך. Description חשוב כי הוא מסביר ל-Claude מתי ה-Skill רלוונטי. ניתן להוסיף Model, Tools, Paths, Context ומאפיינים נוספים. StackAI מגדירה Output ברור כדי שה-Skill יחזיר תוצאה עקבית ולא רק 'יעזור' באופן כללי.

**Metadata:** `category=automation` · `subcategory=skills` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_109 — disable-model-invocation עבור Skills עם Side Effects

`disable-model-invocation: true` מתאים ל-Skills עם Side Effects שבהם רק המשתמש צריך להחליט מתי להריץ, למשל Deployment, Commit או פעולה עסקית רגישה. כך Claude לא מפעיל אותם מיוזמתו. StackAI מעדיפה Manual Invocation לכל Workflow שהעיתוי שלו הוא החלטה עסקית או אבטחתית.

**Metadata:** `category=automation` · `subcategory=skills` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_110 — allowed-tools ו-disallowed-tools בתוך Skill

`allowed-tools` יכול לאפשר Tools מסוימים במהלך Skill ללא Prompt נוסף, אך אינו בהכרח מסיר כלים אחרים מהסביבה. `disallowed-tools` יכול לסייע לצמצם. StackAI בודקת Skills שמגיעים מ-Repository משום שהגדרת Tools בתוך Skill היא חלק מה-Attack Surface וצריכה Review.

**Metadata:** `category=automation` · `subcategory=skills` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_111 — Arguments ו-Dynamic Context Injection ב-Skills

Skills יכולים לקבל Arguments כגון מספר Issue או שם לקוח, ולשלב Dynamic Context באמצעות פקודות שמבוצעות בזמן ההפעלה. לדוגמה ניתן להכניס `git diff` ל-Code Review. Dynamic Commands הם Shell אמיתי ולכן יש להעדיף פקודות צפויות ומצומצמות ולהימנע מהרחבה שלא נבדקה.

**Metadata:** `category=automation` · `subcategory=skills` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_112 — Supporting Files ושמירת SKILL.md ממוקד

Skill מורכב יכול לכלול Supporting Files כגון Checklists, Examples ו-Scripts. SKILL.md נשאר קצר ומפנה לקבצים שנקראים רק כאשר צריך. זה מפחית Context ומקל על תחזוקה. StackAI שומרת Reference ארוך מחוץ לקובץ הראשי ומכניסה את כל החבילה ל-Version Control.

**Metadata:** `category=automation` · `subcategory=skills` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_113 — Reference Skill לעומת Task Skill

Reference Skill מספק ידע שנדרש רק לעיתים, למשל כיצד מערכת Legacy מחשבת עמלות. Task Skill מגדיר Workflow כגון Release Check או Bug Investigation. ההבחנה עוזרת לבחור מבנה נכון: ידע אינו חייב להיות סדרת פקודות, ותהליך אינו צריך להיטמע כעמוד Documentation פסיבי.

**Metadata:** `category=automation` · `subcategory=skills` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_114 — שילוב Skills עם MCP ו-Hooks

MCP נותן ל-Claude יכולת, Skill נותן לו תהליך. לדוגמה MCP חושף `create_customer_task` ו-Skill מגדיר מתי לקרוא פניות, כיצד לסכם ומתי לבקש אישור לפני יצירת משימה. Hooks יכולים לאכוף בדיקות סביב אותו תהליך. השילוב יוצר Workflow ארגוני עקבי.

**Metadata:** `category=automation` · `subcategory=mcp` · `intent=how_to` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_115 — בדיקה, Versioning ו-Governance של Skills

Skills משותפים הם Configuration ארגוני ולכן שינוי בהם צריך לעבור Git Review. StackAI בודקת Purpose, Inputs, Output, Side Effects, Tools, Credentials ו-Test Case. ניתן לשמור Version ו-Owner כ-Metadata פנימי. Skill שלא בשימוש או שהתהליך שלו השתנה צריך לעבור עדכון או הסרה.

**Metadata:** `category=automation` · `subcategory=skills` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 13: Hooks ב-Claude Code – אוטומציה ואכיפה של תהליכים ארגוניים

## stk_116 — מהו Hook ומתי הוא עדיף על הנחיה ב-CLAUDE.md

Hook הוא מנגנון שמפעיל פעולה כאשר אירוע מסוים קורה ב-Claude Code. הוא מתאים ל-Formatting, Validation, Audit או בדיקה לפני Tool Call. בניגוד ל-CLAUDE.md שמבקש מ-Claude לזכור פעולה, Hook מחבר את הפעולה לנקודה קבועה ב-Workflow. StackAI משתמשת בו לאוטומציה ואכיפה ממוקדת.

**Metadata:** `category=automation` · `subcategory=hooks` · `intent=how_to` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_117 — Command, Prompt, Agent ו-HTTP Hooks

Command Hook מריץ Script או Shell command; Prompt Hook משתמש במודל לקבלת החלטה סמנטית; Agent Hook מפעיל Agent; HTTP Hook קורא שירות חיצוני. כאשר אפשר לבצע בדיקה קשיחה בקוד, StackAI מעדיפה Command Hook משום שהוא דטרמיניסטי יותר. Model-based Hook נשמר למקרים שבהם באמת נדרש שיקול סמנטי.

**Metadata:** `category=automation` · `subcategory=hooks` · `intent=how_to` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_118 — אירועי Hook מרכזיים במחזור העבודה

אירועי Hooks כוללים בין היתר SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, SubagentStart, SubagentStop, Stop ו-SessionEnd. אין צורך להשתמש בכולם. בוחרים Event לפי נקודת הבקרה שה-Use Case דורש.

**Metadata:** `category=automation` · `subcategory=hooks` · `intent=how_to` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_119 — PreToolUse לבדיקת פעולה לפני ביצוע

PreToolUse פועל לפני Tool ולכן מתאים ל-Validation או חסימה תלוית Context. לדוגמה ניתן לבדוק Command שמכוון ל-Production. אם פעולה אסורה תמיד, Permission Deny הוא בדרך כלל פשוט וחזק יותר; Hook מתאים כאשר ההחלטה תלויה בפרמטרים או Context.

**Metadata:** `category=automation` · `subcategory=automation` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_120 — PostToolUse ו-PostToolUseFailure לאחר הפעלת Tool

PostToolUse רץ לאחר Tool שהצליח ומתאים ל-Formatter, Lint, Logging או בדיקת קובץ אחרי עריכה. PostToolUseFailure מאפשר להגיב לכשל, למשל לאסוף Diagnostics. StackAI מפרידה בין Fast Checks שרצים לעיתים קרובות לבין בדיקות עמוקות שרצות בנקודות נדירות יותר.

**Metadata:** `category=automation` · `subcategory=automation` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_121 — JSON Input, Exit Codes ו-Structured Output ב-Hooks

Command Hooks מקבלים JSON דרך stdin עם פרטי Event, Tool ו-Context. Exit Codes ו-Structured JSON יכולים להעביר הצלחה, חסימה או Feedback, בהתאם לסוג האירוע. Script צריך לבצע Input Validation ולא להניח שהקלט בטוח. StackAI מתעדת את Schema הצפוי לכל Hook.

**Metadata:** `category=automation` · `subcategory=hooks` · `intent=how_to` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_122 — Hooks ברמת User, Project ו-Managed Settings

Hooks יכולים להיות ב-User Settings, Project Settings או Managed Settings. Hook פרויקטלי מתאים ל-Lint או Validation ספציפי; Managed Hook מתאים למדיניות ארגונית. Scope קובע מי יכול לשנות את ההגדרה ולכן Security Hook קריטי לא צריך להישען רק על קובץ מקומי של המשתמש.

**Metadata:** `category=automation` · `subcategory=hooks` · `intent=how_to` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_123 — אבטחת Hooks ובדיקת קוד שמגיע מ-Repository

Hook הוא קוד שיכול לרוץ במחשב ולכן כל Hook שמגיע מ-Repository או Plugin צריך Review. בודקים Command, Scripts, Network Calls ו-Credentials. StackAI אינה מאשרת Hook רק לפי שמו. שינוי Hook משמעותי עובר Branch, Review ו-Test בדיוק כמו קוד אחר.

**Metadata:** `category=automation` · `subcategory=security` · `intent=how_to` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_124 — Hook ל-Formatting ו-Validation לאחר Edit

Post Edit Hook יכול לזהות Extension ולהריץ Formatter או Validation מתאים, למשל Lint ל-TypeScript או בדיקת JSON. הוא צריך להיות מהיר וממוקד; בדיקה של דקות אחרי כל Edit פוגעת בחוויית העבודה. Deep Tests נשמרים ל-Stop, Skill או CI.

**Metadata:** `category=automation` · `subcategory=hooks` · `intent=how_to` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_125 — Hook להגנת Secrets ו-Production

Hooks יכולים להפעיל Secret Scanner לאחר Edit או לבדוק פקודות רגישות לפני ביצוע. Production Protection Hook יכול להחזיר Feedback או לחסום, אך אינו צריך להיות שכבת ההגנה היחידה. StackAI משלבת Hook עם Permissions, Identity ו-Network Controls עבור פעולה קריטית.

**Metadata:** `category=automation` · `subcategory=security` · `intent=how_to` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_126 — שילוב Hooks עם Skills, MCP ו-Audit

Skill מגדיר Workflow, MCP מספק יכולת, Hook מגיב לאירוע ו-Audit מתעד. לדוגמה Skill של Release מפעיל תהליך, Hook בודק Secret Scan לפני סיום, ו-MCP מעדכן מערכת חיצונית לאחר Approval. StackAI בונה מעט Hooks בעלי ערך ברור ומונעת מערכת אוטומציות מסובכת שקשה לתחזק.

**Metadata:** `category=automation` · `subcategory=mcp` · `intent=how_to` · `risk=medium` · `platform=all` · `last_verified=2026-10`


---

# מאמר 14: Git, GitHub וספק פיתוח חיצוני – איך העסק נשאר בעל השליטה בקוד

## stk_127 — העסק כבעלים של GitHub Organization וה-Repository

המודל המועדף הוא GitHub Organization בבעלות העסק ובתוכה Repositories עסקיים. הספק החיצוני מקבל גישה, אך אינו מחזיק את הנכס הראשי. כך העסק יכול להחליף ספק בלי לבקש את הקוד בחזרה. StackAI בודקת גם Cloud, Domain ו-CI/CD משום שבעלות על Git בלבד אינה מספיקה.

**Metadata:** `category=git_governance` · `subcategory=git` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_128 — שני Owners עסקיים וניהול הרשאות Admin

רצוי של-Organization יהיו לפחות שני Owners עסקיים או גורמים מאושרים לפי גודל החברה, כדי להימנע מתלות באדם יחיד. ספק חיצוני אינו מקבל Owner כברירת מחדל. Admin ניתן רק כאשר התפקיד דורש זאת. StackAI מתעדת מי בעל Role גבוה ולמה.

**Metadata:** `category=git_governance` · `subcategory=git_governance` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_129 — Outside Collaborators ו-Repository Roles לספקים

Outside Collaborator מאפשר לתת לספק גישה ל-Repositories מסוימים בלי להפוך אותו לחבר מלא בארגון. Repository Roles כמו Read, Write, Maintain ו-Admin מאפשרים Least Privilege. ספק שצריך לפתח ולפתוח PR אינו בהכרח צריך Admin או גישה לכל ה-Repositories.

**Metadata:** `category=git_governance` · `subcategory=vendor_management` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_130 — Rulesets, Branch Protection ו-PR חובה

Rulesets ו-Branch Protection יכולים לדרוש Pull Request, Review ו-Status Checks לפני Merge ולחסום Force Push או מחיקה. StackAI משתמשת בהם כדי לאכוף Workflow גם כאשר Claude או ספק עובדים מהר. Bypass List צריכה להיות קטנה ומבוקרת, אחרת ההגנה הופכת להמלצה בלבד.

**Metadata:** `category=git_governance` · `subcategory=git_governance` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_131 — CI/CD ו-Human Review בעבודה עם Claude Code

CI/CD מריץ Tests, Build ו-Security Checks ללא תלות ב-Claude, וה-Human Review נשאר נקודת אישור לשינוי משמעותי. Workflow בריא הוא Branch → Claude → Tests → PR → Review → Merge → Deployment Policy. Claude יכול לסייע ב-Review אך אינו צריך להיות Approver יחיד של שינוי שהוא עצמו כתב.

**Metadata:** `category=git_governance` · `subcategory=git_governance` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_132 — Secrets, Deployment Credentials ובעלות על סביבת Production

Secrets ו-Deployment Credentials אינם נשמרים בקוד. Cloud, Database ו-Production Accounts צריכים להיות בבעלות העסק, עם זהויות ורשאות נפרדות. ספק לא צריך להחזיק Root Credentials רק משום שהוא אחראי לפיתוח. StackAI ממפה מי יכול Deploy ומצמצמת Access בהתאם לסביבה.

**Metadata:** `category=git_governance` · `subcategory=security` · `intent=governance` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_133 — Offboarding של ספק פיתוח וגישה שנשארת ב-Local Clones

כאשר ספק עוזב מסירים GitHub, Cloud, VPN, MCP, SSH, Tokens ו-Deploy Keys ובודקים PRs ו-Branches פתוחים. יש לזכור ש-Local Clones שכבר הורדו אינם נעלמים עם הסרת GitHub Access; הטיפול בהם תלוי בהסכם ובמדיניות החברה. Offboarding צריך להיות מתועד מראש.

**Metadata:** `category=git_governance` · `subcategory=vendor_management` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_134 — מבחן 24 השעות להפחתת Vendor Dependency

מבחן 24 השעות שואל: אם ספק הפיתוח מפסיק לענות מחר, האם בתוך יום ניתן לתת לספק חדש Repository, Documentation, Setup, Deployment Process, Access Map ו-Known Issues? אם לא, קיימת תלות מסוכנת. Claude Code יכול לעזור לייצר תיעוד, אך הבעלות והגישה צריכות להיות מוסדרות.

**Metadata:** `category=git_governance` · `subcategory=vendor_management` · `intent=governance` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_135 — Ownership Map ו-Repository Audit של StackAI

Ownership Map מציג מי בעל GitHub, Domain, Hosting, Database, Cloud, CI/CD ו-Secrets. Repository Audit בודק Owners, External Access, Roles, Rulesets, Default Branch, Secrets ו-Deployment. שני המסמכים נותנים לעסק תמונת שליטה ומאפשרים ל-StackAI לתכנן מעבר מספק-תלוי למודל עסק-שולט.

**Metadata:** `category=git_governance` · `subcategory=git_governance` · `intent=governance` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 15: Subagents ו-Agent Teams ב-Claude Code – בניית צוות AI ארגוני

## stk_136 — מהו Subagent ולמה להשתמש ב-Context נפרד

Subagent הוא Agent שפועל ב-Context נפרד ומחזיר תוצאה ל-Claude הראשי. הוא מתאים לחקירה עמוקה, Security Review או Test Analysis בלי למלא את השיחה הראשית בכל הקבצים והצעדים. היתרון הוא בידוד Context והתמחות; החיסרון הוא צריכת משאבים נוספת וצורך להגדיר משימה ברורה.

**Metadata:** `category=automation` · `subcategory=agents` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_137 — מתי להשתמש ב-Subagent ומתי Claude יחיד מספיק

Claude יחיד מספיק למשימות פשוטות וקצרות. Subagent מתאים כאשר העבודה ניתנת לבידוד, דורשת קריאת הרבה קבצים, מומחיות מסוימת או יכולה לרוץ במקביל. StackAI אינה יוצרת Agent לכל משימה, משום שעוד Agents מוסיפים עלות ומורכבות בלי בהכרח לשפר איכות.

**Metadata:** `category=automation` · `subcategory=agents` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_138 — יצירת Custom Subagent באמצעות .claude/agents

Custom Subagent ניתן להגדיר בקבצים תחת `.claude/agents/` עם Name, Description, Prompt ו-Tools. Prompt צריך להיות עצמאי כי ה-Agent אינו מקבל בהכרח את כל היסטוריית השיחה. StackAI מגדירה Output Format ברור ותפקיד צר, למשל Security Reviewer או Test Analyst.

**Metadata:** `category=automation` · `subcategory=agents` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_139 — Least Privilege ל-Review Agents

Review Agent בדרך כלל צריך Read, Grep ו-Glob ולא Edit/Write. Least Privilege מונע ממנו 'לתקן בשקט' את הדבר שהוא אמור לבקר. Implementation Agent יכול לקבל Write בהתאם למדיניות. Production ו-Push נשלטים בנפרד דרך Permissions ו-Git Governance.

**Metadata:** `category=automation` · `subcategory=agents` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_140 — הפעלת מספר Subagents במקביל ל-Deep Review

ב-Deep Review ניתן להפעיל Security, Testing ו-Architecture Subagents במקביל ואז לאחד את הממצאים. זה מתאים לשינוי משמעותי שבו תחומי הבדיקה עצמאיים. הדוח המאוחד צריך להציג Findings, Risks ופריטים הדורשים Review אנושי ולא להכריז שהקוד 'בטוח' באופן מוחלט.

**Metadata:** `category=automation` · `subcategory=agents` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_141 — Context, Memory, Skills ו-MCP בתוך Subagent

Subagent עובד ב-Context מבודד ויכול לקבל Skills, Memory ו-MCP לפי הגדרה. אין להניח שהוא יודע את כל פרטי השיחה הראשית. MCP Access צריך להיות מצומצם לפי תפקיד. Review Agent שקורא Tickets אינו צריך Tool למחיקה, ו-Agent עם Memory דורש Governance על מה נשמר לאורך זמן.

**Metadata:** `category=automation` · `subcategory=mcp` · `intent=how_to` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_142 — Agent Teams לעומת Subagents

Agent Team שונה מ-Subagents בכך שמספר Claude Sessions עצמאיים יכולים לעבוד עם Task List משותף ולתקשר ביניהם. Subagents מדווחים בעיקר ל-Main Agent. Team מתאים לפיתוח מקביל מורכב; Review ממוקד בדרך כלל מסתדר טוב יותר עם Subagents פשוטים.

**Metadata:** `category=automation` · `subcategory=agents` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_143 — Agent Teams כיכולת ניסיונית ועלות השימוש

Agent Teams הם יכולת מתקדמת וניסיונית בסביבות שבהן הם זמינים, וכל Teammate מחזיק Session ו-Context משלו ולכן העלות יכולה לגדול משמעותית. StackAI אינה מפעילה Team ביום הראשון של Pilot. קודם בודקים אם Claude יחיד או מספר Subagents פותרים את הבעיה בפחות מורכבות.

**Metadata:** `category=automation` · `subcategory=agents` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_144 — Git Worktrees ו-Batch לעבודה מקבילית

Git Worktrees מאפשרים לכל Agent לעבוד על Branch וסביבת קבצים נפרדת. זה מפחית התנגשויות כאשר עבודה מקבילית נוגעת בחלקים שונים. יכולות Batch יכולות לפרק משימות רחבות ליחידות. עדיין נדרש Integration מסודר דרך Git ו-PR ולא 'מיזוג' אוטומטי ללא Review.

**Metadata:** `category=automation` · `subcategory=git` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_145 — Governance ורמות בשלות ל-Agents בארגון

StackAI מגדירה ארבע רמות בשלות: Claude יחיד; Specialist Subagents; Automated Agent Workflows; Agent Teams. המעבר לרמה הבאה מתבצע רק אם יש Use Case, Governance ויכולת למדוד ערך. Agents עצמם נכנסים ל-Version Control, עוברים Review ומקבלים Tools לפי Least Privilege.

**Metadata:** `category=automation` · `subcategory=agents` · `intent=how_to` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 16: ניטור, Audit, עלויות ו-Observability של Claude Code בארגון

## stk_146 — מודל Observability של StackAI: Usage, Cost, Audit ו-ROI

StackAI מחלקת Observability לארבעה תחומים: Usage, Cost, Audit ו-ROI. Usage מראה מי משתמש ובאיזו תדירות; Cost מראה Tokens ועלות; Audit מתעד Tools, MCP, Hooks ו-Permission Events; ROI מחבר את הנתונים לתוצאה עסקית. המטרה אינה לאסוף כמה שיותר Telemetry אלא לקבל מידע שמאפשר לנהל את ההטמעה.

**Metadata:** `category=operations_support` · `subcategory=roi` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_147 — בדיקת שימוש מקומי באמצעות /usage

`/usage` מאפשר למשתמש לראות מידע על שימוש בסשן, Tokens, Model ובמקרים מתאימים גם צריכה ביחס למגבלות. הוא טוב לאבחון אישי ולהבנת Context ו-Cost, אך אינו תחליף לניטור מרכזי כאשר יש כמה עובדים. StackAI משתמשת בו בעיקר ב-Pilot וב-Support מקומי.

**Metadata:** `category=operations_support` · `subcategory=operations_support` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_148 — הפעלת OpenTelemetry עבור Claude Code

Claude Code יכול לייצא Telemetry באמצעות OpenTelemetry. ניתן לשלוח Metrics, Events ובאופן אופציונלי Traces ל-OTLP Endpoint או Collector מרכזי. StackAI מגדירה את היעד באמצעות Policy ארגונית כאשר נדרש ומוודאת שהניטור עצמו אינו שולח מידע רגיש שלא לצורך.

**Metadata:** `category=operations_support` · `subcategory=monitoring` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_149 — Metrics מרכזיים: Sessions, Tokens ו-Cost

מדדים שימושיים כוללים Session Count, Token Usage ו-Cost Usage. אפשר לנתח לפי משתמש, Model, Skill, Plugin או Subagent כאשר הנתונים זמינים. העלות ב-Telemetry היא אינדיקציה תפעולית ולא תחליף לחשבונית הרשמית. StackAI עוקבת אחרי מגמות ולא רק אחרי מספר בודד.

**Metadata:** `category=operations_support` · `subcategory=operations_support` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_150 — Analytics ארגוני ומדידת Claude-assisted Pull Requests

Analytics ארגוני יכול לספק Adoption ומדדים כמו Daily Active Users, Sessions ו-Pull Requests שבהם זוהתה תרומת Claude. מדדי Attribution אינם הוכחה ישירה לפרודוקטיביות, ולכן StackAI משלבת אותם עם Cycle Time, Rework ו-Business Outcomes. יותר PRs או שורות קוד אינם בהכרח הצלחה.

**Metadata:** `category=operations_support` · `subcategory=operations_support` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_151 — Audit לאירועי Tools, MCP, Permissions, Hooks, Skills ו-Subagents

Audit יכול לתעד אירועי Tool, MCP, Permission Mode, Hooks, Skills ו-Subagents, ולשייך אותם למשתמש ול-Session. המטרה היא להבין מי הפעיל מה, מה נכשל ומה נחסם. StackAI אינה מתעדת אוטומטית כל תוכן; היא שומרת Metadata תפעולי ומרחיבה Logging רק כאשר קיים צורך ברור.

**Metadata:** `category=operations_support` · `subcategory=permissions` · `intent=operations` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_152 — Privacy ו-Redaction ב-Telemetry ו-Logging

Telemetry עלולה להפוך למאגר מידע רגיש אם שומרים Prompts, Tool Inputs או Outputs מלאים. StackAI מעדיפה ברירת מחדל של Metadata, Redaction ו-Masking. Raw API Bodies או Prompt Content מופעלים רק בהחלטה מפורשת עם Retention ואבטחה מתאימים. Audit טוב אינו צריך להעתיק את כל שיחת המשתמש.

**Metadata:** `category=operations_support` · `subcategory=monitoring` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_153 — התראות על Cost Spike, Permission Change ו-MCP Failure

Alerts צריכים להיות ממוקדים: Cost Spike חריג, Permission Change משמעותי, MCP Failure, Authentication Failure או עלייה ב-Hook Blocks. לא כל עלייה ב-Sessions היא Incident. StackAI קובעת Baseline ורק חריגה בעלת משמעות מייצרת התראה, כדי למנוע Alert Fatigue.

**Metadata:** `category=operations_support` · `subcategory=permissions` · `intent=operations` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_154 — StackAI ROI Framework ומדידת חיסכון בזמן ובשעות ספק

ROI נמדד בזמן שנחסך, ירידה בשעות ספק, שיפור Cycle Time, איכות ויכולת עצמאית. לדוגמה, אם טיפול בבאג ירד מ-3 שעות ל-45 דקות, זה נתון שימושי יותר ממספר Tokens. לפני Pilot נמדד Baseline ולאחר 30–60 יום משווים תוצאה. Cost נבחנת תמיד מול הערך שנוצר.

**Metadata:** `category=operations_support` · `subcategory=roi` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_155 — רמות Monitoring ודוח חודשי של StackAI

StackAI מגדירה רמות Monitoring: Basic עם `/usage`; Managed עם OTel ו-Dashboard; Governance עם Permission/MCP/Hook Events; Security/Compliance עם SIEM ו-Retention. דוח חודשי מסכם Adoption, Cost, Incidents, Integrations ו-ROI ומציע פעולות לחודש הבא. עסק קטן אינו חייב Enterprise Monitoring אם הצורך אינו מצדיק זאת.

**Metadata:** `category=operations_support` · `subcategory=monitoring` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 17: אבטחת מידע, Secrets ו-Credentials ב-Claude Code – הגנה על המידע הארגוני

## stk_156 — מיפוי Access Paths לפני הטמעת Claude Code

לפני הטמעה ממפים Access Paths: קבצים, Environment Variables, CLIs מאומתים, GitHub, Cloud, Database, SSH, kubectl, MCP ו-Production. Claude יכול להשתמש בזהות שכבר קיימת במחשב גם אם אינו 'רואה' את הסיסמה. לכן Security Assessment בודק מה Terminal מסוגל לעשות בפועל ולא רק אילו Secrets נמצאים בקוד.

**Metadata:** `category=permissions_security` · `subcategory=permissions_security` · `intent=security` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_157 — Secrets אינם Context: מה לא להכניס ל-CLAUDE.md, Skills ו-Agents

Secrets אינם Context. אין להכניס Passwords, API Keys או Tokens ל-CLAUDE.md, Skills או Agent Prompts. רכיבים אלה יכולים להפנות לשם משתנה כמו `DEPLOY_TOKEN`, אך הערך עצמו נשמר ב-Secret Management או Credential Store. כך הידע והסוד נשארים מופרדים.

**Metadata:** `category=permissions_security` · `subcategory=security` · `intent=security` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_158 — .env ו-.gitignore: למה Git Ignore אינו מנגנון הרשאה

`.gitignore` מונע בדרך כלל מ-Git להוסיף קובץ חדש ל-Repository, אך אינו חוסם את Claude מקריאתו אם הוא קיים בסביבת העבודה. לכן `.env`, Keys ו-Credentials דורשים Permissions או בידוד נוסף. אפשר לספק `.env.example` עם שמות משתנים וערכי Test במקום לחשוף Secret אמיתי.

**Metadata:** `category=permissions_security` · `subcategory=git` · `intent=security` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_159 — Permissions, Sandbox ו-bypassPermissions בהגנת הסביבה

Permissions קובעות מה Claude רשאי להפעיל; Sandbox מגביל לאן התהליך יכול להגיע. `bypassPermissions` מרחיב אוטונומיה ולכן אינו ברירת מחדל בסביבה עסקית. StackAI משלבת Deny Rules, Sandbox, Identity מצומצמת ואישור אנושי במקום להסתמך על שכבה אחת.

**Metadata:** `category=permissions_security` · `subcategory=security` · `intent=security` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_160 — Credentials קיימים ב-CLI: AWS, GitHub, SSH, kubectl ועוד

CLI מאומת יכול להיות Access Path משמעותי: AWS CLI, `gh`, SSH Agent, `kubectl` או Database CLI עשויים לעבוד ללא Password נוסף. יש לבדוק `gh auth status`, Cloud Identity, SSH Keys ו-Kubernetes Context. Claude שמקבל Bash יכול להשתמש בכלים האלה בהתאם להרשאות, ולכן Identity צריכה להיות מינימלית.

**Metadata:** `category=permissions_security` · `subcategory=security` · `intent=security` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_161 — הפרדה בין Development, Staging ו-Production

Development, Staging ו-Production צריכים להיות מופרדים. Claude עובד תחילה ב-Development/Branch, אחר כך Staging, ו-Production דורש Policy ואישור מתאים. אין לתת Production Credential רק כי המפתח האנושי מחזיק אותו. הפרדה סביבתית מקטינה את הנזק האפשרי מטעות או Prompt Injection.

**Metadata:** `category=permissions_security` · `subcategory=permissions_security` · `intent=security` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_162 — PII, Masking ושימוש ב-Test Data

כאשר המשימה אינה דורשת PII אמיתי, משתמשים ב-Test Data, Masking או מזהים מלאכותיים. פרטי לקוחות, טלפונים, מידע פיננסי או רפואי אינם צריכים להיכנס ל-Context רק כדי לשחזר Bug. StackAI מגדירה איזה סוג מידע מותר בכל Environment ומעדיפה מינימום נתונים.

**Metadata:** `category=permissions_security` · `subcategory=permissions_security` · `intent=security` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_163 — טיפול ב-Secret שנחשף ב-Git והצורך ב-Rotation

אם Secret נכנס ל-Git, מחיקה מהקובץ אינה מספיקה. מתייחסים אליו כחשוף בהתאם לנסיבות: מבטלים או מסובבים, בודקים Logs ו-History, מנקים היסטוריה אם נדרש ומוסיפים Secret Scanning למניעה. Rotation הוא הצעד החשוב משום ש-Credential ישן עלול להמשיך לעבוד גם לאחר מחיקה.

**Metadata:** `category=permissions_security` · `subcategory=security` · `intent=security` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_164 — MCP Security ו-Minimum Tool Access

MCP Security מבוסס על Minimum Tool Access. מתחילים ב-Read Tools, מוסיפים Write בסיכון נמוך, ו-Sensitive Actions דורשים Approval או נשארים חסומים. Credential של MCP צריך להיות ייעודי וניתן לביטול. Server צד שלישי עובר Review משום שהוא מקבל גישה למידע ולפעולות עסקיות.

**Metadata:** `category=permissions_security` · `subcategory=mcp` · `intent=security` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_165 — זהויות ספקים, Service Accounts ו-Credential Inventory

לכל ספק ולעבודה אוטומטית עדיף Identity נפרדת ולא Shared Account. Service Account מקבל Scope מוגבל, Owner ותהליך Rotation. Credential Inventory מתעד Purpose, Environment, Scope, Storage ו-Revocation. כאשר ספק עוזב ניתן להשבית את זהותו במקום להחליף סיסמה משותפת בכל המערכות.

**Metadata:** `category=permissions_security` · `subcategory=security` · `intent=security` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_166 — Prompt Injection, Supply Chain ו-Data Exfiltration

Prompt Injection ו-Supply Chain חשובים כאשר Claude קורא תוכן חיצוני, Packages, MCP Responses או Repository לא מוכר. מידע חיצוני אינו Instruction מהימן. Agent שקורא אינטרנט לא צריך בהכרח Production Write באותו Context. StackAI משתמשת ב-Separation of Duties, Limited Tools ו-Network Controls לצמצום Data Exfiltration.

**Metadata:** `category=permissions_security` · `subcategory=permissions_security` · `intent=security` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_167 — Incident Response, Kill Switch ו-StackAI Security Baseline

Incident Response של StackAI הוא Stop → Contain → Rotate → Investigate → Recover → Improve. Kill Switch יכול להיות ביטול Credential, השבתת MCP, Service Account או Network Access. לאחר אירוע בודקים Session, Git, Tool Calls ו-Cloud Logs ומעדכנים Permission, Hook או Process כדי למנוע חזרה.

**Metadata:** `category=permissions_security` · `subcategory=permissions_security` · `intent=security` · `risk=high` · `platform=all` · `last_verified=2026-10`


---

# מאמר 18: מתודולוגיית StackAI – תהליך מלא להטמעת Claude Code בעסק

## stk_168 — מודל StackAI: Discover, Assess, Design, Secure, Deploy, Pilot, Adopt, Improve

מתודולוגיית StackAI מחברת שמונה שלבים: Discover, Assess, Design, Secure, Deploy, Pilot, Adopt ו-Improve. היא נועדה למנוע התקנה טכנית ללא יעד עסקי, Governance ותחזוקה. כל שלב מייצר Deliverable ברור, וההרחבה לשלב הבא מתבצעת רק כאשר התנאים הבסיסיים קיימים.

**Metadata:** `category=implementation` · `subcategory=pilot` · `intent=implementation` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_169 — שלב Discover: הבנת הבעיה העסקית לפני הטכנולוגיה

Discover מתחיל מהעסק: מה כואב, מי משתמש, מי הספק ומה ייחשב הצלחה. דוגמאות הן תלות בפיתוח חיצוני, זמן שינוי ארוך או חוסר תיעוד. StackAI אינה מתחילה בבחירת Feature של Claude. קודם מגדירים Business Problem, אחר כך Process ורק לבסוף Technology.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_170 — שלב Assess: Ownership Map ובדיקת מוכנות

Assess ממפה Repository, Ownership, Cloud, Domain, Database, Credentials, Documentation וספקים. Ownership Map מציג מי בעל כל נכס ומי מנהל אותו בפועל. במקביל Readiness Assessment בודק סביבה, Rollback, משתמשים ו-Security. אם חסרה תשתית קריטית, מתקנים אותה לפני Pilot.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_171 — בחירת Pilot בעל ערך עסקי וסיכון מוגבל

Pilot טוב נותן ערך אך מגביל סיכון. לדוגמה Code Review, Documentation או טיפול בבאגים קטנים ב-Development. מגדירים משתמשים, Repository, משך ו-KPI. לא מתחילים עם אוטומציה על Production. Pilot מאפשר למדוד ערך ולגלות פערים לפני Rollout רחב.

**Metadata:** `category=implementation` · `subcategory=pilot` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_172 — Design: Authentication, Accounts, Git, Data ו-Production

ב-Design מחליטים על Authentication, Accounts, Git Ownership, Data Access, Production Policy ו-Architecture. משרטטים כיצד Claude Code, Repository, MCP ומערכות העסק מתחברים. המטרה היא למנוע החלטות Ad-hoc במהלך ההתקנה ולתת ללקוח תמונה של גבולות האחריות.

**Metadata:** `category=implementation` · `subcategory=git` · `intent=implementation` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_173 — Secure: Permissions, Sandbox, Secrets ו-Managed Settings

שלב Secure מגדיר Permissions, Managed Settings, Sandbox, Secrets, Network ו-Identity. כל Access חדש נשאל לפי Need, Risk, Revocation ו-Monitoring. Security Baseline נבדק בפועל באמצעות פעולות Allow/Ask/Deny ולא רק בקריאת קובץ Settings.

**Metadata:** `category=implementation` · `subcategory=security` · `intent=implementation` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_174 — Deploy: התקנה, Verification ו-Configuration Baseline

Deploy כולל התקנה בשיטה מאושרת, `claude --version`, `claude doctor`, `/status` ו-Configuration Baseline. מתעדים Authentication, Version, Settings Sources ו-Environment. ההתקנה נחשבת מלאה רק לאחר Smoke Test מול פרויקט מתאים ולא כאשר הבינארי קיים.

**Metadata:** `category=implementation` · `subcategory=installation` · `intent=implementation` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_175 — הקמת CLAUDE.md, Git Governance ו-Settings

לאחר ההתקנה בונים CLAUDE.md, Git Workflow ו-Settings. Repository נמצא בשליטת העסק, main מוגן ותהליכים חוזרים עוברים ל-Skills. כללי אבטחה קריטיים נאכפים ב-Managed Settings או מערכות חיצוניות ולא נשארים רק כהמלצה ב-Documentation.

**Metadata:** `category=implementation` · `subcategory=git` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_176 — Rollout של MCP, Skills, Hooks ו-Subagents

MCP, Skills, Hooks ו-Subagents נכנסים בהדרגה. קודם מחברים Read-only Integration, אחר כך Workflow מצומצם, ורק לאחר שהשימוש ברור מוסיפים Automation. StackAI מעדיפה 2–4 רכיבים שימושיים על פני עשרות Customizations שקשה להבין ולתחזק.

**Metadata:** `category=implementation` · `subcategory=mcp` · `intent=implementation` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_177 — Pilot Execution, KPIs והחלטת Go / Adjust / Stop

ב-Pilot מודדים Adoption, Speed, Quality, Cost ו-Vendor Dependency. בסוף מתקבלת החלטת Go, Adjust או Stop. Stop הוא תוצאה לגיטימית אם Use Case אינו מצדיק עלות או מורכבות. אין להרחיב הטמעה רק משום שכבר השקענו בהקמה.

**Metadata:** `category=implementation` · `subcategory=pilot` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_178 — Training ו-Go-Live מדורג

Training מלמד Plan Mode, Git diff, Permissions, Secrets, Evidence ו-Stop Conditions — לא רק Prompting. Go-Live נעשה בהדרגה למשתמשים נוספים. לפני הרחבה בודקים Monitoring, Incident Process, Documentation ו-Support Owner. כך אימוץ אינו תלוי במשתמש 'אלוף' אחד.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_179 — Monthly Improvement ו-StackAI Implementation Pack

לאחר Go-Live מתחיל Monthly Improvement: Usage, Cost, Security, Skills, MCP, Vendor Access ו-Use Cases חדשים. הלקוח מקבל Implementation Pack הכולל Discovery, Readiness, Ownership Map, Architecture, Security Profile, CLAUDE.md, Settings, Registries, Pilot Report ו-Support Plan. המטרה היא שהלקוח יישאר בעל השליטה.

**Metadata:** `category=implementation` · `subcategory=implementation` · `intent=implementation` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 19: Troubleshooting ל-Claude Code בארגון – מדריך StackAI לאבחון ופתרון תקלות

## stk_180 — claude command not found: אבחון PATH והתקנה

אם `claude` אינו מזוהה, קודם בודקים האם הבינארי קיים והאם תיקיית ההתקנה נמצאת ב-PATH. ב-Windows Native הנתיב המקובל הוא `%USERPROFILE%\.local\bin`; ב-macOS/Linux `~/.local/bin`. לאחר תיקון PATH פותחים Terminal חדש ומריצים `claude --version` ו-`claude doctor`.

**Metadata:** `category=operations_support` · `subcategory=installation` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_181 — מספר התקנות Claude Code וגרסה לא צפויה

כאשר מתקבלת גרסה לא צפויה, ייתכן שקיימות מספר התקנות. ב-Windows משתמשים ב-`where.exe claude`; ב-macOS/Linux ב-`which -a claude`. משאירים שיטת התקנה אחת ברורה ומסירים עותקים ישנים אם אינם נדרשים. לאחר מכן מאמתים Version ו-Update Channel.

**Metadata:** `category=operations_support` · `subcategory=installation` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_182 — כשל הורדה, Proxy, Firewall ו-TLS Certificate

כשל הורדה או Connection עשוי לנבוע מ-DNS, Proxy, Firewall או TLS Inspection. בודקים גישה לשרתי ההורדה, Environment Variables של Proxy ו-CA ארגוני. אין לעקוף TLS Validation כפתרון קבוע. בסביבה ארגונית עובדים עם IT כדי לאפשר Domains ו-Certificate Chain מתאימים.

**Metadata:** `category=operations_support` · `subcategory=troubleshooting` · `intent=troubleshooting` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_183 — Login נכשל או Credential לא צפוי נמצא בשימוש

אם Login נכשל, בודקים `/status`, מבצעים `/logout` ו-`/login`, ומוודאים שהחשבון מורשה. אם Claude משתמש ב-Credential לא צפוי, מחפשים Environment Variables כמו `ANTHROPIC_API_KEY` שיכולים לשנות את מסלול ההתחברות. Proxy או Organization Policy יכולים גם לגרום ל-403/OAuth failure.

**Metadata:** `category=operations_support` · `subcategory=troubleshooting` · `intent=troubleshooting` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_184 — Settings precedence ו-Settings Error ב-JSON

אם שינוי ב-Settings אינו משפיע, בודקים `/status` ואת סדר הקדימות בין Managed, Command Line, Local, Project ו-User. Settings Error עשוי לנבוע מ-JSON לא תקין, Comment או Trailing Comma. מריצים `claude doctor` ובמידת הצורך `/debug` כדי לראות איזה מקור נטען.

**Metadata:** `category=operations_support` · `subcategory=settings` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_185 — CLAUDE.md לא נטען או שהוראה מתעלמת

אם CLAUDE.md לא משפיע, בודקים `/context` כדי לוודא שהוא נטען. קובץ בתת-תיקייה עשוי להיטען רק כאשר Claude עובד באותו אזור. אם הוא נטען אך הוראה מתעלמת, מחפשים ניסוח עמום, סתירה או מסמך ארוך מדי. הוראה קריטית צריכה גם אכיפה טכנית אם נדרש.

**Metadata:** `category=operations_support` · `subcategory=troubleshooting` · `intent=troubleshooting` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_186 — Permissions מתנהגים אחרת מהמצופה

כאשר Permissions מתנהגות אחרת מהמצופה, פותחים `/permissions` ובודקים Rules ומקור. Deny יכול לגבור על Allow, ו-Bash Pattern עשוי לא לכסות וריאציה אחרת של אותה פקודה. אם נדרש גבול קשיח, שקלו Hook או Sandbox ולא רק String Pattern.

**Metadata:** `category=operations_support` · `subcategory=permissions` · `intent=operations` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_187 — MCP Server לא מופיע או נמצא ב-Pending Approval

אם MCP Server לא מופיע, מריצים `claude mcp list` ובתוך Claude `/mcp`. Project Server צריך להיות מוגדר ב-`.mcp.json` ב-Root ולהיות מאושר כ-Trusted. מצב Pending Approval מצריך אישור משתמש. בודקים גם Scope נכון ושם Server.

**Metadata:** `category=operations_support` · `subcategory=troubleshooting` · `intent=troubleshooting` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_188 — MCP Authentication או Connection Failure

MCP Connection Failure נבדק עם `claude mcp get NAME` ו-`/mcp`. 401/403 מצביעים לרוב על Authentication/Scope; Network Error על Proxy/DNS; Local Server עשוי להיכשל בגלל Command או Dependency. OAuth Server ניתן להתחבר מחדש דרך `/mcp` או פקודת login מתאימה.

**Metadata:** `category=operations_support` · `subcategory=mcp` · `intent=operations` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_189 — MCP מחובר אבל Tools לא מופיעים

אם MCP מחובר אבל מציג אפס Tools, בודקים Tool Count ב-`/mcp`, מבצעים Reconnect ומפעילים Debug ל-MCP. ייתכן שה-Server עצמו אינו מפרסם Tools או שגרסה/Config אינה תואמת. ב-stdio יש לבדוק גם Paths מוחלטים ו-Working Directory.

**Metadata:** `category=operations_support` · `subcategory=troubleshooting` · `intent=troubleshooting` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_190 — Hook לא מופיע או לא רץ

אם Hook אינו מופיע, פותחים `/hooks` ומוודאים שההגדרה נמצאת תחת `hooks` בתוך settings.json המתאים. אם מופיע אבל לא רץ, בודקים Event, Matcher ו-Case Sensitivity של Tool Name. `claude --debug` או debug file מציגים Match, Exit Code ו-Output של Hook.

**Metadata:** `category=operations_support` · `subcategory=troubleshooting` · `intent=troubleshooting` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_191 — Skill לא מופיע או אינו מופעל אוטומטית

Skill של Project צריך להימצא תחת `.claude/skills/<name>/SKILL.md`. אם אינו מופיע, בודקים מבנה, Frontmatter ו-`/skills`. אם הוא קיים אך Claude לא מפעיל אוטומטית, ייתכן `disable-model-invocation: true` או Description לא ברור. ניתן להריץ ידנית כדי להפריד בין Discovery ל-Invocation.

**Metadata:** `category=operations_support` · `subcategory=troubleshooting` · `intent=troubleshooting` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_192 — Subagent לא מקיים CLAUDE.md או Context צפוי

Subagent אינו בהכרח מקבל את כל CLAUDE.md או היסטוריית השיחה. Custom Agent צריך Prompt עצמאי, ויש לבדוק Settings של Context/Memory. אם כלל קריטי חסר, מעבירים אותו במפורש או מגדירים Agent מתאים. אין להניח שכל Agent מובנה מתנהג כמו Session ראשי.

**Metadata:** `category=operations_support` · `subcategory=agents` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_193 — Search לא מוצא קבצים ו-ripgrep/WSL איטיים

אם Search או `@file` אינם מוצאים קבצים, בודקים ripgrep, Ignore Rules ומיקום הפרויקט. ב-WSL עבודה על `/mnt/c` יכולה להיות איטית לעומת Filesystem של Linux. ניתן לבדוק `claude doctor` ולהשתמש ב-ripgrep מערכת אם נדרש. בעיית Search אינה תמיד בעיית Claude עצמה.

**Metadata:** `category=operations_support` · `subcategory=operations_support` · `intent=operations` · `risk=low` · `platform=windows-wsl` · `last_verified=2026-10`

## stk_194 — CPU, RAM ו-Context גבוהים או Session נתקע

CPU, RAM או Context גבוהים מטופלים באמצעות `/compact`, Session חדש, צמצום קבצים ובדיקת Customizations. `--safe-mode` עוזר לזהות אם Plugin, Hook או MCP גורמים לבעיה. Session תקוע ניתן לעצור ב-Ctrl+C ולחדש עם `--resume`. Heapdump עלול להכיל מידע רגיש.

**Metadata:** `category=operations_support` · `subcategory=operations_support` · `intent=troubleshooting` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_195 — Safe Mode, Clean Config, Debug ו-Escalation

Safe Mode משבית Customizations מרכזיים ומאפשר לבדוק אם הבעיה נובעת מ-Configuration. Clean Config עם `CLAUDE_CONFIG_DIR` זמני מבודד עוד יותר, כאשר Managed Settings עדיין עשויות לחול. אם התקלה נמשכת, אוספים Debug Log, Version, Reproduction Steps ו-Doctor Output לפני Escalation — ללא Secrets.

**Metadata:** `category=operations_support` · `subcategory=operations_support` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`


---

# מאמר 20: StackAI Claude Code Operations Manual – תחזוקה וניהול שוטף לאחר ההטמעה

## stk_196 — Version Management ו-Stable לעומת Latest

Version Management קובע Release Channel ודרך עדכון. `stable` מתאים לרוב הסביבות העסקיות שמעדיפות יציבות; `latest` מתאים לבדיקת Features חדשים. StackAI יכולה לבדוק Latest בסביבה פנימית לפני Rollout. Version נרשמת ב-Support וניתן להגדיר Minimum/Required Version לפי מדיניות.

**Metadata:** `category=operations_support` · `subcategory=version_management` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_197 — Health Check תקופתי באמצעות claude doctor ו-/status

Health Check תקופתי כולל `claude doctor` ו-`/status`. בודקים Version, Authentication, Setting Sources, MCP, Hooks ו-Environment. המטרה היא לזהות Drift לפני שמשתמש מדווח על תקלה. StackAI שומרת תמונת מצב חודשית ולא מסתפקת ב'זה עובד כרגע'.

**Metadata:** `category=operations_support` · `subcategory=operations_support` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_198 — Configuration Drift ו-Permission Hygiene

Configuration Drift נוצר כאשר Local Overrides ו-Allow Rules מצטברים. Permission Hygiene בודק כל Rule: האם עדיין צריך אותו, מי ביקש ומה Scope. כללים קריטיים עוברים ל-Managed Policy כאשר הם אינם אמורים להיות ניתנים לשינוי. Golden Configuration מאפשר להשוות מצב נוכחי למצב מאושר.

**Metadata:** `category=operations_support` · `subcategory=permissions` · `intent=operations` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_199 — MCP Drift ובדיקת Tool Inventory תקופתית

MCP Drift קורה כאשר Server משתנה, מוסיף Tools או מחליף Credential. Review תקופתי בודק Purpose, Owner, Authentication, Tool Inventory ו-Read/Write Risk. Tool חדש כמו `delete_customer` לא צריך לקבל הרשאה רק משום שהופיע לאחר Upgrade. כל הרחבה עוברת Risk Classification מחדש.

**Metadata:** `category=operations_support` · `subcategory=mcp` · `intent=operations` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_200 — סקירה תקופתית של Skills, Hooks ו-Agents

Skills, Hooks ו-Agents נבדקים לפי שימוש, ביצועים ודיוק. Skill שלא מופעל עשוי להיות מיותר או לא ברור; Hook איטי יכול לבזבז זמן; Agent יקר עשוי לחזור על Agent אחר. StackAI מסירה Customizations שאין להם ערך במקום להמשיך לצבור מורכבות.

**Metadata:** `category=operations_support` · `subcategory=skills` · `intent=operations` · `risk=medium` · `platform=all` · `last_verified=2026-10`

## stk_201 — Git Governance, Vendor Access ו-Credential Review

Git Governance Review בודק Owners, Outside Collaborators, Rulesets, Bypass, Deploy Keys ו-GitHub Apps. Credential Review בודק Expiration, Scope, Owner ו-Usage. ספק שעזב צריך להיעלם מכל Access Path, לא רק מ-GitHub. הבדיקות מתחברות ל-Offboarding ול-Ownership Map.

**Metadata:** `category=operations_support` · `subcategory=security` · `intent=operations` · `risk=high` · `platform=all` · `last_verified=2026-10`

## stk_202 — עדכון CLAUDE.md ו-Documentation לאורך זמן

CLAUDE.md ו-Documentation צריכים להתעדכן כאשר Architecture, Commands, Deployment, Integrations או Business Rules משתנים. טעות שחוזרת אצל Claude היא סימן לבדוק אם ההוראה חסרה או מיושנת. README, architecture, development, deployment ו-troubleshooting הם נכסי Operations ולא מסמכים חד-פעמיים.

**Metadata:** `category=operations_support` · `subcategory=claude_md` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_203 — Cost Review מול Business Value ו-/insights

Cost Review בוחן Tokens, Sessions, Agents ו-MCP מול Business Value. עלייה בעלות יכולה להיות חיובית אם ירדו שעות ספק או Cycle Time. `/insights` יכול לעזור לזהות דפוסי שימוש ונקודות חיכוך מקומיות. StackAI מחפשת Optimization בעל ערך ולא חיסכון Token בכל מחיר.

**Metadata:** `category=operations_support` · `subcategory=operations_support` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_204 — Feature Gate ו-Managed Settings Review

Feature חדש עובר Gate: האם הלקוח צריך אותו, מה הסיכון, איך בודקים ומה ה-Pilot. Managed Settings נבדקות במקביל כדי לוודא שה-Policy עדיין מתאימה. אין להפעיל Feature חדש בכל הארגון רק משום שהוא יצא; שינוי Capability הוא שינוי Governance.

**Metadata:** `category=operations_support` · `subcategory=settings` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_205 — Monitoring, Backup, Change Management ו-Rollback

Monitoring צריך להמשיך לעבוד, Backup צריך לכלול Configuration לא-סודי, וכל שינוי משמעותי ב-Permissions/MCP/Hooks/Agents עובר Change Management. לכל שינוי יש Owner, Test ו-Rollback. Secrets אינם נכנסים ל-Git; Configuration כן. אם Monitoring נופל בשקט, יש לבדוק גם את Pipeline עצמו.

**Metadata:** `category=operations_support` · `subcategory=monitoring` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_206 — Onboarding ו-Offboarding של משתמשים וספקים

Onboarding של משתמש כולל Account, Repository, Claude Code, Training, Permissions ו-Approved MCP. Offboarding מסיר Claude, GitHub, Cloud, VPN, MCP, SSH ו-Tokens ומסובב Shared Secrets אם נדרש. אותו עיקרון חל על ספקים. Lifecycle מתועד מונע גישה שנשארת אחרי עזיבה.

**Metadata:** `category=operations_support` · `subcategory=vendor_management` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_207 — Monthly, Quarterly ו-Annual Operations Review

StackAI מציעה cadence של Review: שבועי למערכות רגישות ול-Incidents, חודשי ל-Usage/Cost/Permissions/MCP, רבעוני ל-Security/Governance ו-Annual Review לארכיטקטורה ואסטרטגיה. המטרה היא להתאים את הסביבה לשינוי בעסק בלי לייצר תחזוקה מיותרת.

**Metadata:** `category=operations_support` · `subcategory=operations_support` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`

## stk_208 — Maturity Levels, Health Score ו-Golden Configuration

Maturity Levels נעים מ-Installed דרך Managed, Integrated ו-Governed עד Optimized. Health Score יכול למדוד Version, Security, Governance, Documentation, Integrations, Monitoring, Cost ו-Business Value. Golden Configuration היא גרסה ידועה וטובה של Settings, Skills, Hooks, MCP ו-Agents שניתן להשוות אליה בעת תקלה או Drift.

**Metadata:** `category=operations_support` · `subcategory=operations_support` · `intent=operations` · `risk=low` · `platform=all` · `last_verified=2026-10`
