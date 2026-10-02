# StackAI Website

`index.html` הוא קובץ ה־Source of Truth של ממשק StackAI.

## מצב נוכחי

- RTL
- Responsive
- Luxury Light / Premium Consulting design
- Demo mode
- StackAI Advisor UI
- 8-question readiness demo
- Readiness score
- Polling-ready JavaScript

## חיבור ל־n8n

בתוך `index.html` קיימת הגדרת `CONFIG`.

כל עוד:

```javascript
USE_MOCK_API: true
```

האתר עובד ללא Backend.

לחיבור אמיתי:

1. שנה ל־`false`.
2. הגדר `START_ENDPOINT`.
3. הגדר `STATUS_ENDPOINT`.
4. ודא שה־CORS ב־Backend מאפשר את מקור האתר.

אין לשנות את מבנה ה־Polling ללא עדכון מקביל ב־n8n.