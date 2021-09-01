# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Histograms

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# %% draw 100 samples from normal distribution
x = np.random.randn(1000)

# %% create figure
fig = plt.figure(figsize=(14,8))

# Matplotlib histogram
ax1 = fig.add_subplot(221)
plt.hist(x)
plt.ylabel("Count")

# Matplotlib cumulative histogram
ax2 = fig.add_subplot(222)
plt.hist(x, cumulative=True)
plt.ylabel("Count")

# Seaborn histogram
ax3 = fig.add_subplot(223)
sns.histplot(x, ax=ax3)

# Seaborn cumulative histogram
ax4 = fig.add_subplot(224)
sns.histplot(x, cumulative=True, ax=ax4)

plt.show()

# %%
