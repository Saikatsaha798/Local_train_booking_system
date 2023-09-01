import json
from prettytable import PrettyTable

def searchS(text):
    station = PrettyTable(["Station Code", "Station Name"])
    with open("assets/station_filtered.json", "r") as f:
        stations = json.load(f)
    no_stations = 0

    for i in sorted(stations):
        if text.lower() in stations[i]["name"].lower():
            station.add_row([i, stations[i]["name"]])
            no_stations += 1

    station.title = f"Stations List ({no_stations} found)"
    print(station)

    if no_stations == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    text = input("Enter for search : ")
    searchS(text)