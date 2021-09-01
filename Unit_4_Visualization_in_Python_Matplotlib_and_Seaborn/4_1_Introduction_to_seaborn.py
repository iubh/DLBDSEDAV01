# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Introduction to seaborn

# %% import modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

## Themes

# %% set the seaborn style
# change to: whitegrid, darkgrid,
# white, dark, ticks
sns.set(style='darkgrid')

# %% generate sample data
x = np.linspace(0,10)
y1 = 2*x
y2 = 1.5*x

# %% two lines in seperate subplots

# create a figure
plt.figure(figsize=(14,10))

# two subplots in two rows and one column
# first position
plt.subplot(211)
plt.plot(x ,y1)
plt.title('Subplot 211')
plt.xlabel('x label 211')
plt.ylabel('y label 211')

# second position
plt.subplot(212)
plt.plot(x, y2)
plt.title('Subplot 211')
plt.xlabel('x label 211')
plt.ylabel('y label 211')

# show the plot
plt.show()

## Aesthetics

# %% load sample data
tips = sns.load_dataset("tips")

# %% create scatterplot (i.e. bubble plot)
sns.relplot(data=tips, x="total_bill", y="tip", \
    hue="smoker", style="smoker", size="size")

plt.show()
