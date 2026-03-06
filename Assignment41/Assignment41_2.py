'''
The value of K plays an important role in the KNN algorithm.
Write a python program that demonstrates how prediction changes when K changes.

Dataset:
    Point    X     Y    Label
      A      1     2     Red
      B      2     3     Red
      C      3     1     Blue
      D      6     5     Blue

Tasks:
    Predict the class of the same new point using:
    1. K = 1
    2. K = 3
    3. K = 5
'''
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def UD_KNN(new_x, new_y, dataset, k):
    # Compute Euclidean distance from all dataset points
    distances = []
    for data in dataset:
        dist = euclidean_distance(new_x, new_y, data['x'], data['y'])
        distances.append({'point': data['point'], 'label': data['label'], 'distance': dist})

    # Sort the distances
    distances.sort(key=lambda x: x['distance'])

    # Select the K nearest neighbors
    neighbors = distances[:k]

    # Predict the class label based on majority voting
    label_count = {}

    for neighbor in neighbors:
        label = neighbor['label']
        if label in label_count:
            label_count[label] = label_count[label] + 1
        else:
            label_count[label] = 1

    # Find the label with the most votes
    predicted_label = max(label_count, key=label_count.get)
    return predicted_label

def main():
    # Dataset
    dataset = [
        {'point': 'A', 'x': 1, 'y': 2, 'label': 'Red'},
        {'point': 'B', 'x': 2, 'y': 3, 'label': 'Red'},
        {'point': 'C', 'x': 3, 'y': 1, 'label': 'Blue'},
        {'point': 'D', 'x': 6, 'y': 5, 'label': 'Blue'}
    ]


    # Step 1: Accept X and Y coordinates of a new point from the user
    new_x = float(input("Enter X coordinate : "))
    new_y = float(input("Enter Y coordinate : "))

    # Predict the class of the new point using different values of K
    for k in [1, 3, 5]:
        predicted_label = UD_KNN(new_x, new_y, dataset, k)
        print(f"K = {k}: Predicted Label = {predicted_label}")



if __name__ == "__main__":  
    main()