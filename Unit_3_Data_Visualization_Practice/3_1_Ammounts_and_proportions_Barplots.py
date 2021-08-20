# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Ammounts and Proportions - Barplots

# %% import pyplot from matplotlib toolkit
import matplotlib.pyplot as plt
import numpy as np

# %% define categories of programming languages and quantities
prog_language = ['Python', 'C++', 'Java']
students = [40,22,31]

# %% create figure
fig = plt.figure()

# %% create a bar plot
# set axes values
plt.bar(prog_language,students)

# set axes labels
plt.xlabel('Programming language')
plt.ylabel('Number of students')

# show the figure
plt.show()

# %% create dot plot
plt.scatter(prog_language,students)

# set limits of y-axis
plt.ylim((0, 45))

# add x- and y-axis labels
plt.xlabel('Programming language')
plt.ylabel('Number of students')

# show the figure
plt.show()

# %% create pie chart
plt.pie(students, labels=prog_language, autopct='%1.1f%%')

# show figure
plt.show()

# %% define categories of programming languages and quantities
prog_language = ['Python', 'C++', 'Java']
male = [20,11,10]
female = [15,7,11]

# %% the label locations
x = np.arange(len(prog_language)) 

# the width of the bars 
width = 0.35  

# %% create figure with two subfigures
fig, (ax1,ax2) = plt.subplots(1,2)

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

# create stacked bar plot
ax2.bar(prog_language, male, width, label='Male')
ax2.bar(prog_language, female, width, bottom=male, label='Female')

# add x- and y-axis labels
ax2.set_xlabel('Programming language')
ax2.set_ylabel('Number of students')

ax2.legend()

# show figure
plt.show()
