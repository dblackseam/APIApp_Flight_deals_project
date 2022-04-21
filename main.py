from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_data()

if sheet_data[0]["IATA Code"] == "":
    data_manager.add_iata_codes()

flight_search = FlightSearch(sheet_data)
raw_flights_data = flight_search.search_for_flights()

pprint(raw_flights_data)

data_formatter = FlightData(raw_flights_data)
formatted_flights_data = data_formatter.format_available_options()

if formatted_flights_data == "no flights available":
    pass
else:
    notification_manager = NotificationManager(formatted_flights_data)
    notification_manager.send_message()
