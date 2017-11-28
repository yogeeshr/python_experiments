# Imports
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pylab import *
import pandas as pd
import numpy as np
import os

from pandas.tools.plotting import table

df = pd.read_csv("population_data.csv")

# Column headers
list_of_column=df.columns.tolist()
print list_of_column

# Population Graph graph
pivot_data = pd.pivot_table(df, index=["State"], values=["Population_2011"], aggfunc=np.sum)
my_plot = pivot_data.plot(kind='line', color='brown', grid=True, marker='.', markersize=15, linewidth=2, title='Population Data')
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
fig.savefig("gender_population_compare.png")

# Pie chart - Density Graph
plt.subplots()
plt.pie(df['Density_per_km2'], pctdistance=.8, labels=df['State'], autopct='%1.1f%%',
        shadow=False, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Density Per Km2 Pie")
plt.tight_layout()
plt.savefig("Density_KM2.png")

#HTML of Pivot Data
population_html=pivot_data.to_html(justify='left').replace('<th>','<th style = "background-color: lightgrey; padding:3px; text-align:center;">')

text_file = open("population.html", "w")
text_file.write("%s" % population_html)
text_file.close()
