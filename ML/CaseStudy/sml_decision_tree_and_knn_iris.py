#Supervised Machine Learning Decision using Decision Tree & K Nearest Neighbor Iris Dataset
#Consider below characteristics of Machin Learning Application.
#Classifier : Decision Tree K Nearest Neighbor
#Dataset : Iris Dataset
# Features : Sepal Width, Sepal Length, Petal Width, Petal Length
#Labels : Versicolor, Setosa, Virginica
#Training Dataset : 75
#Testing Dataset : 75
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def calculate_accuracy_decision_tree():
    iris  = load_iris()
    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(data_train, target_train)
    predictions = classifier.predict(data_test)
    accuracy = accuracy_score(target_test, predictions)
    return accuracy


def calculate_accuracy_k_neighbour():
    iris = load_iris()
    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)
    classifier = KNeighborsClassifier()
    classifier.fit(data_train, target_train)
    predictions = classifier.predict(data_test)
    accuracy = accuracy_score(target_test, predictions)
    return accuracy




def main():
    print("ML Application")
    accuracy = calculate_accuracy_decision_tree()
    print("Accuracy of classification algorithm with Decision Tree classifier is : ", accuracy*100)

    accuracy = calculate_accuracy_k_neighbour()
    print("Accuracy of classification algorithm with KNN classifier is : ", accuracy*100)


if __name__ == "__main__":
    main()