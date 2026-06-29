# Wine Prediction (Supervised Learning)
# Consider below characteristics of Machine Learning Application:
# Classifier: KNN
# DataSet: Wine Predictor
# Features: Alcohol, Malic acid, Ash, Alkalinity of ash, Magnesium, Total phenols, Flavonoids,
# Nonflavonoids phenols, Proanthocyanins, Color intensity, Hue, OD280/OD315 of diluted wines, Proline
# Labels: Class
# Training Dataset: 142 Entries
# Testing Dataset: 35 Entry

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from ML.CaseStudy.user_defined_knn import knn


def main():
    print("Wine Predictor Case Study Application")
    # Step 1 : Load the dataset
    df = pd.read_csv("WinePredictor.csv")
    # Check the data.
    print(df.head())
    # Drop any potential null values
    df.dropna()
    # Data info
    df.info()
    # for c in df:
    #     df[c].hist()
    #     plt.title(c)
    #     plt.show()
    data = df.drop('Class', axis=1)
    target = df['Class']

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.2, random_state = 42)
    # Fitting data in KNN classifier
    classifier = KNeighborsClassifier(3)
    classifier.fit(data_train, target_train)
    prediction = classifier.predict(data_test)
    print(f"Data Test: {data_test}")
    print("Prediction:", prediction )
    # Checking the accuracy of KNN classifier
    accuracy = accuracy_score(target_test, prediction)
    print(f"Accuracy: {accuracy * 100:.2f}%")




if __name__ == "__main__":
    main()