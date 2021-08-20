# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Decomposition

# %% import modules
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from IPython.display import Image

# %% show the formula
Image(filename='decomposition_formula.png') 

# %% load sample data
flights = sns.load_dataset("flights")

# %% decompose the time series
decomp = seasonal_decompose(flights['passengers'], \
    model='multiplicative', period=12)

# %% plot decomposition
fig, ax = plt.subplots(figsize=(14,6))
decomp.plot(figsize=(14,6))

plt.show()

# %% create a figure with 4 subplots
fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1, \
                            figsize=(15,8))

# plot decomposed time series
decomp.observed.plot(ax=ax1)
decomp.trend.plot(ax=ax2)
decomp.seasonal.plot(ax=ax3)
decomp.resid.plot(ax=ax4)

# label the data
ax1.set_ylabel("observed")
ax2.set_ylabel("trend")
ax3.set_ylabel("seasonal")
ax4.set_ylabel("residual")

plt.show()