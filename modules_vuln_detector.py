import requests

def detect_vulnerabilities(target):
    # Basic example: Check for common vulnerabilities like open directories or SQL injection hints
    try:
        response = requests.get(target)
        if response.status_code == 200:
            if "sql syntax" in response.text.lower():  # Naive check
                return {"vulnerability": "Potential SQL Injection"}
            else:
                return {"status": "No obvious vulnerabilities detected"}
        else:
            return {"error": f"HTTP Status: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}