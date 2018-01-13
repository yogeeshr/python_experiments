# Imports
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
import pandas as pd
import numpy as np
import os
import seaborn as sns

from pandas.tools.plotting import table

# Load data
df = pd.read_csv("linear.csv")

# Color code being set
sns.set(color_codes=True)

# Plot graph of linear regression
plot=sns.lmplot(x='x',y='y',data=df, fit_reg=True)

# Save figure
plot.savefig("linear_regression.png")