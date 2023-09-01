import login
import search_train
import search_station
from datetime import datetime
import book_ticket
from wallet import wallet

if __name__ == "__main__":
    run, user = login.entry()
    # run, user = True, "Saikat Saha"
    if run:
        print(f"\nWelcome {user.split(' ')[0]},")
    while run:
        book_ticket.refresh()
        time_obj = datetime.now()
        print(f"\nTime : {time_obj.strftime('%H:%M')}\nDate : {time_obj.strftime('%d-%b-%Y')}\n\nMENU :\n1. Book ticket\n2. Search train\n3. Search station\n4. Show ticket\n5. Wallet\n6. Log out")
        try :
            choice = int(input("Enter choice : "))
        except :
            print("\nWrong choice, try again !\n")
            continue

        if (choice == 1):
            NOTbooked = True
            while NOTbooked:
                print("\nBook ticket\n-----------\n")
                src = input("Enter Source Station : ")
                dest = input("Enter Destination Station : ")
                try : 
                    adult = int(input("Enter the number of adults : "))
                    child = int(input("Enter the number of childs : "))
                except :
                    print("\nWrong choice, try again !")
                    continue
                print()

                status = book_ticket.ticket(src, dest, adult, child)

                break

        elif (choice == 2):
            NOTsearched = True
            while NOTsearched:
                print("\nSearch train\n------------")

                src = input("Enter Source Station : ")
                dest = input("Enter Destination Station : ")

                print()

                NOTsearched = not search_train.searchT(src, dest)

        elif (choice == 3):
            NOTsearchedST = True
            while NOTsearchedST:
                print("\nSearch station\n--------------")
                station = input("Enter station to search : ")

                print()

                NOTsearchedST = not search_station.searchS(station)
        
        elif (choice == 4):
            print("\nShow ticket\n-----------")
            book_ticket.show_ticket()

        elif (choice == 5):
            wallet_visit = True
            my_wallet = wallet()
            while wallet_visit:
                print("\nWallet\n------")
                print("Menu :\n1. Add money\n2. Show balance\n3. Exit")
                try :
                    choice = int(input("Enter choice : "))
                except :
                    print("\nWrong choice, try again !")
                    continue

                if (choice == 1):
                    NOTcredited = True
                    while NOTcredited:
                        try:
                            money = float(input("Enter money to add : "))
                            NOTcredited = not my_wallet.credit(money)
                            print()
                        except:
                            pass

                elif (choice == 2):
                    balance = my_wallet.show_balance()
                    print(f"\nCurrent balance : {balance}")
                
                elif (choice == 3):
                    wallet_visit = False
                
                else:
                    print("\nWrong choice, try again !")

        elif (choice == 6):
            print("\nLogged out !\n")
            run, user = login.entry()

        print()