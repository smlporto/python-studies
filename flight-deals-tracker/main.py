from data_manager import *
from flight_data import *
from flight_search import *
from notification_manager import *
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_data()

flight_search = FlightSearch()

ORIGIN_CITY = "SAO"

for row in sheet_data:
    if row[1] != "":
        pass
    else:
        row[1] = flight_search.add_iataCode(row[0])
    
data_manager.destiny_info = sheet_data
data_manager.update_data()

tomorrow = datetime.now() + timedelta(days = 1)
six_months_period = datetime.now() + timedelta(days = 6 * 30)

for i, destination in enumerate(sheet_data):
    if i > 0:
        flight = flight_search.check_for_flights(
            ORIGIN_CITY,
            destination[1],
            from_date=tomorrow,
            to_date=six_months_period
        )