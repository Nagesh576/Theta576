# Set the random seed for reproducibility
np.random.seed(42)

# Generate random data
data = np.random.randn(20, 81, 1000)

# Flatten the data to 1D for histogram plotting
flattened_data = data.flatten()

# Create the histogram
plt.hist(flattened_data, bins=10, edgecolor='black', color='skyblue')

# Set the title and labels
plt.title('Histogram of Cancer Patients Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Patients')

# Show the plot
plt.show()