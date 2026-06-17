import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()


print("Feature name of iris dataset")
print(iris.feature_names)

print("Target names of iris dataset::")
print(iris.target_names)

#indices to be removed
test_index=[1,51,101]

#training data with removed elements
train_target = np.delete(iris.target, test_index,axis = 0)
train_data = np.delete(iris.data, test_index, axis = 0)

#testing data for testing on training data
test_target = iris.target[test_index]
test_data = iris.data[test_index]

# form decision tree classifier
classifier = tree.DecisionTreeClassifier()

# apply training data to form tree
classifier.fit(train_data, train_target)

print("Values that we removed from testing dataset:")
print(test_target)

print("Result of classifying iris dataset:")
print(classifier.predict(test_data))


