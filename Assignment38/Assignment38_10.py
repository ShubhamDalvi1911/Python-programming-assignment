"""
Plot SleepHours against FinalResult.
Dose sleeping more guarantee success? Explain
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
    plt.scatter(df["SleepHours"], df["FinalResult"])
    plt.xlabel("SleepHours")
    plt.ylabel("FinalResult")
    plt.title("SleepHours vs FinalResult")
    plt.show()

    # Explanation of observations
    print(Border)
    print("Explanation of observations : ")
    print("The scatter plot of SleepHours vs FinalResult shows the relationship between the number of hours students sleep and their final results. \n")
    print("Those student who sleep more than 6 hours tend to have better final results, indicating that getting enough sleep may contribute to better academic performance. ")
    
if __name__ == "__main__":
    main()