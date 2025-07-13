import httpx

# ---- 1. crt.sh ----
async def fetch_crtsh(domain: str):
    url = f"https://crt.sh/?q={domain}&output=json"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"crt.sh status {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


# ---- 2. Whois (Using https://api.ipwhois.io or similar free service) ----
async def fetch_whois(domain: str):
    api_key = "oyAr3jLJypOJvshUAbOdaQ==Perpmc3uTGkC6hUJ"  # Optional
    url = f"https://api.api-ninjas.com/v1/whois?domain={domain}"
    headers = {"X-Api-Key": api_key}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            return response.json()
    except Exception as e:
        return {"error": str(e)}


async def fetch_hunter_emails(domain: str):
    HUNTER_API_KEY = "c4a6ffbca62821c33a4bb574f722f1a2ff499302"
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.json()
    except Exception as e:
        return {"error": str(e)}

async def fetch_wayback(domain: str):
    url = f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&limit=5&fl=timestamp,original&collapse=urlkey"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Wayback status {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

async def fetch_virustotal(domain: str):
    VT_API_KEY = "958f4afb1678d99cec62a9a9c7b1769e832581c4ee0e7d8391a6629f40707181"
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {
        "x-apikey": VT_API_KEY
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            return response.json()
    except Exception as e:
        return {"error": str(e)}
