# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Introduction to matplotlib

## Basics

# %% import modules
import matplotlib.pyplot as plt

# %% create an empty figure
fig = plt.figure()

# %% inspect the data type of the figure
type(fig)
# console output:
# matplotlib.figure.Figure

# %% add an axis to the figure
# coordinates of the lower left point, width and height
ax = fig.add_axes([0,0,1,1])

# %% add an axis to the figure
# grid of two rows and three columns
# position 1
ax1 = fig.add_subplot(231)

# %% add an axis to the figure
# grid of two rows and three columns
# position 4
ax2 = fig.add_subplot(234)

# %% add an axis to the figure
# grid of two rows and three columns
# position 3
ax3 = fig.add_subplot(233)

# %% create a simple line plot
from numpy import linspace
x = linspace(0,10)
y = 2*x
l1 = ax3.plot(x, y)

# %% add artists
ax3.set_title("xy plot example")
ax3.set_xlabel('x label')
ax3.set_ylabel('y label')

## Plot of two lines

# %% import modules
import matplotlib.pyplot as plt
import numpy as np

# create a figure
fig = plt.figure()

# generate sample data
x = np.linspace(0,10)
y1 = 2*x
y2 = 1.5*x

# add subplot to the figure
ax = fig.add_subplot(111)

# add the lines
ax.plot(x, y1)
ax.plot(x, y2)

# set artists
ax.set_xlabel("x label")
ax.set_ylabel("y label")
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_xticklabels(['zero', 'two', 'four', \
    'six', 'eight', 'ten'])
ax.set_yticks([0, 10, 20])

# add legend and show the plot
ax.legend(labels = ('y=2x', 'y=1.5x'), loc = 'lower right')
plt.show()

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

# %%
