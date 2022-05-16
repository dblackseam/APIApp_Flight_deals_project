import requests
import os

SHEETBEST_ENDPOINT = os.environ["SHEETBEST_ENDPOINT"]
TEQUILA_IATA_ENDPOINT = "http://tequila-api.kiwi.com/locations/query"


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.sheet_contents = []

    def get_data(self, outsourse_data: bool = True):
        if outsourse_data:
            sheet_response = requests.get(SHEETBEST_ENDPOINT)
            self.sheet_contents = sheet_response.json()
        else:
            self.sheet_contents = [
                {'City': 'Paris', 'IATA Code': 'PAR', 'Lowest Price': '54'},
                {'City': 'Berlin', 'IATA Code': 'BER', 'Lowest Price': '42'},
                {'City': 'Tokyo', 'IATA Code': 'TYO', 'Lowest Price': '485'},
                {'City': 'Sydney', 'IATA Code': 'SYD', 'Lowest Price': '551'},
                {'City': 'Istanbul', 'IATA Code': 'IST', 'Lowest Price': '95'},
                {'City': 'Kuala Lumpur', 'IATA Code': 'KUL', 'Lowest Price': '414'},
                {'City': 'New York', 'IATA Code': 'NYC', 'Lowest Price': '240'},
                {'City': 'San Francisco', 'IATA Code': 'SFO', 'Lowest Price': '260'},
                {'City': 'Capetown', 'IATA Code': 'CPT', 'Lowest Price': '378'}
            ]
        return self.sheet_contents

    def add_iata_codes(self):
        current_row = 0
        for row in self.sheet_contents:
            tequila_body = {
                "term": row["City"]
            }
            tequila_header = {
                "apikey": os.environ["TEQUILA_API_KEY"]
            }

            iata_code = requests.get(TEQUILA_IATA_ENDPOINT, params=tequila_body, headers=tequila_header)
            iata_code.raise_for_status()
            code = iata_code.json()["locations"][0]["code"]

            sheetbest_body = {
                "IATA Code": code
            }

            tequila_response = requests.patch(f"{SHEETBEST_ENDPOINT}/{current_row}", json=sheetbest_body)
            tequila_response.raise_for_status()

            current_row += 1
