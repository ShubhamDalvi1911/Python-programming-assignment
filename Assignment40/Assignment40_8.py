'''
Decision Tree Visualization
Use:
from sklearn.tree import plot_tree
visualize the trained decision tree.
    1. Which feature appears at the root node?
    2. Why do you think that feature was selected first?
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import plot_tree

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
    y_pred = model.predict(X_test)

    # Display predicted values along with actual values
    results_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(results_df)

    # Calculate model accuracy using accuracy_score
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy on Test Students: {accuracy * 100:.2f}%")
    
    # Visualize the decision tree
    plt.figure(figsize=(12, 8))
    plot_tree(model, feature_names=X.columns, class_names=['Fail', 'Pass'], filled=True)
    plt.title('Decision Tree Visualization')
    plt.show()

    # Identify the feature at the root node
    root_feature = model.tree_.feature[0]
    print(f"Feature at the root node: {X.columns[root_feature]}")

    # Explanation for feature selection at the root node
    print(f"The feature '{X.columns[root_feature]}' was selected at the root node because it provides the best split based on the Gini impurity criterion, which helps to maximize the separation of classes (Pass vs Fail) at the first level of the tree.")
    
if __name__ == "__main__":
    main()
