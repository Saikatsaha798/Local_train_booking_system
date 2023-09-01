from getpass import getpass
from prettytable import PrettyTable
import os
import pickle
from cryptography.fernet import Fernet

def signup():
    if "user_data" in os.listdir("data"):
        with open("data//user_data", "rb") as f:
            UserData = pickle.load(f)
        key = UserData["key_FERNET"]
    else:
        UserData = dict()
        key = Fernet.generate_key()
        UserData["key_FERNET"] = key

    fernet = Fernet(key)

    print("\nSignUp\n-------")

    while True:
        usr = input("Enter Username : ")
        if (usr in UserData.keys() or usr == ""):
            print("\nUsername not available !\n")
        else:
            break
    while True:
        pas = getpass("Enter Password : ")
        pasN = getpass("Enter Password again : ")

        if pas == pasN and pas != "":
            UserData[usr] = fernet.encrypt(bytes(pas, "utf-8"))
            with open("data//user_data", "wb") as f:
                pickle.dump(UserData, f)
            print("\nUser added !\n")
            break
        else:
            print("\nPasswords do not match !\n")    

def login():
    if "user_data" in os.listdir("data"):
        with open("data//user_data", "rb") as f:
            UserData = pickle.load(f)
        key = UserData["key_FERNET"]
        fernet = Fernet(key)
    else:
        print("\nNo data present, try signing up !\n")
        return False, "NA"

    print("\nLogin\n-------")

    usr = input("Enter Username : ")
    if usr in UserData.keys():
        pas = getpass("Enter Password : ")
        if fernet.decrypt(UserData[usr]).decode() == pas:
            print("\nLogged in !\n")
            return True, usr
        else:
            print("\nWrong password !\n")
            return False, usr
    else:
        print(f"\n{usr} username not in data !\n")
        return False, usr
    
def entry():
    if "data" not in os.listdir():
        os.mkdir("data")
    locked = True
    while (locked):
        print("Welcome to E-Ticket,\nChoose from below :\n1. Login\n2. Signup\n3. Exit")
        try : 
            choice = int(input("Enter choice : "))
        except :
            print("\nWrong choice, try again !\n")
            continue

        if (choice == 1):
            locked, user = login()
            locked = not locked
        elif (choice == 2):
            signup()
        elif (choice == 3):
            print("\nThanks for using !\n")
            return False, "NA"
        else:
            print("\nWrong choice !\n")
        
    return True, user

if __name__ == "__main__":
    entry()

