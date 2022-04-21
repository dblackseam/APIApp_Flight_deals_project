import requests
import os

PUSHOVER_ENDPOINT = "https://api.pushover.net/1/messages.json"
PUSHOVER_PROJECT_TOKEN = os.environ["PUSHOVER_PROJECT_TOKEN"]
PUSHOVER_USER_KEY = os.environ["PUSHOVER_USER_KEY"]


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self, special_deals_data: list):
        self.data = special_deals_data

    def send_message(self):
        for flight in self.data:
            message = f"Low price alert! Only £{flight['price']} to fly from {flight['cityFrom']}-" \
                      f"{flight['airportCodeFrom']} to {flight['cityTo']}-{flight['airportCodeTo']}, " \
                      f"from {flight['fromDate']} to {flight['toDate']}."
            pushover_body = {
                "token": PUSHOVER_PROJECT_TOKEN,
                "user": PUSHOVER_USER_KEY,
                "message": message
            }
            requests.post(PUSHOVER_ENDPOINT, json=pushover_body)
