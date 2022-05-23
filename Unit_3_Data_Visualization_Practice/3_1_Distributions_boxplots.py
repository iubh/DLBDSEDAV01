# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Boxplots

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns

# %% load samples data
penguins = sns.load_dataset("penguins")

# %% create figure with six subplots
fig, ((ax1,ax2,ax3,ax4), (ax5,ax6,ax7,ax8)) = plt.subplots(2,4, \
                                                    figsize=(20,8))

# box plot
sns.boxplot(x="species", y="flipper_length_mm", \
    data=penguins, ax=ax1)

# violin plot
sns.violinplot(x="species", y="flipper_length_mm", \
    data=penguins, ax=ax2)

# strip chart
sns.stripplot(x="species", y="flipper_length_mm", \
    data=penguins, size=3, ax=ax3)

# swarm plot
sns.swarmplot(x="species", y="flipper_length_mm", \
    data=penguins, size=3, ax=ax4)

# box plot with strip chart
sns.boxplot(x="species", y="flipper_length_mm", \
    data=penguins, ax=ax5)
sns.stripplot(x="species", y="flipper_length_mm", \
    data=penguins, color=".3", size=3, ax=ax5)

# box plot with swarm plot
sns.boxplot(x="species", y="flipper_length_mm", \
    data=penguins, ax=ax6)
sns.swarmplot(x="species", y="flipper_length_mm", \
    data=penguins, color=".3", size=3, ax=ax6)

# violin plot with strip chart
sns.violinplot(x="species", y="flipper_length_mm", \
    data=penguins, inner=None, saturation=0.1, ax=ax7)
sns.stripplot(x="species", y="flipper_length_mm", \
    data=penguins, size=3, ax=ax7)

# violin plot with swarm plot
sns.violinplot(x="species", y="flipper_length_mm", \
    data=penguins, inner=None, saturation=0.1, ax=ax8)
sns.swarmplot(x="species", y="flipper_length_mm", \
    data=penguins, size=3, ax=ax8)

plt.show()
