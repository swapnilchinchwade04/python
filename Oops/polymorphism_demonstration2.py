# Polymorphism demonstration with method overriding
class Base:
    def fun(self):
        print("Base")

class Derived(Base):
    def fun(self):
        print("Derived")

def main():
    obj = Derived()
    obj.fun()

if __name__ == "__main__":
    main()


