# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Time Series

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# %% generate sample data
x = np.linspace(0, 10)
y = np.sin(x)

# generate 10-fold variation of the data
y_col = y
x_col = x
for i in range(0, 10):
    
    # generate error to be added to the data
    error = np.random.normal(0.2, 0.01, size=y.shape)
    
    # generate values for y
    y += np.random.normal(0, 0.2, size=y.shape)
    
    # collect random variations of y and
    # repeated values for x
    y_col = np.append(y_col, y)
    x_col = np.append(x_col, x)

# %% Matplotlib
plt.plot(x, y)
plt.fill_between(x, y-error, y+error, alpha=0.4)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# %% Seaborn
sns.lineplot(x_col, y_col)

# %% Seaborn
# CI controls: change n_boot to 2 and/or err_style to "bars"
sns.lineplot(x_col, y_col, n_boot=1000, err_style="band")