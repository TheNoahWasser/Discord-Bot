import os

logBarrier = "-----------------------------------------------------"

def fetchKey():
    print(logBarrier)
    print("Getting API-Key...")
    with open("api_key", "r") as file:
        print("Got Key. Key is: " + file.read())
        print(logBarrier)
        return file.read()

def fetchAccounts():
    print(logBarrier)
    print("Fetching Accounts...")
    with os.scandir() as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith(".py"):
                print(entry.name)
    print("Fetching Accounts done")
    print(logBarrier)
    return

def main():
    apikey = fetchKey()
    fetchAccounts()

if __name__ == "__main__":
    main()