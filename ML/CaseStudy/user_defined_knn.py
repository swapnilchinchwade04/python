#Supervised Machine Learning User Defined K Nearest Neighbor Algorithm
#Consider below characteristics of Machin Learning Application.
#Classifier : User Defined K Nearest Neighbor
#Dataset : Iris Dataset
# Features : Sepal Width, Sepal Length, Petal Width, Petal Length
#Labels : Versicolor, Setosa, Virginica
#Training Dataset : 75
#Testing Dataset : 75
from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
    return distance.euclidean(a,b)

class knn():

    def fit(self, training_data, training_target):
        self.training_data = training_data
        self.training_target = training_target

    def predict(self, test_data):
        predictions=[]
        #print(test_data)
        #exit()
        for row in test_data:
            #print(row)
            #exit()
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self,row):
        #print("Row:", row, "Target: ",self.training_data[0])
        #exit()
        best_distance =euc(row, self.training_data[0])
        #exit()
        best_index = 0
        for i in range(1, len(self.training_data)):
            dist = euc(row, self.training_data[i])
            if dist < best_distance:
                best_distance = dist
                best_index = i
        return self.training_target[best_index]


def knneighbor():
    border = "-"*50
    iris = load_iris()
    data = iris.data
    target = iris.target
    print(border)
    print("Actual data set is")
    print(border)

    for i in range(len(iris.target)):
        print("ID: %d, Label %s, Feature : %s" % (i, iris.data[i], iris.target[i]))
    print("Size of actual data set %d"%(i+1))

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size= 0.5)

    print(border)
    print("Training data set is")
    print(border)
    for i in range(len(data_train)):
        print("ID: %d, Label %s, Feature : %s" % (i, data_train[i], target_train[i]))
    print("Size of training data set %d"%(i+1))

    print(border)
    print("Test data set is")
    print(border)
    for i in range(len(data_test)):
        print("ID: %d, Label %s, Feature : %s" % (i, data_test[i], target_test[i]))
    print("Size of test data set %d"%(i+1))

    classifier = knn()
    classifier.fit(data_train, target_train)
    predictions = classifier.predict(data_test)
    #print("Target test",target_test,"Predictions", predictions)
    accuracy = accuracy_score(target_test, predictions)
    return accuracy


def main():
    accuracy = knneighbor()
    print("Accuracy of classification algorithm with K Neighbor is ", accuracy * 100,"%")


if __name__ == "__main__":
    main()
