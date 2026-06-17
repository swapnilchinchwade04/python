#Supervised Machine Learning Decision using Decision Tree & K Nearest Neighbor Iris Dataset
#Consider below characteristics of Machin Learning Application.
#Classifier : Decision Tree, K Nearest Neighbor
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


def calculate_accuracy_decision_tree(data_train, data_test, target_train, target_test):
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(data_train, target_train)
    prediction = classifier.predict(data_test)
    accuracy = accuracy_score(target_test, prediction)
    return accuracy

def calculate_accuracy_knn(data_train, data_test, target_train, target_test):
    classifier = KNeighborsClassifier()
    classifier.fit(data_train, target_train)
    prediction  = classifier.predict(data_test)
    accuracy  = accuracy_score(target_test, prediction)
    return accuracy

def main():
    print("ML Application")
    iris = load_iris()
    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)

    accuracy_dtc = calculate_accuracy_decision_tree(data_train, data_test, target_train, target_test)

    accuracy_knn = calculate_accuracy_knn(data_train, data_test, target_train, target_test)

    print("Accuracy of Decision Tree is : ", accuracy_dtc*100)
    print("Accuracy of KNN is : ", accuracy_knn*100)


if __name__ == "__main__":
    main()