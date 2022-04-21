import requests
from datetime import datetime, timedelta
import os

TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
TEQUILA_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self, all_the_sheet_data: list):
        self.sheet_data = all_the_sheet_data
        self.flights = []

    def search_for_flights(self):
        current_date = datetime.now().date()
        tomorrow_date = current_date + timedelta(days=1)
        date_in_six_months = current_date + timedelta(weeks=24)
        fly_from = "LON"
        min_nights_in_dst = "7"
        max_nights_in_dst = "28"
        flight_type = "round"
        currency = "GBP"
        sort = "price"
        output_limit = 1

        for row in self.sheet_data:
            search_body = {
                "fly_from": fly_from,
                "fly_to": row["IATA Code"],
                "date_from": tomorrow_date.strftime("%d/%m/%G"),
                "date_to": date_in_six_months.strftime("%d/%m/%G"),
                "nights_in_dst_from": min_nights_in_dst,
                "nights_in_dst_to": max_nights_in_dst,
                "price_to": row["Lowest Price"],
                "curr": currency,
                "limit": output_limit,
                "flight_type": flight_type,
                "sort": sort
            }
            tequila_header = {
                "apikey": TEQUILA_API_KEY
            }
            flights_response = requests.get(
                TEQUILA_SEARCH_ENDPOINT,
                params=search_body,
                headers=tequila_header
            )
            flights_response.raise_for_status()
            flights_info = flights_response.json()
            self.flights.append(flights_info)

        return self.flights
