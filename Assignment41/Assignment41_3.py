'''
Ise KNN to predict whether a student passes or fails based on study hours and attendance.

Dataset:
    Study Hours    Attendance     Result
      2                60          Fail
      5                80          Pass
      6                85          Pass
      1                50          Fail

Tasks:
    1. Accept input from user:
        a. Study hours
        b. Attendance percentage
    2. Apply KNN algorithm
    3. Predict whether the student Passes or Fails
'''
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    # Dataset
    dataset = [
        {'StudyHours': 2, 'Attendance': 60, 'Result': 'Fail'},
        {'StudyHours': 5, 'Attendance': 80, 'Result': 'Pass'},
        {'StudyHours': 6, 'Attendance': 85, 'Result': 'Pass'},
        {'StudyHours': 1, 'Attendance': 50, 'Result': 'Fail'}
    ]


    # Step 1: Accept X and Y coordinates of a new point from the user
    new_x = float(input("Enter Study Hours : "))
    new_y = float(input("Enter Attendance Percentage : "))

    # Compute Euclidean distance from all dataset points
    distances = []
    for data in dataset:
        dist = euclidean_distance(new_x, new_y, data['StudyHours'], data['Attendance'])
        distances.append({'StudyHours': data['StudyHours'], 'Result': data['Result'], 'distance': dist})

    # Sort the distances
    distances.sort(key=lambda x: x['distance'])

    # Select the K nearest neighbors
    k = 3
    neighbors = distances[:k]

    # Predict the class label based on majority voting
    label_count = {}

    for neighbor in neighbors:
        label = neighbor['Result']
        if label in label_count:
            label_count[label] = label_count[label] + 1
        else:
            label_count[label] = 1

    # Find the label with the most votes
    predicted_label = max(label_count, key=label_count.get)
    print(f"Predicted Result: {predicted_label}")



if __name__ == "__main__":  
    main()