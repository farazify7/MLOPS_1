# iris_data.py

from sklearn.datasets import load_iris
import pandas as pd

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Save to CSV file
df.to_csv('iris_data.csv', index=False)
print("Iris dataset saved as 'iris_data.csv'")
