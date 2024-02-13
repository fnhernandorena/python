#Requires pandas, matplotlib and seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv('csv/grafico.csv')

sb.lineplot(x='x',y='y', data = df)

#sb.barplot(x='x',y='y', data = df)

plt.show()