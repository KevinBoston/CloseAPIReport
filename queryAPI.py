from closeio_api import APIError, Client
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
api = Client(API_KEY)

def query():
  #Mimic search endpoint JSON, needs additional filtering
  search_payload = {
        "query": {
            "type": "and",
            "queries": [
                {"type": "object_type", "object_type": "lead"},
                {
                    "type": "field_condition",
                    "field": {
                        "type": "regular_field",
                        "object_type": "lead",
                        "field_name": "date_created"
                    },
                    "condition": {
                        "type": "date_range",
                        "gte": "2026-03-01"  # Since March
                    }
                }
            ]
        }
    }

    results = api.post('data/search', data=search_payload)
    #Post to /data/search endpoint to 
    #Then iterate through results to verify they are correct
    for lead in results.get('data', []):
        print(f"Lead: {lead['display_name']} | Created: {lead['date_created']}")

    if __name__ == "__main__":
        query()
