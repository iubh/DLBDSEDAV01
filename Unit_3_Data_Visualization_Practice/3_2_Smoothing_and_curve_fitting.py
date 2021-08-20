# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Smoothing and Curve Fitting

## Moving averages

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from IPython.display import Image

# %% load Covid-19 dataset and query data for New York
data_url = "http://covidtracking.com/api/states/daily.csv"
corona = pd.read_csv(data_url, parse_dates=['date'])
corona_ny = corona.query("state=='NY'")

# %%
# calculate SMA with time windows of one, two and four weeks.
# The smoothed curve becomes shorter due to the calculation 
# of the sum of multiple values, which is why we had to apply 
# a shifting of  the data.
corona_ny['mva_7day'] = corona_ny.positiveIncrease.\
    rolling(7).mean().shift(-3)
corona_ny['mva_14day'] = corona_ny.positiveIncrease.\
    rolling(14).mean().shift(-7)
corona_ny['mva_28day'] = corona_ny.positiveIncrease.\
    rolling(28).mean().shift(-14)

# %% create figure 
fig, ax = plt.subplots(figsize=(14,6))

# raw data
sns.lineplot(x="date", y="positiveIncrease", \
    label="Daily cases", data=corona_ny, ax=ax)

# SMA one week
sns.lineplot(x="date",y="mva_7day", \
    label="SMA one week", data=corona_ny, ax=ax)

# SMA two weeks
sns.lineplot(x="date",y="mva_14day", \
    label="SMA two weeks", data=corona_ny, ax=ax)

# SMA four weeks
sns.lineplot(x="date",y="mva_28day", \
    label="SMA four weeks", data=corona_ny, ax=ax)

ax.set_xlabel("Date")
ax.set_ylabel("Daily Cases New York")

plt.show()

## Curve fitting

# %% show the formula
Image(filename='polynomial_fitting_formula.png') 

# %% extract x and y variables
x = corona_ny['date']  
y = corona_ny['positiveIncrease'] 

# %% set values for the x axis
xaxis = range(len(corona_ny.index))

# %% fit polynomials of degrees 5, 7 and 9
coefficients1 = np.polyfit(xaxis, \
    corona_ny['positiveIncrease'], 5)
coefficients2 = np.polyfit(xaxis, \
    corona_ny['positiveIncrease'], 7)
coefficients3 = np.polyfit(xaxis, \
    corona_ny['positiveIncrease'], 9)

# %% convert coefficients into polynomial objects
f1 = np.poly1d(coefficients1)
f2 = np.poly1d(coefficients2)
f3 = np.poly1d(coefficients3)

# %% create figure 
fig, ax = plt.subplots(figsize=(14,6))

# raw data
sns.lineplot(x="date", y="positiveIncrease", \
    label="Daily cases", data=corona_ny, ax=ax)

# Polynomial fit degree 5
sns.lineplot(x=x, y=f1(xaxis), \
    label="Polynomial fit degree 5", ax=ax)

# Polynomial fit degree 7
sns.lineplot(x=x, y=f2(xaxis), \
    label="Polynomial fit degree 7", ax=ax)

# Polynomial fit degree 9
sns.lineplot(x=x, y=f3(xaxis), \
    label="Polynomial fit degree 9", ax=ax)

plt.show()


