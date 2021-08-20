# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Using color

## Example 1

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns

# %% load sample data
penguins = sns.load_dataset("penguins") # load dataset

# %% create figure with subplots
fig, (ax1,ax2) = plt.subplots(nrows=2, sharex=True)

# overlapping density plot with badly chosen color palette
sns.kdeplot(data=penguins, x="flipper_length_mm", \
    hue="species", fill=True, common_norm=False, \
    palette="crest", alpha=.5, linewidth=0, ax=ax1)

# overlapping density plot with well chosen color palette
sns.kdeplot(data=penguins, x="flipper_length_mm", \
    hue="species", fill=True, common_norm=False, \
    palette="bright", alpha=.8, linewidth=0, ax=ax2) 

plt.show()

## Example 2

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns

# %% load sample data
tips = sns.load_dataset("tips") # load dataset

# create figure with two subplots
fig, (ax1,ax2) = plt.subplots(nrows=2, sharex=True)

# scatter plot with badly chosen color palette
sns.scatterplot(data=tips, x="total_bill", y="tip", \
    hue="time", palette="crest", ax=ax1)

#scatter plot with well chosen color palette
sns.scatterplot(data=tips, x="total_bill", y="tip", \
    hue="time", palette="bright",ax=ax2)

plt.show()

