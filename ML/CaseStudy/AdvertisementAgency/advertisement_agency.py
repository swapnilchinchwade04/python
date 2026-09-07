import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def advertisementagency():
    print("advertisement agency")
    data = pd.read_csv("Advertising.csv")
    print("Size of data set:", data.shape)

    X= data[['TV', 'radio', 'newspaper']]
    y=data['sales']
    print(X)

    reg = LinearRegression()
    print(f"X shape: {getattr(X, 'shape', len(X))}, y shape: {getattr(y, 'shape', len(y))}")

    reg = reg.fit(X, y)
    y_pred = reg.predict(X)
    r2 = reg.score(X, y)
    print("R² Score:", r2)

def main():
    advertisementagency()

if __name__ == "__main__":
    main()

