import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

my_data = pd.read_csv('../data/iris.csv')

print(my_data.shape)
print((my_data.head()))

sns.pairplot(data=my_data)
plt.show()



