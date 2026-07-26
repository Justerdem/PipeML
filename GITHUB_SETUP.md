# GitHub setup steps

## 1. Create a repository on GitHub

Create a new empty repository on GitHub. Do not initialize it with a README, .gitignore, or license.

## 2. Connect the local repository

Run these commands in the project folder:

```bash
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY_NAME>.git
git branch -M main
git push -u origin main
```

## 3. If GitHub prompts for authentication

If you are using HTTPS, GitHub will ask for your username and a Personal Access Token (PAT), not your password.

## 4. Optional: verify the remote

```bash
git remote -v
```
