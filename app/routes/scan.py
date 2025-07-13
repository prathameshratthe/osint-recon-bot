from fastapi import APIRouter
from models.schemas import ScanRequest
from app.services.osint import fetch_crtsh, fetch_whois
from app.utils.gemini import summarize_osint

router = APIRouter()
    
from app.services.osint import (
    fetch_crtsh, fetch_whois,
    fetch_hunter_emails, fetch_wayback, fetch_virustotal
)

@router.post("/scan")
async def scan_target(request: ScanRequest):
    domain = request.target
    ip = request.target

    crtsh_data = await fetch_crtsh(domain)
    whois_data = await fetch_whois(domain)
    hunter_data = await fetch_hunter_emails(domain)
    wayback_data = await fetch_wayback(domain)
    vt_data = await fetch_virustotal(domain)

    # Combine all OSINT data
    osint_results = {
        "crtsh": crtsh_data,
        "whois": whois_data,
        "hunter": hunter_data,
        "wayback": wayback_data,
        "virustotal": vt_data
    }

    summary = await summarize_osint(osint_results)

    return {
        "target": domain,
        "osint": osint_results,
        "summary": summary
    }
