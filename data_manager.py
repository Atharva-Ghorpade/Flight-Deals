import os
import smtplib
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d0684b984e180ac45b31e794ec16b26b/flightDeals/prices"


class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.header = {
            'Authorization': 'Basic QXRoYXJ2YTE3MTA6QUA0MjEwOTc3'
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        print(response.status_code)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            url = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
            response = requests.put(url=url, json=new_data, auth=self._authorization)
            print(response.status_code)

