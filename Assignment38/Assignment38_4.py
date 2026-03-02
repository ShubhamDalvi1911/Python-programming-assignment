"""
Use value_counts() to analyze the distribution of FinalResult.
Calculate the percentage of Pass and Fail students.
Is the dataset balanced? Justify your answer.
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

    # Average StudyHours
    print(Border)
    print("Distribution of FinalResult : ")
    print(df["FinalResult"].value_counts())
    print(Border)

    # Calculate the percentage of Pass and Fail students.
    P_P = (((df['FinalResult'] == 1).sum()) / df.shape[0]) * 100
    F_P = (((df['FinalResult'] == 0).sum()) / df.shape[0]) * 100
    print(Border)
    print("percentage of Pass Student : ")
    print(P_P)
    print(Border)
    print(Border)
    print("percentage of Fail Student : ")
    print(F_P)
    print(Border)


if __name__ == "__main__":
    main()