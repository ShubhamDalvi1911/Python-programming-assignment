"""
write a python program to load the file student_performance_ml.csv using pandas.
Display:
    First 5 records
    Last 5 records
    Total number of rows and columns
    List of column names
    Data types of each column
"""

import pandas as pd

def main():
    Border = "-"*100
    print(Border)
    print("student performance ml")
    print(Border)

    Data = "student_performance_ml.csv"

    # Load the data using pandas
    df = pd.read_csv(Data)

    # First 5 records
    print(Border)
    print("First 5 records for the dataset is : ")
    print(df.head())
    print(Border)

    # Last 5 records
    print(Border)
    print("Last 5 records for the dataset is : ")
    print(df.tail())
    print(Border)

    # Total number of rows and columns
    print(Border)
    print("Total number of rows and columns : ")
    print(df.shape)
    print(Border)

    # List of column names
    print(Border)
    print("List of column names : ")
    print(list(df.columns))
    print(Border)

    # Data types of each column
    print(Border)
    print("Data types of each column : ")
    print(df.dtypes)
    print(Border)

if __name__ == "__main__":
    main()