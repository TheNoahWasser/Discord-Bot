def fetchKey():
    with open("api_key", "r") as file:
        return file.read()

def main():
    apikey = fetchKey()
    print("ooga")
    print(apikey)
    print("booga")

if __name__ == "__main__":
    main()