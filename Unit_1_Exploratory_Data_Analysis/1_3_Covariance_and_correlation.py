# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Covariance and Correlation

## Simple covariance example

# %% import modules
import numpy as np

# %% generate sample data
x = [3,5,8,12,15] # values for X  
y = [1,8,13,16,20] # values for Y  

# %% combine data
X = np.stack((x, y), axis=0) # form random vector  

# %% calculate the covariance matrix
np.cov(X) # calculate covariance matrix  

# result: array([[24.3 , 35.05],  
#                [35.05, 54.3 ]]) 

## Example with real data

# %% import modules
import matplotlib.pyplot as plt # import matplotlib 
import seaborn as sns # import seaborn 
import numpy as np
from scipy.stats import pearsonr

# %% load sample data set
penguins = sns.load_dataset("penguins") # load dataset  
penguins = penguins.dropna()

# %% plot the data in a simple scatter plot
plt.figure()
sns.set_theme(style="whitegrid")
sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g")
plt.show()

# %% calculate the covariance matrix
np.cov([penguins.flipper_length_mm, \
    penguins.body_mass_g]) # calculate covariance matrix  

# result:
# array([[1.96441677e+02, 9.85219165e+03],
#        [9.85219165e+03, 6.48372488e+05]])

## Person correlation

# %% import modules
from scipy.stats import pearsonr  

# %% generate sample data	  
x = [3,5,8,12,15] # values for X    
y = [1,8,13,16,20] # values for Y    

# %% calculate correlation coefficient  
corr = pearsonr(x, y)

# result: ~0.965  

## Correlogram

# %% import modules
import matplotlib.pyplot as plt # import matplotlib   
import seaborn as sns # import seaborn   

# %% load sample data
penguins = sns.load_dataset("penguins") # load dataset    

# %% create a correlogram
plt.figure() # create figure  
sns.set_theme(style="whitegrid")  
sns.heatmap(penguins.corr()) # generate heatmap containing correlation coefficients  
plt.show() # show figure  

# %%
