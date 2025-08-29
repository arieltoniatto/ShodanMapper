import os
import shodan
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
API_KEY = os.getenv("SHODAN_API_KEY")
if not API_KEY:
    raise ValueError("Please set SHODAN_API_KEY in your .env file.")

api = shodan.Shodan(API_KEY)

def search_shodan(query, limit=100):
    """
    Search Shodan using a query string.
    Returns a pandas DataFrame with IP, port, service, banner, org, location.
    """
    results = []
    try:
        response = api.search(query, limit=limit)
        for match in response['matches']:
            results.append({
                "ip": match.get("ip_str"),
                "port": match.get("port"),
                "service": match.get("product") or "unknown",
                "banner": match.get("data", "")[:100].replace("\n", " ").replace("\r", " "),
                "org": match.get("org") or "unknown",
                "location": f"{match.get('location', {}).get('city', '')}, {match.get('location', {}).get('country_name', '')}"
            })
        return pd.DataFrame(results)
    except shodan.APIError as e:
        print("Shodan API Error:", e)
        return pd.DataFrame([])
