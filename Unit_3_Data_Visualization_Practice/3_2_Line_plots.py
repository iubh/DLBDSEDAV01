# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Associations and relations

## Line plots

# %% import modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %% load flights dataset
flights = sns.load_dataset("flights")

# %% get data for January
jan_flights = flights.query("month == 'Jan'")

# %% create figure with four subplots
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(20,20))

# scatter plot
ax1.scatter(jan_flights["year"], \
    jan_flights["passengers"])

# connected scatter plot
ax2.plot(jan_flights["year"], \
    jan_flights["passengers"], \
    linestyle = '-', marker='o')

# connected scatter plot with dashed line
ax3.plot(jan_flights["year"], \
    jan_flights["passengers"], \
    linestyle = 'dotted', marker='o')

# line graph
ax4.plot(jan_flights["year"], \
    jan_flights["passengers"])

plt.show()

## Filled line plots

# %% import module
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %% load flights dataset
flights = sns.load_dataset("flights")

# %% get data for January
jan_flights = flights.query("month == 'Jan'")

# %% create figure with four subplots
fig, ax = plt.subplots(figsize=(10,6))

# plot the line
ax.plot(jan_flights["year"], \
    jan_flights["passengers"])

# fill the area under the line
ax.fill_between(jan_flights["year"], \
    jan_flights["passengers"], alpha=0.2)

ax.set_xlabel("Year")
ax.set_ylabel("Number of passengers")

plt.show()

## Multiple lines

# import modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %% load flights dataset
flights = sns.load_dataset("flights")

# %% get data for three different months
jan_flights = flights.query("month == 'Jan'")
apr_flights = flights.query("month == 'Apr'")
jul_flights = flights.query("month == 'Jul'")

# %% create figure with four subplots
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, \
                                figsize=(20,20))
# scatter plot
ax1.scatter(jan_flights["year"], \
    jan_flights["passengers"], label="January")
ax1.scatter(apr_flights["year"], \
    apr_flights["passengers"], label="April")
ax1.scatter(jul_flights["year"], \
    jul_flights["passengers"], label="July")

# connected scatter plot
ax2.plot(jan_flights["year"], \
    jan_flights["passengers"], \
    linestyle = '-', marker='o', \
    label="January")
ax2.plot(apr_flights["year"], \
    jan_flights["passengers"], \
    linestyle = '-', marker='o', \
    label="January")
ax2.plot(jul_flights["year"], \
    jan_flights["passengers"], \
    linestyle = '-', marker='o', \
    label="January")

# graph with legend
ax3.plot(jan_flights["year"], \
    jan_flights["passengers"], label="January")
ax3.plot(apr_flights["year"], \
    apr_flights["passengers"], label="April")
ax3.plot(jul_flights["year"], \
    jul_flights["passengers"], label="July")

# line graph with direct annotation
# plot lines
ax4.plot(jan_flights["year"], \
    jan_flights["passengers"], label="January")
ax4.plot(apr_flights["year"], \
    apr_flights["passengers"], label="April")
ax4.plot(jul_flights["year"], \
    jul_flights["passengers"], label="July")

# annotate line graphs with particular month information
ax4.annotate(xy=(jan_flights["year"].iloc[-1], \
             jan_flights["passengers"].iloc[-1]), xytext=(5,0), \
             textcoords='offset points', s='January', \
             va='center', color='blue')
ax4.annotate(xy=(apr_flights["year"].iloc[-1], \
             apr_flights["passengers"].iloc[-1]), xytext=(5,0), \
             textcoords='offset points', s='April', \
             va='center', color='orange')
ax4.annotate(xy=(jul_flights["year"].iloc[-1],
             jul_flights["passengers"].iloc[-1]), xytext=(5,0), \
             textcoords='offset points', s='July', \
             va='center', color='green')

# turn on legends and set axes labels
ax1.legend()
ax2.legend()
ax3.legend()
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of passengers")
ax2.set_xlabel("Year")
ax2.set_ylabel("Number of passengers")
ax3.set_xlabel("Year")
ax3.set_ylabel("Number of passengers")
ax4.set_xlabel("Year")
ax4.set_ylabel("Number of passengers")

plt.show()

## Many lines per plot

# %% import modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %% load flights dataset
flights = sns.load_dataset("flights")

# %% create figure with two subplots
fig, (ax1,ax2) = plt.subplots(1,2, figsize=(14,6))

# line plot with different colors
sns.lineplot(data=flights, x="year", y="passengers", \
    hue="month",ax=ax1)

# line plot with different colors and line styles
sns.lineplot(data=flights, x="year", y="passengers", \
    hue="month", style="month",ax=ax2)

plt.show()
