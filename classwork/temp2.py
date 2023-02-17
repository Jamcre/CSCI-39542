import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set()
ti = sns.load_dataset('titanic').dropna().reset_index(drop=True)

sns.histplot(data=ti['age'], kde=True, bins=60)
plt.show()

sns.boxplot(x='fare', data=ti)
plt.show()

sns.lmplot(x='age', y='fare', hue='who', data=ti, fit_reg=False)
plt.show()

sns.countplot(x='alive', data=ti)
plt.show()

sns.pointplot(x='alive', y='age', data=ti)
plt.show()
