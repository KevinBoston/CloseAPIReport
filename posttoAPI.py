import csv, time
from closeio_api import APIError, Client
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
CSV_FILE_PATH = 'cleaned.csv'
api=Client(API_KEY)

def import_leads():
    with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as f:

        reader = csv.DictReader(f)

        for row in reader:
            try:

                payload = {
                    'name': row['company_name'],
                    'status_label': 'Potential',
                    'contacts': [{
                        'name': row['contact_name'],
                        'emails': [{'email': row['email']}]
                    }]
                }

                response = api.post('lead', data=payload)
                print(f"Successfully created: {response['display_name']}")
                time.sleep(1.1)

            except APIError as e:
                print(f"Failed to import {row.get('company_name')}: {e}")
            except KeyError as e:
                print(f"Column missing in CSV: {e}")
                break


if __name__ == "__main__":
    import_leads()
