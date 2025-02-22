import requests
from dotenv import load_dotenv
from pprint import pprint
import os

load_dotenv()
api_key = os.getenv("SHEETY_API")


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "Authorization":f"bearer {api_key}"
        }

    

    def get_sheety_data(self):
        url = f"{self.base_url}"
        try:
            response = requests.get(self.base_url, headers=self.headers)
            response.raise_for_status()  # Kasta ett fel om statuskod är fel
            return response.json()  # Returnera JSON-datan
        except requests.exceptions.HTTPError as e:
            print(f"An error occurred: {e}")
            return None

    def update_entry(self, entry):
        edit_url = f"{self.base_url}/{entry['id']}"
        json_data = {
            "flight": {
            "iataCode": entry["iataCode"]
             }
            }

        response = requests.put(url=edit_url, headers=self.headers, json=json_data)
        response.raise_for_status()
        print(f"Row {entry['id']} has been updated with {entry['iataCode']}.")