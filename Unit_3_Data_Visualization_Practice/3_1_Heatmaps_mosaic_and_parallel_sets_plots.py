# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Heatmaps, Mosaic and Parellel Sets plots

## Heatmap

# %% import modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %% generate sample ata
prog_language = ['Python', 'C++', 'Java']
sex = ['Male', 'Female']

# %% create array with values
amounts = np.array([[20,11,10], [15,7,11]])

# %% create figure
fig, ax = plt.subplots()

# create heatmap with annotation
sns.heatmap(amounts, annot=True,ax=ax)

# set x- and y-axis tick labels
ax.set_xticklabels(prog_language)
ax.set_yticklabels(sex)

# show figure
plt.show()

## Mosaic plot

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic

# %% load tips dataset
tips = sns.load_dataset("tips")

# %%mosaic plot of sex, smoker and time
mosaic(tips, ['sex','smoker','time'])

plt.show()


## Parallel sets

# %% import modules
import plotly.express as px
import seaborn as sns

# %% load titanic dataset
titanic = sns.load_dataset("titanic")

# %% parallel sets plot
fig = px.parallel_categories(titanic, \
    dimensions=['sex', 'class', 'alive'], \
    color="survived", \
    labels={'sex':'Passenger sex', \
        'class':'Class of passenger', \
        'alive':'Survived'})

fig.show()
