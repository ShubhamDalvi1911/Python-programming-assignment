'''
1. Write a python program that calculates the variance and standard deviation of a dataset using NumPy for the following values:
[6,7,8,9,10,11,12]
'''
import numpy as np

def main():
    data = np.array([6,7,8,9,10,11,12])

    variance = np.var(data)
    print("Variance of the dataset is : ", variance)

    standard_deviation = np.std(data)
    print("Standard deviation of the dataset is : ", standard_deviation)


if __name__ == "__main__":
    main()