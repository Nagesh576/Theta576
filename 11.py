import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(10)

# Create a DataFrame with two normal distributions
data = pd.DataFrame({
    'value': np.concatenate([np.random.normal(0, 1, 100), np.random.normal(5, 1, 100)])
})

# Calculate the IQR and determine outliers
Q1 = data['value'].quantile(0.25)
Q3 = data['value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = data[(data['value'] < lower_bound) | (data['value'] > upper_bound)]

# Print outliers
print(f"Outliers based on Box plot criteria:\n{outliers}")

# Create plots
plt.figure(figsize=(8, 6))

# Box plot
plt.subplot(2, 1, 1)
sns.boxplot(x=data['value'])
plt.title('Box Plot of Value')

# Histogram with KDE
plt.subplot(2, 1, 2)
sns.histplot(data['value'], kde=True)
plt.title('Histogram of Value')

# Show plots
plt.tight_layout()
plt.show()