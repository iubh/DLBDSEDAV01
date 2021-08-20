# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Associations and relations

## Scatterplots

# %% import modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %% load sample data
penguins = sns.load_dataset("penguins")

# %% create figure with six subplots
fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(20,6))

# scatter plot with one variable
sns.scatterplot(data=penguins, x="bill_length_mm", \
    y="flipper_length_mm",ax=ax1)

# scatter plot with additional grouping into species by colors
sns.scatterplot(data=penguins, x="bill_length_mm", \
    y="flipper_length_mm", hue="species",ax=ax2)

# bubble plot
sns.scatterplot(data=penguins, x="bill_length_mm", \
    y="flipper_length_mm", size="bill_depth_mm",ax=ax3)

plt.show()

## KDE plots

# %% import modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %% create multivariate data from normal distribution
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 1000).T

# %% create figure with three subplots
fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(20,6))

# density contour plot
sns.kdeplot(x=x, y=y, ax=ax1)

# 2d bin plot
ax2.hist2d(x, y, bins=25, cmap='Blues')

# hex-bin plots
ax3.hexbin(x, y, gridsize=25, cmap='Blues')

plt.show()

## Line plots

# %% import modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %% load flights dataset
flights = sns.load_dataset("flights")

# %% get data for January
jan_flights = flights.query("month == 'Jan'")

# %% create figure with two subplots
fig, (ax1,ax2) = plt.subplots(1,2, figsize=(14,6))

# line plot
sns.lineplot(data=jan_flights, x="year", \
    y="passengers", ax=ax1)

# line plot including confidence band
sns.lineplot(data=flights, x="year", \
    y="passengers", ax=ax2)

plt.show()
