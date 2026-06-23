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

def func_knn(data_train, data_test, target_train, target_test, weather_ip, temperature_ip):
    classifier = KNeighborsClassifier(3)
    classifier.fit(data_train, target_train)
    #print("weather_ip: ", weather_ip)
    #print("temperature_ip: ", temperature_ip)
    user_features = pd.DataFrame([[weather_ip, temperature_ip]], columns=['Weather', 'Temperature',])
    # print("target_test")
    # print(target_test)
    prediction = classifier.predict(user_features)
    print(f"Predicted model output: {prediction}")

    if prediction == "Yes":
        print("You can play.")
    elif prediction == "No":
        print("You can not play.")


def check_accuracy_knn(data, target):
    """
    Splits the data into two equal parts for training and testing.
    """
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.5)

    # Defining the values of K to test. (Odd numbers to prevent ties.)
    k_values = [1,3,5,7,9]

    print(f"{'K Value':<10} | {'Accuracy(%)':<12}")
    print("-" * 27)
    # Check accuracy for each K
    for k in k_values:
        #Classifier
        knn = KNeighborsClassifier(n_neighbors=k)
        #Trin the algorithm
        knn.fit(data_train, target_train)
        prediction = knn.predict(data_test)
        accuracy = accuracy_score(target_test, prediction)
        print(f"{k:<10} | {accuracy*100:.2f}%")


def main():
    print("Play Predictor ML Application")

    # load csv file
    #df  = pd.read_csv("Play_Predictor.csv", index_col=0)
    df = pd.read_csv("Play_Predictor.csv", index_col= False)
    #print(df.head())
    # Initialize label encoder
    label_encoder_weather = LabelEncoder()
    label_encoder_temp = LabelEncoder()
    # fit and transform the specific columns as per requirement
    df['Weather' ] =label_encoder_weather.fit_transform(df['Weather'])
    df['Temperature'] = label_encoder_temp.fit_transform(df['Temperature'])
    # save encoded data to the new file.
    df.to_csv('encoded_play_predictor.csv', index=False)

    ef = pd.read_csv("encoded_play_predictor.csv")
    #print(ef.head())

    data = ef.drop(columns= ['Play'])
    target = ef['Play']
    #print(f"Known classes in encoder: {label_encoder_weather.classes_}\n")
    #print(f"Known classes in temp encoder: {label_encoder_temp.classes_}\n")
    weather_ip = input("Please enter Weather condition:").strip()
    #print("Weather :", weather_ip)
    temperature_ip = input("Please enter Temperature:").strip()
    #print("Temperature :", temperature_ip)

    try:
        encoded_weather_ip = label_encoder_weather.transform([weather_ip])[0]
        encoded_temperature_ip = label_encoder_temp.transform([temperature_ip])[0]

    except ValueError:
        print(f"\nError: Input is an unrecognized category!")


    data_train, data_test, target_train, target_test = train_test_split(data, target)


    func_knn(data_train, data_test, target_train, target_test, encoded_weather_ip, encoded_temperature_ip)

    check_accuracy_knn(data, target)


if __name__ == "__main__":
    main()
