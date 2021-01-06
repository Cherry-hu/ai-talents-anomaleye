import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('mousemovement.csv')
df1 = df[['X', 'Y', 'Wait time']]

plt.rcParams['figure.figsize'] = (20,10)

sns.heatmap(df1.corr(), cmap='coolwarm')


