# Imports
import 	matplotlib
import 	matplotlib.pyplot as plt
from 	pylab import *
import 	pandas as pd
import 	numpy as np
import 	os
import 	seaborn as sns

from pandas.tools.plotting import table

# Load data
df = pd.read_csv("data.csv")

# Color code being set
sns.set(color_codes=True)

# Plot graph of logistic regression
plot=sns.regplot(x="x", y="y", data=df)


fig=plot.get_figure()

# Save figure
fig.savefig("logistic_regression.png")