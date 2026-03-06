'''
3. Consider below task
    1. Train linear regression model.
    2. Predict salary for 6 years of experience.
    3. Plot regression line using matplotlib.

Dataset
    Experience     Salary
    1              20000
    2              25000
    3              30000
    4              35000
    5              40000
'''

import math
import matplotlib.pyplot as plt

def main():
    # Dataset
    X = [1, 2, 3, 4, 5]
    Y = [20000, 25000, 30000, 35000, 40000]

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
    print(f"Predicted salary for 6 years of experience = {X_new} : {Y_pred}")

    # Plot regression line
    plt.scatter(X, Y, color='blue', label='Data points')
    plt.plot(X, [(m * x) + c for x in X], color='red', label='Regression line')
    plt.plot(X_new, Y_pred, marker='o', color='green', label='Predicted point (6, Y_pred)')
    plt.xlabel('Experience')
    plt.ylabel('Salary')
    plt.title('Linear Regression')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()