# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Scatterplots

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# %% generate sample data
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
area = (np.random.rand(N))

# %% collect data in DataFrame
df = pd.DataFrame({'x': x, 'y': y, 'area': area})

# create figure
fig = plt.figure(figsize=(14,6))

# Matplotlib
ax1 = fig.add_subplot(121)
plt.scatter(x, y, s=area*50) # factor 50 for larger scaling
plt.xlabel("x")
plt.ylabel("y")

# Seaborn
ax2 = fig.add_subplot(122)
sns.scatterplot(df["x"], df["y"], \
    size=df["area"], ax=ax2)

plt.show()

# %%
