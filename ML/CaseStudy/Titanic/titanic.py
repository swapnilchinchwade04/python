import numpy as np
import pandas as pd
from seaborn import countplot
from matplotlib.pyplot import figure, show
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def titanic_logistic():
    # Step 1: Load Data
    titanic_data = pd.read_csv("titanic.csv")
    print("First 5 entries from loaded dataset")
    print(titanic_data.head())
    print("Number of passengers are " + str(len(titanic_data)))

    # Step 2: Analyze Data
    print("Visualisation : Survived and non survived passengers")
    figure()
    countplot(data=titanic_data, x="Survived").set_title("Survived and non survived passengers")
    show()

    print("Visualisation : Survived and non survived passengers based on Gender")
    figure()
    countplot(data=titanic_data, x="Survived", hue="Sex").set_title(
        "Survived and non survived passengers based on Gender")
    show()

    print("Visualisation : Survived and non survived passengers based on Passenger class")
    figure()
    countplot(data=titanic_data, x="Survived", hue="Pclass").set_title(
        "Survived and non survived passengers based on the Passenger class")
    show()

    print("Visualisation : Age distribution")
    figure()
    titanic_data["Age"].plot.hist().set_title("Age distribution")
    show()

    print("Visualisation : Fare distribution")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Fare distribution")
    show()

    # Step 3 : Data Cleaning
    titanic_data.drop("PassengerId", axis=1, inplace=True)

    # ---Change Age before dropping any rows, with a numeric value ---
    titanic_data["Age"] = titanic_data["Age"].replace(r"^\s*$", np.nan, regex=True)
    titanic_data["Age"] = pd.to_numeric(titanic_data["Age"], errors="coerce")
    median_age = titanic_data["Age"].median()          # median is more robust than mean to Titanic's age outliers
    titanic_data["Age"] = titanic_data["Age"].fillna(median_age)

    # Change Fare and Embarked lightly too, instead of dropping those rows
    titanic_data["Fare"] = titanic_data["Fare"].fillna(titanic_data["Fare"].median())
    titanic_data["Embarked"] = titanic_data["Embarked"].fillna(titanic_data["Embarked"].mode()[0])

    # Feature creation of family size instead of removing SibSp/Parch columns
    titanic_data["FamilySize"] = titanic_data["SibSp"] + titanic_data["Parch"] + 1
    titanic_data["IsAlone"] = (titanic_data["FamilySize"] == 1).astype(int)

    # One-hot encode categorical columns
    Sex = pd.get_dummies(titanic_data["Sex"], drop_first=True)
    Pclass = pd.get_dummies(titanic_data["Pclass"], drop_first=True, prefix="Pclass")
    Embarked = pd.get_dummies(titanic_data["Embarked"], drop_first=True, prefix="Embarked")

    titanic_data = pd.concat([titanic_data, Sex, Pclass, Embarked], axis=1)

    # Drop the original Pclass/Sex/Embarked columns
    titanic_data.drop(
        ["Sex", "SibSp", "Parch", "Embarked", "Cabin", "Name", "Ticket", "Pclass"],
        axis=1, inplace=True
    )

    # Now drop any remaining stray NaNs
    titanic_data.dropna(inplace=True)

    df = pd.DataFrame(titanic_data)
    df.to_csv("filtered_titanic.csv", index=False)

    print("Column Names:", titanic_data.columns.tolist())

    x = titanic_data.drop("Survived", axis=1)
    y = titanic_data["Survived"]

    # Step 4 : Train test split
    xtrain, xtest, ytrain, ytest = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale only the continuous columns; fit on train, apply to both (no leakage)
    scaler = StandardScaler()
    continuous_cols = ["Age", "Fare", "FamilySize"]
    xtrain[continuous_cols] = scaler.fit_transform(xtrain[continuous_cols])
    xtest[continuous_cols] = scaler.transform(xtest[continuous_cols])

    logmodel = LogisticRegression(max_iter=1000)
    logmodel.fit(xtrain, ytrain)

    # Step 5 : Predict
    prediction = logmodel.predict(xtest)

    # Step 6 : Evaluate
    print("Classification Report of Logistic Regression is: ")
    print(classification_report(ytest, prediction))

    print("Confusion Matrix of Logistic Regression is:")
    print(confusion_matrix(ytest, prediction))

    print("Accuracy of Logistic Regression is:")
    print(accuracy_score(ytest, prediction))


def main():
    print("Supervised Machine Learning")
    print("Logistic Regression on Titanic Dataset")
    titanic_logistic()


if __name__ == "__main__":
    main()