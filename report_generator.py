import google.generativeai as genai
import json
import os
from datetime import datetime

def generate_report(scan_results, target):

    MY_API_KEY = "AIzaSyBoeag-78qKX5majHgf0g3ztEmHdSZTkkE"

    genai.configure(api_key=MY_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')

    scan_text = json.dumps(scan_results, indent=2)

    prompt = f"""
    You are a professional penetration tester.
    Analyze the Nmap scan results below and write a security report.

    TARGET: {target}
    DATE: {datetime.now().strftime("%Y-%m-%d %H:%M")}

    SCAN RESULTS:
    {scan_text}

    Write a report with these sections:

    1. EXECUTIVE SUMMARY
       - What was found, overall risk level

    2. OPEN PORTS AND SERVICES
       - Each port, what it does, why it could be risky

    3. VULNERABILITIES
       - Security issues found, mention CVEs if you know them

    4. RISK LEVEL FOR EACH FINDING
       - Critical / High / Medium / Low with explanation

    5. RECOMMENDATIONS
       - How to fix each issue, in priority order

    6. CONCLUSION
       - What to do immediately

    Be clear, specific and professional.
    """

    print("[*] Sending scan data to Gemini AI...")
    response = model.generate_content(prompt)
    return response.text


def save_report(report, target):
    os.makedirs("reports", exist_ok=True)
    filename = f"reports/report_{target.replace('.','_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    with open(filename, 'w') as f:
        f.write(report)
    print(f"[✓] Report saved to: {filename}")
    return filename

