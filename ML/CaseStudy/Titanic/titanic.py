import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def titanic_logistic():
    # Step 1: Load Data
    titanic_data = pd.read_csv("titanic.csv")
    print("First 5 entries from loaded dataset")
    print(titanic_data.head())
    print("Number of passengers are "+str(len(titanic_data)))

    # Step 2: Analyze Data
    print("Visualisation : Survived and non survived passengers")
    figure()
    target = "Survived"
    countplot(data = titanic_data, x=target).set_title("Survived and non survived passengers")
    show()

    print("Visualisation : Survived and non survived passengers based on Gender")
    figure()
    target = "Survived"
    countplot(data = titanic_data, x=target, hue = "Sex").set_title("Survived and non survived passengers based on Gender")
    show()

    print("Visualisation : Supervised and non supervised passengers based on the passengers class.")
    figure()
    target = "Survived"

    countplot(data = titanic_data, x=target, hue = "Pclass").set_title("Survived and non survived passengers based on the Passengers class")
    show()

    print("Visualisation : Survived and non survived passengers based on Age")
    figure()
    titanic_data["Age"].plot.hist().set_title("Survived and non survived passengers based on age.")
    show()

    print("Visualisation: Survived and non survived passengers based on the Fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Survived and non survived passengers based on Fare")
    show()

    # Step 3 : Data Cleaning
    titanic_data.drop("PassengerId", axis = 1, inplace=True)
    print("First 5 entries from loaded dataset after removing zero column")
    print(titanic_data.head(5))

    print("Values of Sex column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("Values of Sex column after removing one field")
    Sex = pd.get_dummies(titanic_data["Sex"], drop_first=True)
    print(Sex.head(5))

    print("Values of Pclass column after removing one field.")
    Pclass= pd.get_dummies(titanic_data["Pclass"], drop_first= True, prefix = "Pclass")
    print(Pclass.head(5))

    print("Values of data set after concatenating new columns")
    titanic_data = pd.concat([titanic_data, Sex, Pclass], axis=1)
    print(titanic_data.head(5))

    print("Values of data set after removing irrelevant columns")
    titanic_data.drop(["Sex","SibSp","Parch","Embarked","Cabin","Name","Ticket"], axis = 1, inplace = True)
    print(titanic_data.head(5))

    # Replace empty strings or spaces with NaN
    titanic_data["Age"] = titanic_data["Age"].replace(r"^\s*$", np.nan, regex=True)
    titanic_data.dropna(inplace = True)

    # Ensure the column is numeric
    titanic_data["Age"] = pd.to_numeric(titanic_data["Age"])

    # Calculate average and fill NaN values
    avg_value = str(int(titanic_data["Age"].mean()))
    titanic_data["Age"] = titanic_data["Age"].fillna(avg_value)


    df = pd.DataFrame(titanic_data)
    df.to_csv("filtered_titanic.csv")


    print("Column Names:",titanic_data.columns)

    x= titanic_data.drop("Survived", axis=1)
    y = titanic_data["Survived"]

    # Step 4 : Data Training
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

    logmodel = LogisticRegression()
    logmodel.fit(xtrain, ytrain)

    # Step 5 : Data Testing
    prediction = logmodel.predict(xtest)

    #step 6 : Calculate Accuracy
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