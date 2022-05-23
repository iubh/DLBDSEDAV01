# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Distributions

## Histograms and density plots

# %% import modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %% draw 100 samples from normal distribution
x = np.random.randn(100)

# %% create figure with six subplots
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6)) = plt.subplots(2,3, \
                                        figsize=(12,6))

# histograms with different number of bins
sns.histplot(x, bins=5, ax=ax1)
sns.histplot(x, bins=20, ax=ax2)
sns.histplot(x, bins=40, ax=ax3)

# histogram with estimated density function
sns.histplot(x, bins=5, kde=True, ax=ax4)

# cumulative histogram
sns.histplot(x, bins=20, element="step", fill=False,
             cumulative=True, stat="density", ax=ax5)

# cumulative density function
sns.kdeplot(x, cumulative=True, ax=ax6)

plt.show()

## Stacked histograms and overlapping density plots

# %% load sample data
penguins = sns.load_dataset("penguins")

# %% create figure with six subplots
fig, (ax1,ax2) = plt.subplots(1,2, figsize=(12,6))

# stacked histogram
sns.histplot(penguins, x="flipper_length_mm", \
    hue="species", multiple="stack", ax=ax1)

# overlapping density plot
sns.kdeplot(data=penguins, x="flipper_length_mm", \
    hue="species", multiple="stack", ax=ax2)

plt.show()
