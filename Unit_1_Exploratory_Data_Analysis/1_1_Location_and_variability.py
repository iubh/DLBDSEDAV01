# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Location and variability

# %%
x = [1,2,4,6,8] # list with data values
n = len(x) # number of data values of x
my_sum = sum(x) # sum all values of x up
my_mean = my_sum/n # get mean of x

print(my_mean)
# output: 4.2


# %%
import statistics # import statistics library
x = [1,2,4,6,8] # list with data values
my_mean = statistics.mean(x) # get mean of x

print(my_mean)
# output: 4.2

# %%
x = [1,2,4,6,8] # list with data values
n = len(x) # number of data values of x
x.sort() # sort data
if n % 2 == 0: # even number of values
    median1 = x[n//2]
    median2 = x[n//2 - 1]
    median = (median1 + median2)/2
else: # odd number of values
    median = x[n//2]

print(median)
# output: 4.0

# %%
import statistics # import statistics library
x = [1,2,4,6,8] # list with data values
median = statistics.median(x) # get median of x

print(median)
# output: 4.0

# %%
from collections import Counter # module to count frequencies
x = [1,2,4,6,8,4] # list with data values
n = len(x) # number of data values of x
frequencies = Counter(x) # count frequencies of values
modes_dict = dict(frequencies) # store frequencies in dictionary  

# calculated modes  
modes = [k for k, v in modes_dict.items() if v == max(list(frequencies.values()))]  

print(modes)
# output: [4]

# %%
import statistics # import statistics library
x = [1,2,4,6,8,4] # list with data values
modes = statistics.mode(x) # get mode of x

print(modes)
# output: 4   

# %%
import statistics # import statistics library
x = [1,2,4,6,8,4] # list with data values
my_var = statistics.variance(x) # get variance of x

print(my_var)
# output: 6.566

# %%
import statistics # import statistics library
x = [1,2,4,6,8,4] # list with data values
my_std = statistics.stdev(x) # get standard deviation of x

print(my_var)
# output: 2.563  

# %% import libraries
import seaborn as sns
import pandas as pd 
import numpy as np 

# %% load data
penguins = sns.load_dataset("penguins")
flipper_length_mm = penguins["flipper_length_mm"]

# %% calculate arithmetic mean
sum = 0 
cnt_nan = 0 # helper variable to coun NaN values
for n in flipper_length_mm:
	if not np.isnan(n):
		sum+=n
	else:
		cnt_nan+=1
my_mean = sum/(len(flipper_length_mm)-cnt_nan)
print(my_mean)
# 200.91520467836258

# %% calculate median
flipper_length_mm_sorted = sorted(flipper_length_mm)
num = len(flipper_length_mm)

if num % 2 == 0:
	median1 = flipper_length_mm_sorted[num//2]	
	median2 = flipper_length_mm_sorted[num//2 - 1]
	my_median = (median1 + median2)/2	
else:
        my_median = flipper_length_mm_sorted[num//2]

print(my_median)
# 197.0

# %%calculate mode
counter = {}
for n in flipper_length_mm:
	if n in counter.keys():
		counter[str(n)]+=1
	else:
		counter[str(n)]=1
my_mode = 0
for key,val in counter.items():
	if val>my_mode:
		my_mode = float(key)

print(my_mode)
# 181.0

# %% calculate variance
my_variance = 0
for n in flipper_length_mm:
	if not np.isnan(n):
		my_variance+=(n-my_mean)**2

my_variance/=(len(flipper_length_mm)-cnt_nan)

print(my_variance)
# 197.1536 

# %% calculate standard deviation
my_std = my_variance**0.5

print(my_std)
# 14.041140568589107
=======
# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Location and variability

# %%
x = [1,2,4,6,8] # list with data values
n = len(x) # number of data values of x
my_sum = sum(x) # sum all values of x up
my_mean = my_sum/n # get mean of x

print(my_mean)
# output: 4.2


# %%
import statistics # import statistics library
x = [1,2,4,6,8] # list with data values
my_mean = statistics.mean(x) # get mean of x

print(my_mean)
# output: 4.2

# %%
x = [1,2,4,6,8] # list with data values
n = len(x) # number of data values of x
x.sort() # sort data
if n % 2 == 0: # even number of values
    median1 = x[n//2]
    median2 = x[n//2 - 1]
    median = (median1 + median2)/2
else: # odd number of values
    median = x[n//2]

print(median)
# output: 4.0

# %%
import statistics # import statistics library
x = [1,2,4,6,8] # list with data values
median = statistics.median(x) # get median of x

print(median)
# output: 4.0

# %%
from collections import Counter # module to count frequencies
x = [1,2,4,6,8,4] # list with data values
n = len(x) # number of data values of x
frequencies = Counter(x) # count frequencies of values
modes_dict = dict(frequencies) # store frequencies in dictionary  

# calculated modes  
modes = [k for k, v in modes_dict.items() if v == max(list(frequencies.values()))]  

print(modes)
# output: [4]

# %%
import statistics # import statistics library
x = [1,2,4,6,8,4] # list with data values
modes = statistics.mode(x) # get median of x

print(modes)
# output: 4   

# %%
import statistics # import statistics library
x = [1,2,4,6,8,4] # list with data values
my_var = statistics.variance(x) # get variance of x

print(my_var)
# output: 6.566

# %%
import statistics # import statistics library
x = [1,2,4,6,8,4] # list with data values
my_std = statistics.stdev(x) # get variance of x

print(my_var)
# output: 2.563  

# %% import libraries
import seaborn as sns
import pandas as pd 
import numpy as np 

# %% load data
penguins = sns.load_dataset("penguins")
flipper_length_mm = penguins["flipper_length_mm"]

# %% calculate arithmetic mean
sum = 0 
cnt_nan = 0 # helper variable to coun NaN values
for n in flipper_length_mm:
	if not np.isnan(n):
		sum+=n
	else:
		cnt_nan+=1
my_mean = sum/(len(flipper_length_mm)-cnt_nan)
print(my_mean)
# 200.91520467836258

# %% calculate median
flipper_length_mm_sorted = sorted(flipper_length_mm)
num = len(flipper_length_mm)

if num % 2 == 0:
	median1 = flipper_length_mm_sorted[num//2]	
	median2 = flipper_length_mm_sorted[num//2 - 1]
	my_median = (median1 + median2)/2	
else:
        my_median = flipper_length_mm_sorted[num//2]

print(my_median)
# 197.0

# %%calculate mode
counter = {}
for n in flipper_length_mm:
	if n in counter.keys():
		counter[str(n)]+=1
	else:
		counter[str(n)]=1
my_mode = 0
for key,val in counter.items():
	if val>my_mode:
		my_mode = float(key)

print(my_mode)
# 181.0

# %% calculate variance
my_variance = 0
for n in flipper_length_mm:
	if not np.isnan(n):
		my_variance+=(n-my_mean)**2

my_variance/=(len(flipper_length_mm)-cnt_nan)

print(my_variance)
# 197.1536 

# %% calculate standard deviation
my_std = my_variance**0.5

print(my_std)
# 14.041140568589107
