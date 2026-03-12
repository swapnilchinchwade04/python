def funR(no):
    if no>0:
        print("Inside funR")
        no=no-1
        funR(no)    # recusive call

def main():
    funR(3)

if __name__ == "__main__":
    main()
