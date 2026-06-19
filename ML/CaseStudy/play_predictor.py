#Supervised Machine Learning Decision using Decision Tree & K Nearest Neighbor Play Predictor Case Dataset
#Consider below characteristics of Machin Learning Application.
#Classifier : Decision Tree, K Nearest Neighbor
#Dataset : Play Predictor
# Features : Weather, Temperature
#Labels : Yes, No
#Training Dataset : 30
#Testing Dataset : 10

from sklearn import tree
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def calculate_accuracy_dtc(data_train, data_test, target_train, target_test):
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(data_train, target_train)
    prediction = classifier.predict(data_test)
    accuracy = accuracy_score(target_test, prediction)
    return accuracy

def calculate_accuracy_knn(data_train, data_test, target_train, target_test):
    classifier = KNeighborsClassifier(3)
    classifier.fit(data_train, target_train)
    prediction = classifier.predict(data_test)
    accuracy = accuracy_score(target_test, prediction)
    return accuracy

def main():
    print("Play Predictor ML Application")
    # load csv file
    df  = pd.read_csv("Play_Predictor.csv", index_col=0)
    # view first 5 rows
    #print(df.head())
    # Initialize label encoder
    label_encoder = LabelEncoder()
    # drop the column and overwrite the data frame
    #df.drop(columns=['Unnamed:0'], inplace=True)
    # fit and transform the specific columns as per requirement
    df['Weather' ] =label_encoder.fit_transform(df['Weather'])
    df['Temperature'] = label_encoder.fit_transform(df['Temperature'])
    # save encoded data to the new file.
    df.to_csv('encoded_play_predictor.csv', index=False)

    ef = pd.read_csv("encoded_play_predictor.csv")
    #print(ef.head())

    data = ef.drop(columns= ['Play'])
    target = ef['Play']
    # print(target)
    # print(target)

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.1)
    accuracy_knn = calculate_accuracy_knn(data_train, data_test, target_train, target_test)

    print("Accuracy of KNN is : ", accuracy_knn*100, '%')






if __name__ == "__main__":
    main()
