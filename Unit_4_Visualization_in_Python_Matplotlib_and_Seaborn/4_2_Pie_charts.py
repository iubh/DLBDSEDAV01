# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Pie charts

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# %% generate sample data
prog_language = ['Python', 'C++', 'Java']
students = [40,22,31]

# %% create figure
fig = plt.figure(figsize=(14,8))

# add subplot
ax1 = fig.add_subplot(111)

# create pie chart
plt.pie(students, labels=prog_language, \
    autopct='%1.1f%%', explode=[0.01]*3, \
        pctdistance=0.5)