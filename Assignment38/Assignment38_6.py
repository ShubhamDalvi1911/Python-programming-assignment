"""
Plot a histogram of StudyHours.
Explain what the distribution tells you.
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
    plt.hist(df["StudyHours"], bins=10, edgecolor='black')
    plt.xlabel("StudyHours")
    plt.ylabel("Frequency")
    plt.title("Distribution of StudyHours")
    plt.show()

    # Explanation of distribution
    print(Border)
    print("Explanation of distribution : ")
    print("The histogram of StudyHours shows the distribution of study hours among students. \n")
    print("If the histogram is skewed to the right, it indicates that most students study for fewer hours, with a few studying for many hours. \n")


if __name__ == "__main__":
    main()