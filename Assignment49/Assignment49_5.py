'''
5. Final Output:
    Predict whether a patient is diabetic based on test data.
    Display predictions on screen and save them in a CSV file.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import  DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

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

soft_model = VotingClassifier(
    estimators=[
        ('lr',model_LR),
        ('knn',model_KNN),
        ('dt',model_DT)
    ],
    voting='soft'
)

soft_model.fit(X_train,Y_train)

# Print accuracy score, confusion matrix, precision, recall, and F1 score.
y_pred = soft_model.predict(X_test)

accracy = accuracy_score(y_pred,Y_test)
cm = confusion_matrix(y_pred,Y_test)

print("Accuracy of model is : ", accracy*100)
print("confusion matrix : \n", cm)
print("precision, recall, and F1 score : \n",classification_report(y_pred,Y_test))

# Use matplotlib or seaborn to visualize confusion matrix.
plt.figure(figsize=(8,5))
sns.heatmap(cm,annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

joblib.dump(soft_model,"diabetes_model.pkl")