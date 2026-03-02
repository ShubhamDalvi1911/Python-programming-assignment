'''
Train three Decision Tree models with:
    1. max_depth = 1
    2. max_depth = 3
    3. max_depth = None
    Compare their testing accuracies and write your observations.
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def DCT_model(model):
    # Load the dataset
    Data = "Student_Performance_ml.csv"
    df = pd.read_csv(Data)
    print(df.head())

    # Define features and target variable
    X = df.drop(columns=['FinalResult'])  # Independent variables
    y = df['FinalResult'] # Dependent variable

    # Split the dataset into features and target variable 80-20 %
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

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

    return accuracy

def main():
    Border = "=" * 100
    print(Border)

    # Model Building with max_depth = 1
    model1 = DecisionTreeClassifier(criterion='gini', max_depth=1)
    accuracy_1 = DCT_model(model1)
    print(Border)

    # Model Building with max_depth = 3
    model2 = DecisionTreeClassifier(criterion='gini', max_depth=3)
    accuracy_3 = DCT_model(model2)
    print(Border)

    # Model Building with max_depth = None
    model3 = DecisionTreeClassifier(criterion='gini', max_depth=None)
    accuracy_none = DCT_model(model3)
    print(Border)

    # Observations
    print("\nObservations:")
    if accuracy_1 < accuracy_3 and accuracy_3 < accuracy_none:
        print("The model with max_depth = None has the highest accuracy, indicating that it may be overfitting the training data.")
    elif accuracy_1 > accuracy_3 and accuracy_3 > accuracy_none:
        print("The model with max_depth = 1 has the highest accuracy, indicating that it may be underfitting the training data.")
    else:
        print("The model with max_depth = 3 has a balanced accuracy, suggesting it may be the best choice among the three models.")


if __name__ == "__main__":
    main()