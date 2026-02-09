
def Addition(num1,num2):
    ans = num1 + num2
    return ans
    
def main():
    print("Addition program:")
    print("Enter 1st number")
    x = int(input())
    print("Enter 2nd number")
    y = int(input())
    res = Addition(x, y)
    print( "Addition result:", res)

if __name__ == "__main__":
	main()
	


