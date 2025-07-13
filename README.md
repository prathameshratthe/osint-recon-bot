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

## 🔧 Installation (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/prathameshratthe/osint-recon-bot.git
cd osint-recon-bot
2. Run Backend
bash
Copy
Edit
cd app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Runs at: http://127.0.0.1:8000

3. Run Frontend
bash
Copy
Edit
cd ../frontend
npm install
npm run dev
Runs at: http://localhost:5173

🌐 Live Deployment
🔗 Frontend: https://osint-recon-bot.vercel.app

🔗 Backend: https://osint-recon-bot-production.up.railway.app

📦 API Usage
Scan Endpoint
POST /scan
Body:

json
Copy
Edit
{
  "url": "example.com"
}
Upload Endpoint
POST /upload
For uploading a DOCX and generating extended info.

📄 License
MIT © 2025 Prathamesh Ratthe

yaml
Copy
Edit

---

Let me know if you'd like:

- A version with images, badges (build/deploy status),
- Support for Docker,
- Or step-by-step deploy instructions for Railway/Vercel in the README.
