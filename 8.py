import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data={
    'semester':['sem 1','sem 1','sem 1','sem 1','sem 1','sem 1','sem 2','sem 2','sem 2','sem 2'],
    'hours_studied':[5,8,10,4,6,9,11,7,12,8]
}
df=pd.DataFrame(data)
plt.figure(figsize=(10,6))
sns.barplot(x='semester',y='hours_studied',data=df)
plt.title('Hours Studied per Semester')
plt.xlabel('Semester')
plt.ylabel('Hours Studied')
plt.show()
#Python Program