"""
Create a scatter plot of:
studyhours vs previousscore
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

    # Graphical Visualization 
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.scatter(df["StudyHours"], df["PreviousScore"])
    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    plt.title("StudyHours vs PreviousScore")
    plt.show()

if __name__ == "__main__":
    main()