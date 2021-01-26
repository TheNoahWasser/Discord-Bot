import os
from classes import Account
import pickle

logBarrier = "-----------------------------------------------------"

def fetchKey():
    print(logBarrier)
    print("Getting API-Key...")
    with open("api_key", "r") as file:
        print("Got Key. Key is: " + file.read())
        print(logBarrier)
        return file.read()

def fetchAccounts():
    accountCount = 0
    print(logBarrier)
    print("Fetching Accounts...")
    with os.scandir() as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith(".account"):
                accountCount += 1
                print(entry.name)
                with open(entry.path) as file:
                    print("nix hier")
        print("\nFound " + str(accountCount) + " Accounts.")
    print("Fetching Accounts done.")
    print(logBarrier)
    return

def main():
    apikey = fetchKey()
    accounts = []
    acc = Account("xdddd","123456789","BRONZE", "I", 65)
    accounts.append(acc)
    #accounts.append(Account("xdddd","123456789","BRONZE", "I", 65))
    acc.save()
    fetchAccounts()

if __name__ == "__main__":
    main()