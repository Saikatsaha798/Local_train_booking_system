import os
import pickle
from cryptography.fernet import Fernet

class wallet :
    def __init__(self):
        self.wallet_history = {}
        if "user_data" in os.listdir("data"):
            with open("data//user_data", "rb") as f:
                UserData = pickle.load(f)
            key = UserData["key_FERNET"]

        else:
            UserData = dict()
            key = Fernet.generate_key()
            UserData["key_FERNET"] = key
            with open("data//user_data", "wb") as f:
                pickle.dump(UserData, f)
        
        self.fernet = Fernet(key)

        if "wallet_data" in os.listdir("data"):
            with open("data//wallet_data", "rb") as f:
                self.wallet_history = pickle.load(f)
            self.balance = float(self.fernet.decrypt(self.wallet_history["balance"]).decode())
        else:
            self.balance = 0.0
            self.save()

    def save(self):
        self.wallet_history["balance"] = self.fernet.encrypt(bytes(str(self.balance), "utf-8"))

        with open("data//wallet_data", "wb") as f:
            pickle.dump(self.wallet_history, f)

    def debit(self, price):
        if self.balance < price:
            # print("Insufficient balance, try adding money !")
            return False
        else:
            self.balance -= price
            # print("Payment successfully completed !")
            self.save()
            return True

    def credit(self, price):
        if price < 100:
            # print("\nMinimum that can be added : Rs 100")
            return False
        else:
            self.balance += price
            # print(f"\nRs {price} added to wallet !")
            # print(self.balance)
            self.save()
            return True
        
    def show_balance(self):
        return self.balance


if __name__ == "__main__":
    wallet_0 = wallet()
    # print(wallet_0.credit(1000))
    wallet_0.credit(10)
    print(wallet_0.show_balance())
    # print(0.0<0.0)
