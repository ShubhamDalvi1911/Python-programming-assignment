"""
Draw a boxplot for attendance.
Identify if any outliers are present.
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
    plt.boxplot(df["Attendance"])
    plt.xlabel("Attendance")
    plt.title("Boxplot of Attendance")
    plt.show()

if __name__ == "__main__":
    main()