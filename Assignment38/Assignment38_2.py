"""
write a python program to 
    Display total number of students in the dataset
    Count how many student passed (FinalResult = 1)
    Count how many student failed (FinalResult = 0)
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

    # Total number of students in the dataset
    print(Border)
    print("Display total number of students in the dataset : ")
    print(df.shape[0])
    print(Border)

    # Count how many student passed (FinalResult = 1)
    print(Border)
    print("Count how many student passed (FinalResult = 1) : ")
    print((df['FinalResult'] == 1).sum())
    print(Border)

    # Count how many student failed (FinalResult = 0)
    print(Border)
    print("Count how many student failed (FinalResult = 0) : ")
    print((df['FinalResult'] == 0).sum())
    print(Border)


if __name__ == "__main__":
    main()