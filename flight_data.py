class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self, flights_list: list):
        self.flights = flights_list
        self.list_of_available_options = []

    def format_available_options(self):
        for flight in self.flights:
            if flight["_results"] == 0:
                pass
            else:
                formatted_data_to_dict = {
                    "airportCodeFrom": flight["data"][0]["flyFrom"],
                    "airportCodeTo": flight["data"][0]["flyTo"],
                    "cityFrom": flight["data"][0]["cityFrom"],
                    "cityTo": flight["data"][0]["cityTo"],
                    "fromDate": flight["data"][0]["route"][0]["local_departure"].split("T")[0],
                    "toDate":
                        flight["data"][0]["route"][len(flight["data"][0]["route"]) - 1]["local_arrival"].split("T")[0],
                    "price": flight["data"][0]["price"]
                }
                self.list_of_available_options.append(formatted_data_to_dict)

        if len(self.list_of_available_options) == 0:
            return "no flights available"
        else:
            return self.list_of_available_options
