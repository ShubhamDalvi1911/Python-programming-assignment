'''
3. Model Building:
    Train at least 2 different algorithms on the dataset:
    Logistic Regression
    K-Nearest Neighbors (KNN)
    Decision Tree
    Use train_test_split to divide the data.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import  DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

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

# Split the dataset
X_train,X_test,Y_train,Y_test = train_test_split(X_scaled,Y, test_size=0.2, random_state=42)

# Train the model
model_LR = LogisticRegression()
model_KNN = KNeighborsClassifier()
model_DT = DecisionTreeClassifier()

model_LR.fit(X_train,Y_train)
model_KNN.fit(X_train,Y_train)
model_DT.fit(X_train,Y_train)
