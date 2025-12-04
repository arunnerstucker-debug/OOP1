import pandas as pd
df = pd.read_csv("data.csv")

for x in df.index:
  Ave = (df.loc[x, "Pulse"] + df.loc[x, "Maxpulse"])/2
  df.loc[x, "Average Pulse"] = Ave
df

import matplotlib.pyplot as plt
df.plot()
plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()