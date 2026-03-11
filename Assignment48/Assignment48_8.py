'''
write a python program using scikit-learn to generate a classification report for the following data:
actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

display the complete classification report including precision, recall, F1-score, and support
'''
import numpy as np
from sklearn.metrics import classification_report

def main():
    actual = np.array([1,1,1,1,0,0,0,0])
    predicted = np.array([1,1,0,1,0,1,0,0])

    print(classification_report(actual , predicted))

if __name__ == "__main__":
    main()