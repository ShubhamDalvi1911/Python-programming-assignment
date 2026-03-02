'''
Generate confusion matrix using sklearn.
Display it using ConfusionMatrixDisplay.
Explain Clearly:
    1. True Positives (TP)
    2. True Negatives (TN)
    3. False Positives (FP)
    4. False Negatives (FN)
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

    # Model Building
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

    # Explanation of Confusion Matrix Components
    print("\nConfusion Matrix Explanation:")
    print("1. True Positives (TP): The model correctly predicted the positive class.")
    print("2. True Negatives (TN): The model correctly predicted the negative class.")
    print("3. False Positives (FP): The model incorrectly predicted the positive class (Type I error).")
    print("4. False Negatives (FN): The model incorrectly predicted the negative class (Type II error).")

if __name__ == "__main__":
    main()