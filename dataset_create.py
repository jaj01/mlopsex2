import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
data = np.random.rand(100, 2) * 100  # 100 points in 2D space

# Save dataset for later use
df = pd.DataFrame(data, columns=['Feature1', 'Feature2'])
df.to_csv("data.csv", index=False)
print("Dataset saved as data.csv")
