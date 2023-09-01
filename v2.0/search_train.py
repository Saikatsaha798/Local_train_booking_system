import json
from datetime import datetime

def searchT(src: str, dest: str):
    train_data = [["S.No.", "Arrival Time", "Departure Time", "Train Number", "Train Name"]]

    with open("assets/timetable_filtered.json", "r") as f:
        time_table = json.load(f)

    src = src.upper()
    dest = dest.upper()

    if src not in time_table.keys() or dest not in time_table.keys():
        # print("Wrong station codes given !")
        return False, []

    trains = 0

    for i in sorted(time_table[src]):
        # time = "00:00:00"
        time_obj = datetime.now()
        time = time_obj.strftime("%H:%M:%S")
        if i > time:
            for j in sorted(time_table[dest]):

                if j > i and time_table[src][i]["train_number"] == time_table[dest][j]["train_number"]:
                    # print(time_table[src][i]["train_name"], time_table[src][i]["train_number"], time_table[dest][j]["train_name"],
                    #       time_table[dest][j]["train_number"])
                    trains += 1
                    arrival = time_table[src][i]['arrival']

                    if arrival != "None":
                        arrival = ":".join(arrival.split(":")[0:2])
                    else:
                        arrival = "START"

                    train_data.append([trains, arrival, ":".join(time_table[src][i]['departure'].split(":")[0:2]),
                                        time_table[src][i]['train_number'], time_table[src][i]['train_name']])
                    break
    # train_data.title = f"Trains List ({trains} found)"

    if trains == 0:
        # print("No trains available now !")
        # print(train_data)
        return False, train_data
    else:
        # print(f"{trains} trains founds !")
        # print(train_data)
        return True, train_data
    # return True


if __name__ == "__main__":
    src = input("Enter the Source station : ")
    dest = input("Enter the Destination station : ")
    print()
    searchT(src, dest)
