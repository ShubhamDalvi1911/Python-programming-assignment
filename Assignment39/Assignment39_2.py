'''
Use the trained model to predict results from X_test.
Display predicted values along with actual values.
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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


if __name__ == "__main__":
    main()