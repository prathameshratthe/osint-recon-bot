# 🕵️‍♂️ OSINT Recon Bot

A web-based Open Source Intelligence (OSINT) Reconnaissance tool that scans domains using public APIs and provides a downloadable report.

---

## 🚀 Features

- 🌐 Domain reconnaissance with `ipwhois.io`
- 📄 Downloadable `.docx` report
- 📦 Frontend in Vite + React
- 🔙 Backend in FastAPI (Python)
- ☁️ Hosted using Vercel (Frontend) + Railway (Backend)

---

## 🛠️ Tech Stack

| Layer     | Tech                      |
|-----------|---------------------------|
| Frontend  | Vite + React              |
| Backend   | FastAPI + Uvicorn         |
| Styling   | TailwindCSS               |
| Hosting   | Vercel (Frontend)         |
| Backend Hosting | Railway             |
| Docs      | `python-docx`             |

---

## 🔧 Installation Guide

### 📦 Requirements

- Python 3.10+
- Node.js 18+
- npm 9+
- Git

---

## 🖥️ Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/prathameshratthe/osint-recon-bot.git
cd osint-recon-bot
```
### 2. Backend Setup (FastAPI)
```bash
cd app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Frontend Setup (React + Vite)
```bash
cd ../frontend
npm install
npm run dev
```

🌐 Live Deployment
🔗 Frontend: https://osint-recon-bot.vercel.app
🔗 Backend: https://osint-recon-bot-production.up.railway.app


📄 License
MIT © 2025 Prathamesh Ratthe

