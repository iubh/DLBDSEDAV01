# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Amounts

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

## Simple bar plots

# %% define categories of programming languages and quantities
prog_language = ['Python', 'C++', 'Java']
students = [40,22,31]

# %% create figure
fig = plt.figure(figsize=(14,8))

# add subplot
ax1 = fig.add_subplot(231)

# create bar plot
plt.bar(prog_language, students)

# add x- and y-axis labels
plt.xlabel('Programming language')
plt.ylabel('Number of students')

# add subplot
ax2 = fig.add_subplot(232)

# create bar plot
ax2.bar(prog_language, students)

# add x- and y-axis labels
ax2.set_xlabel('Programming language')
ax2.set_ylabel('Number of students')

# create subplot
ax3 = fig.add_subplot(233)

# create Pandas dataframe
df = pd.DataFrame([ \
    ['Python', 40], \
    [ 'C++',  22], \
    [ 'Java',  31]], \
        columns=['Programming language', \
            'Number of students'])

# create bar plot
sns.barplot(df["Programming language"], \
    df["Number of students"])

# add subplot
ax4 = fig.add_subplot(234)

# create bar plot
plt.barh(prog_language, students)

# add x- and y-axis labels
plt.ylabel('Programming language')
plt.xlabel('Number of students')

# add subplot
ax5 = fig.add_subplot(235)

# create barplot
sns.barplot(df["Number of students"], \
    df["Programming language"], orient="h")

# show figure
plt.show()

## Stacked bar plots

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# %% generate sample data
prog_language = ['Python', 'C++', 'Java']
male = [20, 11, 10]
female = [15, 7, 11]

# %% create figure
fig = plt.figure(figsize=(14,8))

# add subplot
ax1 = fig.add_subplot(121)

# the label locations
x = np.arange(len(prog_language)) 

# the width of the bars 
width = 0.35  

# create grouped bar plot
ax1.bar(x - width/2, male, width, label='Male')
ax1.bar(x + width/2, female, width, label='Female')

# add x- and y-axis labels
ax1.set_xlabel('Programming language')
ax1.set_ylabel('Number of students')

# add legend and adapt tick labels
ax1.legend()
ax1.set_xticks(x)
ax1.set_xticklabels(prog_language)

# add subplot
ax2 = fig.add_subplot(122)

# create Pandas dataframe
df = pd.DataFrame([ \
    ['Python', 20, 'male'], \
    ['C++', 11, 'male'], \
    ['Java', 10, 'male'], \
    ['Python', 15, 'female'], \
    ['C++', 7, 'female'], \
    ['Java', 11, 'female']], \
        columns=['Programming language', \
            'Number of students', 'sex'])

# create bar plot
sns.barplot(df["Programming language"], \
    df["Number of students"], hue=df["sex"])

# show figure
plt.show()

# %%
