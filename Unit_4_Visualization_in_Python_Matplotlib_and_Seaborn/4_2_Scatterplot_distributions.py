# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Scatterplot Distributions

# %% import modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# %% create multivariate normal distribution
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 1000).T
df = pd.DataFrame({'x': x, 'y': y})

# %% create figure 
fig = plt.figure(figsize=(14,4))

# 2d bin plot with Matplotlib
ax1 = fig.add_subplot(131)
ax1.hist2d(x, y, bins=25, cmap='Blues')
ax1.set_xlabel("x")
ax1.set_ylabel("y")

# hex-bin plot with Matplotlib
ax2 = fig.add_subplot(132)
ax2.hexbin(x, y, gridsize=25, cmap='Blues')
ax2.set_xlabel("x")
ax2.set_ylabel("y")

# density contour plot with Seaborn
ax3=fig.add_subplot(133)
sns.kdeplot(x=x,y=y, ax=ax3)
ax3.set_xlabel("x")
ax3.set_ylabel("y")

plt.show()

# %%
