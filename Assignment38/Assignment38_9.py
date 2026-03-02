"""
Create a plot showing relationship between assignments Completed and FinalResult.
Explain your observations
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
    plt.scatter(df["AssignmentsCompleted"], df["FinalResult"])
    plt.xlabel("AssignmentsCompleted")
    plt.ylabel("FinalResult")
    plt.title("AssignmentsCompleted vs FinalResult")
    plt.show()

    # Explanation of observations
    print(Border)
    print("Explanation of observations : ")
    print("The scatter plot of AssignmentsCompleted vs FinalResult shows the relationship between the number of assignments completed by students and their final results. \n")
    print("The student those have completed more assignments tend to have better final results, indicating a positive correlation between the two variables. \n")

if __name__ == "__main__":
    main()