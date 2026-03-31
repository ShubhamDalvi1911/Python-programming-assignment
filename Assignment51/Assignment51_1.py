'''
Part 1: Data Preprocessing
    1. Load the dataset using Pandas
    2. Drop null values and select useful columns (title or text)
    3. Convert the target variable (label) to binary (0 or 1)
'''
import pandas as pd

# Load the dataset using Pandas
df = pd.read_csv("Fake.csv")
print("Some records of data : \n",df.head())

# Drop null values and select useful columns
print("Null Values are : \n", df.isnull().sum())
