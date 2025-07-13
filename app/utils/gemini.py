import httpx
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="C:/Users/prath/OneDrive - rknec.edu/Desktop/VII/osint_recon_bot/app/.env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
GEMINI_VISION_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-vision:generateContent"


HEADERS = {
    "Content-Type": "application/json"
}

async def summarize_osint(osint_data: dict):
    prompt = f"""
    You are an OSINT analyst. Analyze the following reconnaissance data and summarize:
    1. Risky subdomains, infrastructure, or exposed ports
    2. Any email leaks or sensitive records
    3. CVE or malware indicators
    4. Historical presence from Archive
    5. Recommendations

    OSINT DATA:\n{osint_data}
    """

    body = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{GEMINI_URL}?key={GEMINI_API_KEY}",
                headers=HEADERS,
                json=body
            )
            return response.json()
    except Exception as e:
        return {"error": str(e)}


async def analyze_image(base64_img: str):
    prompt = """
You are an AI trained in detecting visual signs of phishing, fraud, and spoofed websites.
Analyze this screenshot for:

1. Impersonation (logos, brand names)
2. Suspicious design traits (login forms, misspellings, fake buttons)
3. Security indicators (or lack of them)
4. Recommendations
"""

    body = {
        "contents": [
            {
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": "image/png",
                            "data": base64_img
                        }
                    },
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{GEMINI_VISION_URL}?key={GEMINI_API_KEY}",
                headers=HEADERS,
                json=body
            )
            return response.json()
    except Exception as e:
        return {"error": str(e)}
