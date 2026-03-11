def fun():
    print("Inside fun")

def gun(function_name):
    print("Inside gun")
    function_name()

def main():
    gun(fun)

if __name__ == "__main__":
    main()