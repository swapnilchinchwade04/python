from filecmp import demo


class Robot:
    #class variable
    populations = None
    population = 0

    def __init__(self,name):
        #instance variable
        self.name = name
        print("Initializing {}".format(self.name))
        #when new object is created the population is increased by 1
        Robot.population += 1

    #instance method
    def die(self):
        """I am dying."""
        print("{} is being destroyed".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working ".format(Robot.population))

    def say_hi(self ):
        """Greetings by the robot."""
        print("Greetings my masters call me {}".format(self.name))

    #class method
    @classmethod
    def how_many(cls):
        """Print the current populations"""
        print("We have {:d} robots".format(Robot.population))

def main():
    print("Demonstration of Class & object variables with 3 types of methods")

    obj1 = Robot("R2-D2")
    obj1.say_hi()
    Robot.how_many()

    obj2 = Robot("O-PC2")
    obj2.say_hi()
    Robot.how_many()

    print("Robots can do some work here.")
    print("Robots have finished their work lts finish them.")

    obj1.die()
    obj2.die()

    Robot.how_many()


if __name__ == "__main__":
    main()

