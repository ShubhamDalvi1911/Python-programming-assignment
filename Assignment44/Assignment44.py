import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main():
    Border = "-"* 50

    # Get data
    print(Border)
    print("Step 1 : Load the data")
    print(Border)

    df = pd.read_csv("Advertising.csv")
    print(df.head())

    # Clean, Prepare and Manipulate
    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate")
    print(Border)

    print("Shape before cleaning dataset : ",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns='Unnamed: 0', inplace=True)

    print("Shape after cleaning dataset : ",df.shape)

    # Train Data
    print(Border)
    print("Step 3 : Trian Data")
    print(Border)   

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of independent variables : ", X.shape)
    print("Shape of dependent variables : ", Y.shape)

    X_train,  X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.5, random_state=42)

    print("X_train shape : ", X_train.shape) 
    print("X_test shape : ", X_test.shape) 
    print("Y_train shape : ", Y_train.shape) 
    print("Y_test shape : ", Y_test.shape) 

    model = LinearRegression()

    model.fit(X_train,Y_train)

    # Test the  data
    print(Border)
    print("Step 4 : Test the Data")
    print(Border)  

    Y_pred = model.predict(X_test)

    # Compare the actual and predicted values
    print(Border)
    print("Step 5 : Compare the actual and predicted values")
    print(Border)

    result = pd.DataFrame({
        'Actual' : Y_test.values,
        'Predicted' : Y_pred
    })

    print(result)


if __name__ == "__main__":
    main()