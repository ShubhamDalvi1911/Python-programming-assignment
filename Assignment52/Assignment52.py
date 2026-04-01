import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    # Load the dataset
    print("Step 1 : Load the dataset")
    df = pd.read_csv("student.csv")
    print(df.head())

    # Select Featurs 
    print("\nStep 2 : Select Featurs ")
    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]

    print("\nSelected featurs : ")
    print(X.head())

    # Step 3 : Scale the data
    print("\nStep 3 : Scale the data")
    scaler = StandardScaler()
    X_Scaled = scaler.fit_transform(X)

    print("\nData after scalling : ")
    print(X_Scaled[:5])

    # Step 4 : Train the model
    model = KMeans(n_clusters=3,random_state=42,n_init=10)
    cluster  = model.fit_predict(X_Scaled)

    df["Cluster"] = cluster

    print("Dataset with cluster")
    print(df.head(30))

    # Step 5: Analyze cluster centers
    print("\nCluster Centers (Scaled):")
    print(model.cluster_centers_)

    # Convert centers back to original scale for understanding
    centers = scaler.inverse_transform(model.cluster_centers_)
    centers_df = pd.DataFrame(centers, columns=X.columns)

    print("\nCluster Centers (Original Scale):")
    print(centers_df)

    # Step 6: Assign Meaningful Labels
    # Sort clusters based on performance (PreviousScore + StudyHours)
    centers_df['PerformanceScore'] = centers_df['PreviousScore'] + centers_df['StudyHours']
    sorted_clusters = centers_df.sort_values(by='PerformanceScore', ascending=False)

    label_map = {}
    label_map[sorted_clusters.index[0]] = "Top Performer"
    label_map[sorted_clusters.index[1]] = "Average Student"
    label_map[sorted_clusters.index[2]] = "Struggling Student"

    # Map labels
    df['Category'] = df['Cluster'].map(label_map)

    print("\nFinal Dataset with Labels:")
    print(df.head(30))

if __name__ == "__main__":
    main()