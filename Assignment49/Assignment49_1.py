'''
1. Exploratory Data Analysis (EDA):
    Load the dataset using pandas.
    Display the first 5 rows.
    Show column info and check for null values.
    Display basic statistics using. describe().
    Plot the distribution of the target variable (Outcome).
    Use graphs like hist, boxplot, or pairplot to identify patterns or outliers.
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset using pandas.
df = pd.read_csv("diabetes.csv")

# Display the first 5 rows.
print("first five rows : ")
print(df.head())

# Show column info and check for null values.
print(df.columns)
print(df.isnull().sum())

# Display basic statistics using. describe().
print(df.describe())

# Plot the distribution of the target variable (Outcome)
plt.figure(figsize=(8,5))
plt.hist(df['Outcome'],bins=10, color='skyblue', edgecolor="black")
plt.title('distribution of the target variable ')
plt.grid(alpha = 0.3)
plt.show()