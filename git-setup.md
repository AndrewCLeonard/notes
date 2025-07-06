# 🧠 README: How to Push This Local Repo to GitHub (Every Time)

---

## ✅ STEP 1: Create the GitHub Repo in Your Browser

1. Go to [github.com/new](https://github.com/new)
2. Name it (e.g. `notes`)
3. **DO NOT initialize with a README** (you already have one)
4. Click **Create Repository**
5. Copy the remote URL (SSH or HTTPS)

---

## ✅ STEP 2: Run These Commands in Terminal (Inside Your Repo Folder)

**Open the terminal in VS Code:**
```bash
cd path/to/your/notes
```

**Initialize Git if you haven’t yet:**
```bash
git init
```

**Add everything and commit it:**
```bash
git add .
git commit -m "Initial commit"
```

**Link to the remote GitHub repo:**
```bash
git remote add origin git@github.com:your-username/notes.git
```

**Push to GitHub:**
```bash
git push -u origin main
```

---

## 🔐 STEP 3: Protect Secrets and Environment Variables

**✅ Do this before pushing anything sensitive!**

1. **Create a `.gitignore` file** (in your repo root) and add:
    ```gitignore
    # Ignore all env files
    *.env

    # Optional: ignore the folder where you store secrets
    env_files/
    ```

2. **Move your `.env` files into a subfolder** like `env_files/` to stay organized:
    ```
    notes/
    ├── env_files/
    │   ├── dashboard1.env
    │   └── dashboard2.env
    ```

3. **If you already committed a `.env` file, remove it from Git:**
    ```bash
    git rm --cached path/to/file.env
    git commit -m "Remove tracked secret"
    ```

4. **Create a `.env.example` file** to document required secrets:
    ```env
    API_KEY=your-api-key-here
    SHEET_ID=your-sheet-id-here
    ```

---

## 🔁 Common Pitfall Fixes

**Check your remote URL:**
```bash
git remote -v
```

**Remove incorrect remote and re-add:**
```bash
git remote remove origin
git remote add origin <correct-URL>
```

**If you see this error:**
```
error: src refspec main does not match any
```

Run:
```bash
git branch -M main
git push -u origin main
```

---

## 📌 TL;DR COMMAND CHEAT SHEET

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:your-username/notes.git
git branch -M main
git push -u origin main
```

---

*Keep this file in your repo forever so you never have to ask again.* 💪
