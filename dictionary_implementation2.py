def main():
    #dictionary
    fees = {"PPA": 12000, "PPA2": 13000,  "PPA3": 14000, "PPA4": 18000}
    print("Fees:", fees)
    print("Please enter batch name:")
    batch = input()
    if batch in fees:
        print("Fees are :", fees[batch])
    else:
        print("Batch not found.")

if __name__ == "__main__":
    main()

