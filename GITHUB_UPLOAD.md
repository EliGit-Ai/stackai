# העלאת StackAI ל־GitHub

ה־Repository מוכן להעלאה.

## אפשרות 1 — GitHub דרך שורת הפקודה

מתוך תיקיית הפרויקט:

```bash
git init -b main
git add .
git commit -m "Initial StackAI project repository"
```

צור Repository חדש וריק ב־GitHub, ואז:

```bash
git remote add origin https://github.com/<YOUR-USER>/stackai.git
git push -u origin main
```

## אפשרות 2 — GitHub Desktop

1. פתח GitHub Desktop.
2. Add existing repository / Create repository from the extracted folder.
3. ודא שה־Branch הוא `main`.
4. Publish repository.

## לפני Push

- ודא שאין `.env` אמיתי.
- אין להעלות API Keys או Tokens.
- אין להעלות Credentials של Pinecone, n8n או LLM provider.
- `website/index.html` הוא גרסת האתר הראשית.
- גרסאות V1–V3 אינן חלק מה־Repository הנקי.