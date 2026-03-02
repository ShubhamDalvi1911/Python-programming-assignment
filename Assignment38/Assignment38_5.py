"""
Based on the dataset values, analyze whether:
    - Higher StudyHours increase the chance of passing.
    - Higher Attendance improves FinalResult.
      Write your observations in 4-5 lines.
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

    # Data Visualization
    print(Border)
    print("Statistical Report of Dataset : ")
    print(df.describe())                            # Gives the report of all data
    print(Border)

    # Graphical Visualization 
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.scatter(df["StudyHours"], df["FinalResult"])
    plt.xlabel("StudyHours")
    plt.ylabel("FinalResult")
    plt.title("StudyHours vs FinalResult")
    plt.show()

    plt.scatter(df["Attendance"], df["FinalResult"])
    plt.xlabel("Attendance")
    plt.ylabel("FinalResult")
    plt.title("Attendance vs FinalResult")
    plt.show()

    # Observations :
    print(Border)
    print("Observations : ")
    print("1. Higher StudyHours increase the chance of passing.\n Those students who have more than 4 hours of study have more chances to pass the exam.")
    print("2. Higher Attendance improves FinalResult. \n Those students who have more than 75%% attendance have more chances to pass the exam.")
    print(Border)


if __name__ == "__main__":
    main()