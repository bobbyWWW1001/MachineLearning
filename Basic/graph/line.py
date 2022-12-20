import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

time = pd.date_range(start='2010', periods=10, freq='Y')
val = np.random.randn(10)

# 可表达变量随着时间变化的趋势
# matplot
plt.plot(time, val)
plt.show()

# seaborn
df = pd.DataFrame({'x': time, 'y': val})

sns.lineplot(x='x', y='y', data=df)
plt.show()



