'''
2. Using the same dataset from above qustion, calculate model performance.

Dataset:
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

Tasks:
    1. Predict all Y values using regression equation.
    2. Calculate:
        a. Mean Squared Error (MSE)
        b. R**2 Score
    Show all intermediate calculations.

'''

import math

def main():
    # Dataset
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    # Mean of X(X_bar)
    X_bar = sum(X) / len(X)
    print(f"Mean of X = {X_bar}")

    # Mean of Y(Y_bar)
    Y_bar = sum(Y) / len(Y)
    print(f"Mean of Y = {Y_bar}")

    # Slope(m)
    # m = (Summation (X - X_Bar) * (Y - Y_Bar)) / (Summation (X - X_Bar) ** 2)

    numerator = 0
    denominator = 0

    for i in range(len(X)):
        numerator = numerator + ((X[i] - X_bar) * (Y[i] - Y_bar))
        denominator = denominator + ((X[i]- X_bar) **2)

    m = numerator / denominator
    print("Slope (m) : ", m)

    # Intercept(c)
    c = Y_bar - (m * X_bar)
    print("Intercept (c) : ", c)

    # Regression Equation
    print(f"Regression Equation: Y = {m}X + {c}")

    # Predicte all Y values using regression equation
    y_pred = []
    for i in range(len(X)):
        pred = (m * X[i]) + c
        y_pred.append(pred)
        print(f"Predicted Y for X = {X[i]} : {pred}")

    # Mean Squared Error (MSE)
    for i in range(len(Y)):
        MSE = sum([(Y[i] - y_pred[i])**2]) / len(Y)
        print(f"Mean Squared Error (MSE) : {MSE}")

    # R**2 Score
    numerator = 0
    denominator = 0

    for i in range(len(Y)):
        numerator = numerator + ((Y[i] - y_pred[i]) ** 2)
        denominator = denominator + ((Y[i] - Y_bar) ** 2)

    R2_score = 1 - (numerator / denominator)
    print(f"R**2 Score : {R2_score}")


if __name__ == "__main__":
    main()