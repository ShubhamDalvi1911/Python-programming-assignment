'''
Write a single structued python program that performs:
    1. Dataset loading
    2. Data Analysis (EDA)
    3. Visualization
    4. Train-Test Split
    5. Model training 
    6. Prediction
    7. Accuracy calculation
    8. Confusion Matrix generation
    9. Final conclusion
    Your code should include proper comments explaining each step.
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
    X = df.drop(columns=['FinalResult'])  # Independent variables
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

    # Final Conclusion
    print("\nFinal Conclusion:")
    if accuracy >= 0.8:
        print("The model has good accuracy and can be used for predictions.")
    elif accuracy >= 0.6:
        print("The model has moderate accuracy and may require further tuning.")
    else:
        print("The model has low accuracy and may not be suitable for predictions.")

    
   
    
if __name__ == "__main__":
    main()