from pprint import pprint
from data_manager import *
from flight_data import *
from flight_search import *
from notification_manager import *

data_manager = DataManager()
sheet_data = data_manager.get_data()

flight_search = FlightSearch()

for row in sheet_data:
    if row["iataCode"]:
        pass
    else:
        row["iataCode"] = flight_search.add_iataCode(row["city"])
    
data_manager.destiny_info = sheet_data
data_manager.update_data()
        
print(sheet_data)