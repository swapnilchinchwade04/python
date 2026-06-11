# Below application uses Decision Tree algorithm to classify the type of ball.
# In this application training set contains two types of balls.
# Features of our training set is weight and type of surface of ball.
# We are using two labels as Tennis and Cricket.
# We train our data set using Decision tree algorithms
# Consider below characteristics of Machine Learning Application:
# Classifier: Decision Tree
# DataSet: Balls Dataset
# Features: Weight & Surface type
# Labels: Tennis and Cricket
# Training Dataset: 15 Entries
# Testing Dataset: 1 Entry

from  sklearn import tree

def ball_classification(weight, surface):
    ball_features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    names = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    obj = tree.DecisionTreeClassifier()
    obj = obj.fit(ball_features, names)
    result = obj.predict([[weight, surface]])
    if result == 1:
        print("Your object looks like Tennis ball.")
    elif result == 2:
        print("Your object looks like Cricket ball.")


def main():
    print("Enter weight of object:")
    weight = input()
    print("What is the surface type of your object Rough or Smooth?")
    surface = input()
    if surface.lower() == "rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 2
    else:
        print("Wrong input.")
        exit()

    ball_classification(weight, surface)

if __name__ == "__main__":
    main()