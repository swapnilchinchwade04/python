# Write a recursive program which display below pattern.
# Input : 5
# Output : 1 2 3 4 5


def pattern_custom(no):
    temp = 0
    if no>0:
        no = no - 1
        pattern_custom(no)
        print(no + 1, end=" ")


def main():
    print("Enter number:")
    no=int(input())
    pattern_custom(no)

if __name__ == "__main__":
    main()