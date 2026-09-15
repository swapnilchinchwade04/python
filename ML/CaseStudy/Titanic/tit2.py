import re
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ----------------------------------------------------------------------
# STEP 1: Load the data
# ----------------------------------------------------------------------
titanic_data = pd.read_csv("titanic.csv")
print("First 5 rows of the dataset:")
print(titanic_data.head())
print("Total passengers:", len(titanic_data))


# ----------------------------------------------------------------------
# STEP 2: Clean up missing values
# We fill in (impute) missing values instead of deleting those rows,
# so we don't throw away good data just because one column is missing.
# ----------------------------------------------------------------------

# Age has some missing values -> fill them with the median age
titanic_data["Age"] = titanic_data["Age"].fillna(titanic_data["Age"].median())

# Fare has a couple of missing values -> fill with the median fare
titanic_data["Fare"] = titanic_data["Fare"].fillna(titanic_data["Fare"].median())

# Embarked (port they boarded from) -> fill with the most common port
titanic_data["Embarked"] = titanic_data["Embarked"].fillna(titanic_data["Embarked"].mode()[0])


# ----------------------------------------------------------------------
# STEP 3: Create a few simple new features
# These are easy to understand and give the model useful extra signal.
# ----------------------------------------------------------------------

# Family size = siblings/spouses + parents/children + the passenger themself
titanic_data["FamilySize"] = titanic_data["SibSp"] + titanic_data["Parch"] + 1

# Was this passenger traveling completely alone?
titanic_data["IsAlone"] = (titanic_data["FamilySize"] == 1).astype(int)


def get_title(name):
    """Grab the title (Mr, Mrs, Miss, Master...) out of the passenger's name.
    Example: 'Braund, Mr. Owen Harris' -> 'Mr'
    The title turns out to be a strong clue about age, sex, and status."""
    title = re.search(r",\s*([^.]*)\.", name).group(1).strip()
    if title not in ["Mr", "Mrs", "Miss", "Master"]:
        title = "Other"   # group all rare titles together to keep things simple
    return title


titanic_data["Title"] = titanic_data["Name"].apply(get_title)


# ----------------------------------------------------------------------
# STEP 4: Turn text columns into numbers
# Machine learning models only understand numbers, so we convert
# categories (like "male"/"female") into 0/1 columns.
# ----------------------------------------------------------------------
titanic_data = pd.get_dummies(
    titanic_data,
    columns=["Sex", "Embarked", "Title", "Pclass"],
    drop_first=True   # avoids redundant columns
)


# ----------------------------------------------------------------------
# STEP 5: Drop columns we don't need for modeling
# (IDs, free text, and columns already captured by our new features)
# ----------------------------------------------------------------------
titanic_data.drop(
    ["PassengerId", "Name", "Ticket", "Cabin", "SibSp", "Parch"],
    axis=1, inplace=True
)

print("\nColumns going into the model:")
print(titanic_data.columns.tolist())


# ----------------------------------------------------------------------
# STEP 6: Split into features (x) and target (y)
# ----------------------------------------------------------------------
x = titanic_data.drop("Survived", axis=1)
y = titanic_data["Survived"]


# ----------------------------------------------------------------------
# STEP 7: Split into training data and testing data
# random_state=42 -> same split every time you run this (repeatable results)
# stratify=y -> keeps the survived/not-survived ratio balanced in both sets
# ----------------------------------------------------------------------
xtrain, xtest, ytrain, ytest = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)


# ----------------------------------------------------------------------
# STEP 8: Scale the numeric columns
# Age and Fare are on very different number ranges (e.g. 0-80 vs 0-500).
# Scaling puts them on a similar footing so the model trains better.
# We fit the scaler on the TRAINING data only, then apply it to both,
# so the test set stays completely "unseen" by the model.
# ----------------------------------------------------------------------
scaler = StandardScaler()
numeric_cols = ["Age", "Fare", "FamilySize"]

xtrain[numeric_cols] = scaler.fit_transform(xtrain[numeric_cols])
xtest[numeric_cols] = scaler.transform(xtest[numeric_cols])


# ----------------------------------------------------------------------
# STEP 9: Train the model
# ----------------------------------------------------------------------
model = LogisticRegression(max_iter=1000)
model.fit(xtrain, ytrain)


# ----------------------------------------------------------------------
# STEP 10: Make predictions on the test data
# ----------------------------------------------------------------------
predictions = model.predict(xtest)


# ----------------------------------------------------------------------
# STEP 11: Check how well the model did
# ----------------------------------------------------------------------
print("\nClassification Report:")
print(classification_report(ytest, predictions))

print("Confusion Matrix:")
print(confusion_matrix(ytest, predictions))

print("Accuracy:", accuracy_score(ytest, predictions))