import addition_function as add_m
import subtraction_function as sub_m

def main():
    no1= int(input("Enter no1: "))
    no2= int(input("Enter no2: "))
    # call to addition modules function
    add_result = add_m.Additon(no1,no2)
    print("Addition result :", add_result)
    # call to subtraction modules function
    sub_result = sub_m.Subtraction(no1,no2)
    print("Subtraction result :", sub_result)

if __name__ == '__main__':
    main()