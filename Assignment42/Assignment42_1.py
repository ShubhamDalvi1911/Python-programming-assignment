'''
1. Implement Simple Linear Regression manually without using any ML library.

Dataset:
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

Tasks:
    Calculate:
    1. Mean of X(X_bar)
    2. Mean of Y(Y_bar)
    3. Slope(m)
    4. Intercept(c)

Expected Output Example:
    Mean of X = 3
    Mean of Y = 3.6

    Slope(m) = 0.4
    Intercept(c) = 2.4

    Regression Equation:
    Y = 0.4X + 2.4

    Predicted Y for X = 6 : 4.8
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

    # Predicted Y for X = 6
    X_new = 6
    Y_pred = (m * X_new) + c
    print(f"Predicted Y for X = {X_new} : {Y_pred}")


if __name__ == "__main__":
    main()