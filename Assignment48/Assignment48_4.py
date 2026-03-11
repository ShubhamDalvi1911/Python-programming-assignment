'''
write a python program to calculate the Euclidean distance between two points before and after 
applying feature scaling and explain the difference in results.
'''
import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    data = np.array([[25, 20000],[30, 40000],[35, 80000]])

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(data)

    # Calculate distance
    distance = np.linalg.norm(data)

    print("The euclidean distance : ", distance)

    distance = np.linalg.norm(scaled_data)

    print("The euclidean distance after scaling : ", distance)    

if __name__ == "__main__":
    main()