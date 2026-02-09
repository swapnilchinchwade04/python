def artihmatic(no1,no2):
    add_res = no1 + no2
    sub_res = no1 - no2
    return add_res, sub_res

def main():
    no1= int(input("Enter no1: "))
    no2= int(input("Enter no2: "))
    addition_result, substraction_result = artihmatic(no1,no2)
    print("Addition result : ", addition_result)
    print("Substraction result : ", substraction_result)

if __name__ == '__main__':
    main()