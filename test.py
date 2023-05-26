#! /usr/bin/python3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Value1': [10, 20, 15, 25, 30, 35],
    'Value2': [5, 15, 10, 20, 25, 30]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(8, 6))

# Plot the first variable
sns.lineplot(x=df.index, y='Value1', data=df, label='Value 1')

# Plot the second variable on the same subplot
sns.lineplot(x=df.index, y='Value2', data=df, label='Value 2')

# Set plot labels and title
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Overlap of Value 1 and Value 2')

# Show the plot
plt.show()
