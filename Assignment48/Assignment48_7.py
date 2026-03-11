'''
write a python program to calculates TP,TN,FP,FN for the following arrays:
actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

display all four values
'''
import numpy as np

def main():
    actual = np.array([1,1,1,1,0,0,0,0])
    predicted = np.array([1,1,0,1,0,1,0,0])

    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for a , p in zip(actual,predicted):
        if a == 1 and p == 1:
            TP = TP + 1
        elif a == 0 and p == 0:
            TN = TN + 1
        elif a == 0 and p == 1:
            FP = FP + 1
        else:
            FN = FN + 1

    print("TP : ", TP)
    print("TN : ", TN)
    print("FP : ", FP)
    print("FN : ", FN)


if __name__ == "__main__":
    main()