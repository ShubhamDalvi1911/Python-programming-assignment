'''
Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
The program should be implemented manually without using any machine Learning library.

The program should:
    1. Calculate Euclidean distance
    2. Sort distances
    3. Select K nearest neighbors
    4. Predict the class based on majority voting 

Dataset:
    Point    X     Y    Label
      A      1     2     Red
      B      2     3     Red
      C      3     1     Blue
      D      6     5     Blue

Tasks:
    1. Accept X and Y coordinates of a new point from the user.
    2. Compute Euclidean distance from all dataset points.
    3. Sort the distances
    4. Select the K = 3 nearest neighbors.
    5. Predict the class label.
'''
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

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

    # Step 2: Compute Euclidean distance from all dataset points
    distances = []
    for data in dataset:
        dist = euclidean_distance(new_x, new_y, data['x'], data['y'])
        distances.append({'point': data['point'], 'label': data['label'], 'distance': dist})

    # Step 3: Sort the distances
    distances.sort(key=lambda x: x['distance'])

    # Step 4: Select the K = 3 nearest neighbors
    k = 3
    neighbors = distances[:k]
    print("Nearest neighbors:")
    for neighbor in neighbors:
        print(f"{neighbor['point']} - Distance: {neighbor['distance']:.2f}")

    # Step 5: Predict the class label based on majority voting
    label_count = {}

    for neighbor in neighbors:
        label = neighbor['label']
        if label in label_count:
            label_count[label] = label_count[label] + 1
        else:
            label_count[label] = 1

    # Find the label with the most votes
    predicted_label = max(label_count, key=label_count.get)

    print(f"Predicted class : {predicted_label}")


if __name__ == "__main__":
    main()