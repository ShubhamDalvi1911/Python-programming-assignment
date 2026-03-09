import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    Border = "-"*50

    # Step 1 : Get Data
    print(Border)
    print("Step 1 : Get Data")
    print(Border)

    df = pd.read_csv("WinePredictor.csv")
    print(df.head())
 
    # Step 2 : Clean, Prepare and Manipulate data
    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(Border)
    
    # Step 3 : Train Data
    print(Border)
    print("Step 3 : Train Data")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y)

    model = DecisionTreeClassifier()

    model.fit(X_train,Y_train)

    # Step 4 : Test Data
    print(Border)
    print("Step 4 : Test Data")
    print(Border)
    y_pred = model.predict(X_test)

    # Step 5 : Calculate accuracy
    print(Border)
    print("Step 5 : Calculate accuracy")
    print(Border)   
    accuracy = accuracy_score(Y_test, y_pred)
    print("Accuracy is : ", accuracy*100)



if __name__ == "__main__":
    main()