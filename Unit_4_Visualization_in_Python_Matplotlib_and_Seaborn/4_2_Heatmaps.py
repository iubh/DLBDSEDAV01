# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Heatmaps

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# %% generate sample data
prog_language = ['Python', 'C++', 'Java']
sex=['male', 'female']
students = np.array([[20, 11, 10], [15, 7, 11]])

df = pd.DataFrame([ \
    ['Python', 20, 'male'], \
    ['C++',  11, 'male'], \
    ['Java', 10, 'male'], \
    ['Python', 15, 'female'], \
    ['C++', 7, 'female'], \
    ['Java', 11, 'female']], \
        columns=['Programming language', \
            'Number of students', 'sex'])

amounts = df.pivot("sex", "Programming language", \
    "Number of students")

# %% create figure
fig = plt.figure(figsize=(14,3))

# Matplotlib heatmap
ax1 = fig.add_subplot(121)
im = ax1.imshow(students)
ax1.set_xticks(np.arange(len(prog_language)))
ax1.set_yticks(np.arange(len(sex)))

ax1.set_xticklabels(prog_language)
ax1.set_yticklabels(sex)
for i in range(len(sex)):
    for j in range(len(prog_language)):
        text = ax1.text(j, i, students[i, j],
                       ha="center", va="center", color="w")

# Seaborn heatmap
ax2 = fig.add_subplot(122)
sns.heatmap(amounts, annot=True, ax=ax2)

plt.show()

# %%
