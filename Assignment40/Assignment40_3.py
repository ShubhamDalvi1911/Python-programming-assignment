'''
Train the model using only:
1. StudyHours
2. Attendance
Compaire the accuracy with the full feature model.
Is the model still performing well?
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

def main():
     # Load the dataset
    Data = "Student_Performance_ml.csv"
    df = pd.read_csv(Data)
    print(df.head())

    # Data Analysis (EDA)
    print("\nData Analysis (EDA):")
    print(df.describe())
    print("\nMissing Values in Each Column:")
    print(df.isnull().sum())
    print("\nClass Distribution (FinalResult):")
    print(df['FinalResult'].value_counts())
    
    # Visualization
    plt.figure(figsize=(10, 6))
    sns.countplot(x='FinalResult', data=df)
    plt.title('Class Distribution of FinalResult')
    plt.xlabel('Final Result (0 = Fail, 1 = Pass)')
    plt.ylabel('Count')
    plt.show()

    # Define features and target variable
    X = df[['StudyHours', 'Attendance']]  # Independent variables
    y = df['FinalResult'] # Dependent variable

    # Split the dataset into features and target variable 80-20 %
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model Building with max_depth = 3
    model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Predicting results from X_test
    y_pred = model.predict(X_test)

    # Display predicted values along with actual values
    results_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(results_df)

    # Calculate model accuracy using accuracy_score
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    # Generate confusion matrix
    con_matrix = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=con_matrix)
    disp.plot()
    plt.title("Confusion Matrix")
    plt.show()

    
   
    
if __name__ == "__main__":
    main()
