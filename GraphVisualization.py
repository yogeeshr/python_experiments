# Imports
import matplotlib
matplotlib.use('Agg')
from pylab import *
import pandas as pd
import numpy as np

df = pd.read_csv("population_data.csv")

# Column headers
list_of_column=df.columns.tolist()
print list_of_column

# Population Graph graph
pivot_data = pd.pivot_table(df, index=["State"], values=["Population_2011"], aggfunc=np.sum)
my_plot = pivot_data.plot(kind='line', color='tab:brown', grid=True, marker='.', markersize=15, linewidth=2, title='Population Data')
my_plot.set_ylabel('State(s)')
my_plot.set_ylabel('Population')
plt.tight_layout()
fig = my_plot.get_figure()
fig.savefig("state_population.png")

# Population Graph graph
pivot_data = pd.pivot_table(df, index=["State"], values=["Male", "Female"], aggfunc=np.sum)
my_plot = pivot_data.plot(kind='bar', title='Male-Female Comparision State Wise')
my_plot.set_ylabel('State(s)')
my_plot.set_ylabel('Population')
plt.tight_layout()
fig = my_plot.get_figure()
fig.savefig("geneder_population_compare.png")