'''
2. Data Preprocessing:
    - Check and handle missing or zero values in columns like Glucose, BloodPressure, etc.
    - Apply feature scaling using StandardScaler or MinMaxScaler.
    - Split the dataset into features(X) and target(y).
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

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
# plt.show()

# Data Preprocessing
print("Before preprocessing on the zero value : \n")
print((df == 0).sum())

cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
df[cols] = df[cols].replace(0, np.nan)
df[cols] = df[cols].fillna(df[cols].mean())

print("After preprocessing on the zero value : \n")
print((df == 0).sum())

# Split the dataset into features(X) and target(y)
X = df.drop(columns=['Outcome'])
Y = df['Outcome']

#feature scaling using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Sample data after feature scaling : \n")
print(X_scaled[:5])



