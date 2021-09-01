# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Boxplots

# %% import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# %% create distributions
data_1 = np.random.normal(50, 40, 200) 
data_2 = np.random.normal(70, 10, 200) 
data_3 = np.random.normal(120, 20, 200) 
data_4 = np.random.normal(60, 50, 200) 
data_5 = np.random.normal(70, 20, 200)
data = [data_1, data_2, data_3, data_4, data_5] 

# collect data in DataFrame
df = pd.DataFrame({
    'data_1': data_1,
    'data_2': data_2,
    'data_3': data_3,
    'data_4': data_4,
    'data_5': data_5
})
data_df = df.melt(var_name='dataset',value_name='values')

# %% create figure
fig = plt.figure(figsize=(14,8))

# Matplotlib boxplot
ax1 = fig.add_subplot(221)
bp = ax1.boxplot(data)

# Matplotlib violine plot
ax2 = fig.add_subplot(222)
bp = ax2.violinplot(data) 

# Seaborn boxplot
ax3 = fig.add_subplot(223)
sns.boxplot(x="dataset", y="values", data=data_df, ax=ax3)

# Seaborn violine plot
ax4 = fig.add_subplot(224)
sns.violinplot(x="dataset", y="values", data=data_df, ax=ax4)

plt.show()
