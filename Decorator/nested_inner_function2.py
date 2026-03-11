def outer():
    print("Inside outer function")
    def inner():
        print("Inside inner function")
    return inner

def main():
    func_name = outer() # its call to the outer function. O/P: Inside outer function
    func_name()  # its same as calling inner function
    # its call to the inner function . O/P: Inside inner function

if __name__ == "__main__":
    main()