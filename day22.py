import matplotlib.pyplot as plt

data = [5, 7, 7, 8, 9, 10, 10, 10, 11, 12, 11, 11]
plt.hist(data, bins=10, edgecolor='black')  # Added a comma here
plt.xlabel('Numbers')
plt.ylabel('Count')
plt.title('Simple Histogram of Data')  # Optional: Adding a title for clarity
plt.show()