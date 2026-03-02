"""
Using pandas functions, calcilate and display:
    Average StudyHours
    Average Attendance
    Maximum PreviousScore
    Minimum SleepHours
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
    print("Average StudyHours : ")
    print((df['StudyHours']).mean())
    print(Border)

    # Average Attendance
    print(Border)
    print("Average Attendance : ")
    print((df['Attendance']).mean())
    print(Border)

    # Maximum PreviousScore
    print(Border)
    print("Maximum PreviousScore : ")
    print((df['PreviousScore']).max())
    print(Border)

    # Minimum SleepHours
    print(Border)
    print("Minimum SleepHours : ")
    print((df['SleepHours']).min())
    print(Border)



if __name__ == "__main__":
    main()