import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the DataFrame
datf = pd.DataFrame({
    "Season 1": [7, 4, 5, 6, 3],
    "Season 2": [1, 2, 8, 4, 9]
})

# Reshape the DataFrame to long format
datf_long = datf.melt(var_name='Season', value_name='Value')

# Create the histogram
p = sns.histplot(data=datf_long, x='Value', hue='Season', multiple='stack', bins=10)

# Set labels
p.set(xlabel="X Label Value", ylabel="Y Label Value")

# Show the plot
plt.show()