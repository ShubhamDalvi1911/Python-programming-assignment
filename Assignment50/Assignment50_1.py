'''
1. Load and Explore the Dataset
    Handle missing or unknown values (e.g., unknown in categorical features).
    Display basic stats and visualize class distribution.
'''
import pandas as pd

# Load the dataset
df = pd.read_csv("bank.csv")
print(df.head())

# Handle missing or unknown values
print(df.isnull().sum())
