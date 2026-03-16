class Dog:
    def speak(self):
        return  "Woof!"

class Cat:
    def speak(self):
        return "Meow!"


def main():
    print("Demonstration of Polymorphism")
    print("Functional polymorphism")
    print(len("Hello World!"))
    print(len([1,2,3]))
    print(len({"abc":1, "xyz":2}))

    print("Operator Polymorphism")
    print( 10 + 2)
    print("Python" + "Rocks")

    print("Class Polymorphism")
    for animal in [Dog(),Cat()]:
        print(animal.speak())


if __name__ == "__main__":
    main()


