# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Coordinates and axes

## Logarithmic scale

# %% import modules
import matplotlib.pyplot as plt

# %% generate sample data
x=[1,2,3,4,5,6,7,8,9]
y=[0,3.16,10,31.6,100,316,1000,3160,10000]

# %% plot the data with a logarithmic scale
plt.figure()
plt.plot(x, y)
plt.yscale('log')
plt.grid(True)
plt.show()

## Polar coordinate system

# %% import modules
import numpy as np
import matplotlib.pyplot as plt

# %% generate sample data
r = [10,10,10]

# %% represent angle in radian
theta = [5*np.pi/180.0,355*np.pi/180.0,15*np.pi/180.0]

# %% create plot with a polar coordinate system
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.scatter(theta, r)
ax.set_rmax(12)
ax.grid(True)
plt.show()

## An example with real data

# %% import pyplot from matplotlib toolkit and seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# %% set standars Seaborn settings
sns.set()

# %% load dataset and query for particular month
flights = sns.load_dataset("flights")
may_flights = flights.query("month == 'May'")

# %% create a figure with two subplots
fig = plt.figure()

# plot line on polar coordinate system
ax1 = fig.add_subplot(211,projection='polar')
sns.lineplot(data=may_flights, x="year", y="passengers",ax=ax1)

# plot line on cartesian coordinate system
ax2 = fig.add_subplot(212)
sns.lineplot(data=may_flights, x="year", y="passengers",ax=ax2)

plt.show()

