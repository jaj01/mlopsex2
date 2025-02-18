import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("data.csv")

# Train K-Means Model
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df)

# Save clustered data
df.to_csv("clustered_data.csv", index=False)
print("Clustering completed. Results saved to clustered_data.csv")

# Plot clusters
plt.scatter(df['Feature1'], df['Feature2'], c=df['Cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='x')  # Cluster centers
plt.title("K-Means Clustering")
plt.savefig("clusters.png")
print("Cluster plot saved as clusters.png")
