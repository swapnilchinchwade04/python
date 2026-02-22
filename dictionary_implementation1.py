def main():
    #       [Python, PPA, Logic Building, Angular]
    fees =  [10000,12000,13000,14500]
    print("Fees:", fees)

    print("Please enter batch name:")
    batch_name = input()

    if batch_name == "Python":
        print("Fees are :", fees[0])
    elif batch_name == "PPA":
        print("Fees are :", fees[1])
    elif batch_name == "Logic Building":
        print("Fees are :", fees[2])
    elif batch_name == "Angular":
        print("Fees are :", fees[3])
    else:
        print("No batch available.")


if __name__ == "__main__":
    main()