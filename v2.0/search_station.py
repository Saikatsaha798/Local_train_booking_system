import json
from prettytable import PrettyTable

def searchS(text):
    station = [["Station Code", "Station Name"]]
    with open("assets/station_filtered.json", "r") as f:
        stations = json.load(f)
    no_stations = 0

    for i in sorted(stations):
        if text.lower() in stations[i]["name"].lower():
            name = stations[i]["name"].split(" ")
            # print(name, len(name))
            if len(name)<3:
                station.append([i, stations[i]["name"]])
            else:
                station.append([i, " ".join(name[:4])])
            no_stations += 1

    # station.title = f"Stations List ({no_stations} found)"
    # print(station)

    if no_stations == 0:
        return False, station
    else:
        return True, station

if __name__ == "__main__":
    text = input("Enter for search : ")
    print(searchS(text))