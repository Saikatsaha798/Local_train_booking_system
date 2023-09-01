import json
import pickle
import os
from datetime import datetime, timedelta
from wallet import wallet

def refresh():
    if ("ticket_data" in os.listdir("data")):
        with open("data//ticket_data", "rb") as f:
            tickets = pickle.load(f)
    else:
        tickets = {}  

    time_obj = datetime.now()
    for i in sorted(tickets.keys(), reverse=False):
            if tickets[i]["valid"]:
                # print(time_obj-i > timedelta(hours=3))
                if ((time_obj-i)>timedelta(hours = 3)):
                    tickets[i]["valid"] = False
    
    with open("data//ticket_data", "wb") as f:
        pickle.dump(tickets, f)

def get_fare(src, dest, adult, child):
    src = src.upper()
    dest = dest.upper()

    child /= 2

    with open("assets/station_filtered.json", "r") as f:
        station = json.load(f)

    if (src in station.keys() and dest in station.keys()) and (station[src]["coordinates"] is not None and station[dest]["coordinates"] is not None):

        distance = (station[src]["coordinates"][0] - station[dest]["coordinates"][0])**2 + (station[src]["coordinates"][1] - station[dest]["coordinates"][1])**2
        fareCost = 10 + (distance * 15.641993980131867)
        
        fareCost = round(fareCost/10)*10

        fareCost *= (child + adult)
    
        return True, round(fareCost)
    
    else:
        return False, 0

def book(src, dest, adult, child):
    found, fare = get_fare(src, dest, 1, 1)

    time_obj = datetime.now()
    time = time_obj.strftime("%H:%M:%S")
    date = time_obj.strftime("%d-%b-%Y")

    if ("ticket_data" in os.listdir("data")):
        with open("data//ticket_data", "rb") as f:
            tickets = pickle.load(f)
    else:
        tickets = {}  
    
    found, fare = get_fare(src, dest, adult, child)

    # print(found, fare)
    if found:
        # time_now = time_obj.strftime('%Y-%m-%d %H:%M:%S')
        # print(time_now)

        tickets[time_obj] = {
            "time" : time,
            "date" : date,
            "source" : src,
            "destination" : dest,
            "valid" : True,
            "fare" : fare,
            "adult" : adult,
            "child" : child
        }
        # print(tickets)

        # with open("ticket_data", "wb") as f:
        #     pickle.dump(tickets, f)
        # print(f"Fare is {fare}")

        return True, fare, tickets
    else:
        # print("\nStation not found\n")
        return False, 0, tickets

def ticket(tickets, fare):
    # status, fare, tickets = book(src, dest, adult, child)
    # print(tickets)
    wallet_now = wallet()

    # if status:
        # con = input(f"Do you want to continue, Rs {fare} will be deducted from your wallet ? (y/n) : ")
        # print()
        # if con == "Y" or con == "y":
    paid = wallet_now.debit(fare)
    if paid:
        with open("data//ticket_data", "wb") as f:
            pickle.dump(tickets, f)
        # print("Ticket booked successfully !")
        return True
    return False
        # else:
        #     print("Payment cancelled !")
        #     return False

    # else:
    #     return False, "Stations not found !"

def show_ticket():
    if ("ticket_data" in os.listdir("data")):
        with open("data//ticket_data", "rb") as f:
            tickets = pickle.load(f)
        
        title = list(next(iter(tickets.values())).keys())
        # ut = title.index('valid')
        title.remove('valid')
        ticket_table = [title]
        for i in sorted(tickets.keys(), reverse=True):
            if tickets[i]["valid"]:
                a = list(tickets[i].values())
                a.pop(4)
                ticket_table.append(a)
        # print(ticket_table)
        if len(ticket_table) == 1:
            return False, ticket_table
        else:
            return True, ticket_table

    else:
        # print("No tickets found !")
        return False, []



if __name__ == "__main__":
    # src = input("Enter source station : ")
    # dest = input("Enter destination station : ")
    
    
    # found = ticket(src, dest, 1, 1)

    # if found:
    #     print(f"Fare is {fare}")
    # else:
    #     print("Station not found")

    # print(ticket(src, dest, 1, 1))
    print(show_ticket())
    # a, l = show_ticket()
    # for i in l:
    #     print(list(i))
    refresh()
