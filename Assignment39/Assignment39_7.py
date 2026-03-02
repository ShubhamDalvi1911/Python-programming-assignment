'''
Use the trained model to predict results for a student with:
    1. StudyHours  = 6
    2. Attendance = 85
    3. PreviousScore = 66
    4. AssignmentCompleted = 7
    5. SleepHours = 7
    will the student pass or fail?
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def main():
     # Load the dataset
    Data = "Student_Performance_ml.csv"
    df = pd.read_csv(Data)
    print(df.head())

    # Define features and target variable
    X = df.drop(columns=['FinalResult'])  # Independent variables
    y = df['FinalResult'] # Dependent variable

    # Split the dataset into features and target variable 80-20 %
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model Building with max_depth = 3
    model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    Test_data = [[6, 85, 66, 7, 7]]  # StudyHours, Attendance, PreviousScore, AssignmentCompleted, SleepHours
    
    prediction = model.predict(Test_data)
    
    if prediction[0] == 1:
        print("The student is predicted to : Pass")
    else:
        print("The student is predicted to : Fail")

   
    
if __name__ == "__main__":
    main()