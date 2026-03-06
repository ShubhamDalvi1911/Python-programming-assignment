import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    # Step 1: Get Data
    df = pd.read_csv('PlayPredictor.csv')

    # Step 2: Clean , Prepare and Manipulate Data
    df.drop(columns=['Unnamed: 0'], inplace=True)

    LE = LabelEncoder()

    df['Whether'] = LE.fit_transform(df['Whether'])
    df['Temperature'] = LE.fit_transform(df['Temperature'])
    df['Play'] = LE.fit_transform(df['Play'])

    # Step 3: Train Data
    model = KNeighborsClassifier(n_neighbors=3)

    X = df.drop(columns=['Play'])
    y = df['Play']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = model.fit(X, y)

    # Step 4: Test Data
    y_pred = model.predict(X_test)
    for i in range(len(y_test)):
        print(f"Actual: {y_test.iloc[i]}, Predicted: {y_pred[i]}")

    for i in range(len(y_pred)):
        if y_pred[i] == 0:
            print("No")
        else:
            print("Yes")

    # Step 5: Calculate Accuracy
    accuracy = accuracy_score(y_test, y_pred) * 100
    print(f"Accuracy: {accuracy:.2f}")


if __name__ == "__main__":
    main()