#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/faf2de50b2dee5618c30cc47685c1d58/flightDeals/flight"
ORIGIN_CODE = "ARL"

if __name__ == "__main__":
    data_manager = DataManager(SHEETY_PRICES_ENDPOINT)  # Skapar en instans med URL
    sheety_data = data_manager.get_sheety_data()  # Hämtar datan
    flight_info = FlightSearch()


    # for iata in sheety_data["flight"]:
    #     if iata["iataCode"] == "":
    #         iata["iataCode"] = "test"
    #         data_manager.update_entry(iata)  # Uppdaterar posten med "test"
    # else:
    #     print("Kunde inte hämta data.")
