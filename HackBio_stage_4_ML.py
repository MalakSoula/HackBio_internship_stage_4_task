# Load libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Load the gene expression data
gene_data = pd.read_csv('New_data.csv')
labels = pd.read_csv('labels1.csv')

# Display shapes of the datasets
print(f"Labels Shape: {labels.shape}")
print(f"Gene Data Shape: {gene_data.shape}")

# Separate gene IDs from gene data
gene_ids = gene_data.iloc[:, 0]  # Assuming the first column is gene IDs
gene_data = gene_data.iloc[:, 1:]

# Normalize the numeric expression data
scaler = StandardScaler()
gene_data_normalized = pd.DataFrame(scaler.fit_transform(gene_data), columns=gene_data.columns)

# Apply K-Means clustering on normalized gene data
kmeans = KMeans(n_clusters=6, random_state=42)  # Assume 6 clusters based on the six IDH statuses
clusters = kmeans.fit_predict(gene_data_normalized)

# Add cluster labels to the normalized data
gene_data_normalized['Cluster'] = clusters

# Calculate and print the silhouette score to assess clustering quality
silhouette_avg = silhouette_score(gene_data_normalized.drop(columns='Cluster'), clusters)
silhouette_percentage = silhouette_avg * 100
print(f'Silhouette Score: {silhouette_percentage:.2f}%')

# Plot the clusters using the first two features of the normalized data
plt.figure(figsize=(10, 7))

# Create a color map for clusters
scatter = plt.scatter(gene_data_normalized.iloc[:, 0], gene_data_normalized.iloc[:, 1], c=clusters, cmap='viridis', marker='o')

# Create color legend
legend1 = plt.legend(*scatter.legend_elements(), title="Clusters")
plt.gca().add_artist(legend1)

plt.title('K-Means Clustering of Gene Expression Data (First Two Features)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster')
plt.show()
