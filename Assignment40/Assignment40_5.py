'''
Without using accuracy_score, manually calculate accuracy:
verify whether it matches sklearn accuracy.
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

    t_df = pd.DataFrame({
        'StudyHours': [2, 4, 6, 8, 10],
        'Attendance': [80, 85, 90, 95, 100],
        'PreviousScore': [50, 60, 70, 80, 90],
        'AssignmentsCompleted': [2, 3, 4, 5, 6],
        'SleepHours': [6, 7, 8, 5, 7]
    })

    t_df_Actual = [0, 0, 1, 1, 1]  # Actual results for the new students

    # Data Analysis (EDA)
    print("\nData Analysis (EDA):")
    print(df.describe())
    print("\nMissing Values in Each Column:")
    print(df.isnull().sum())
    print("\nClass Distribution (FinalResult):")
    print(df['FinalResult'].value_counts())
    
    # Visualization
    '''
    plt.figure(figsize=(10, 6))
    sns.countplot(x='FinalResult', data=df)
    plt.title('Class Distribution of FinalResult')
    plt.xlabel('Final Result (0 = Fail, 1 = Pass)')
    plt.ylabel('Count')
    plt.show()
    '''

    # Define features and target variable
    X = df.drop(columns=['FinalResult'])  # Independent variables
    y = df['FinalResult'] # Dependent variable

    # Split the dataset into features and target variable 80-20 %
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model Building with max_depth = 3
    model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Predicting results from X_test
    y_pred = model.predict(t_df)

    # Display predicted values along with actual values
    results_df = pd.DataFrame({'Actual': t_df_Actual, 'Predicted': y_pred})
    print(results_df)

    # Calculate model accuracy using accuracy_score
    accuracy = accuracy_score(t_df_Actual, y_pred)
    print(f"Model Accuracy on New Students: {accuracy * 100:.2f}%")
    
    # Manually calculate accuracy
    correct_predictions = 0
    wrong_predictions = 0
    len_results = len(t_df_Actual)  

    for Actual , Predicted in zip(t_df_Actual , y_pred):
        if Actual == Predicted:
            correct_predictions = correct_predictions + 1
        else:
            wrong_predictions = wrong_predictions + 1
    
    print(f"Correct Predictions: {correct_predictions}")
    print(f"Wrong Predictions: {wrong_predictions}")

    manual_accuracy = (correct_predictions / len_results) * 100 
    print(f"Manually Calculated Accuracy: {manual_accuracy:.2f}%")
    
if __name__ == "__main__":
    main()
