from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
iris = load_iris()
# Create KMeans model with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
# Train the model
kmeans.fit(iris.data)
# Get cluster labels
cluster_labels = kmeans.labels_
# Display cluster labels
print("Cluster Labels:")
print(cluster_labels)
