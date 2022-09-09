#!/usr/bin/env python
# coding: utf-8

# ## Crypto Arbitrage
# 
# In this Challenge, you'll take on the role of an analyst at a high-tech investment firm. The vice president (VP) of your department is considering arbitrage opportunities in Bitcoin and other cryptocurrencies. As Bitcoin trades on markets across the globe, can you capitalize on simultaneous price dislocations in those markets by using the powers of Pandas?
# 
# For this assignment, you’ll sort through historical trade data for Bitcoin on two exchanges: Bitstamp and Coinbase. Your task is to apply the three phases of financial analysis to determine if any arbitrage opportunities exist for Bitcoin.
# 
# This aspect of the Challenge will consist of 3 phases.
# 
# 1. Collect the data.
# 
# 2. Prepare the data.
# 
# 3. Analyze the data. 
# 
# 

# ###  Import the required libraries and dependencies.

# In[ ]:


import pandas as pd
from pathlib import Path
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Collect the Data
# 
# To collect the data that you’ll need, complete the following steps:
# 
# Instructions. 
# 
# 1. Using the Pandas `read_csv` function and the `Path` module, import the data from `bitstamp.csv` file, and create a DataFrame called `bitstamp`. Set the DatetimeIndex as the Timestamp column, and be sure to parse and format the dates.
# 
# 2. Use the `head` (and/or the `tail`) function to confirm that Pandas properly imported the data.
# 
# 3. Repeat Steps 1 and 2 for `coinbase.csv` file.

# ### Step 1: Using the Pandas `read_csv` function and the `Path` module, import the data from `bitstamp.csv` file, and create a DataFrame called `bitstamp`. Set the DatetimeIndex as the Timestamp column, and be sure to parse and format the dates.

# In[ ]:


# Read in the CSV file called "bitstamp.csv" using the Path module. 
# The CSV file is located in the Resources folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters
bitstamp = pd.read_csv(
    Path('./Resources/bitstamp.csv'), 
    index_col="Timestamp", 
    parse_dates=True, 
    infer_datetime_format=True
)


# ### Step 2: Use the `head` (and/or the `tail`) function to confirm that Pandas properly imported the data.

# In[ ]:


# Use the head (and/or tail) function to confirm that the data was imported properly.
print("\n")
print("bitstamp DataFrame Head:")
display(bitstamp.head())
print("\n")

print("bitstamp Tail:")
display(bitstamp.tail())
print("\n")


# ### Step 3: Repeat Steps 1 and 2 for `coinbase.csv` file.

# In[ ]:


# Read in the CSV file called "coinbase.csv" using the Path module. 
# The CSV file is located in the Resources folder.
# Set the index to the column "Timestamp"
# Set the parse_dates and infer_datetime_format parameters
coinbase = pd.read_csv(
    Path('./Resources/coinbase.csv'), 
    index_col="Timestamp", 
    parse_dates=True, 
    infer_datetime_format=True
)


# In[ ]:


# Use the head (and/or tail) function to confirm that the data was imported properly.
print("\n")
print("coinbase Head:")
display(coinbase.head())
print("\n")

print("coinbase Tail:")
display(coinbase.tail())
print("\n")


# ## Prepare the Data
# 
# To prepare and clean your data for analysis, complete the following steps:
# 
# 1. For the bitstamp DataFrame, replace or drop all `NaN`, or missing, values in the DataFrame.
# 
# 2. Use the `str.replace` function to remove the dollar signs ($) from the values in the Close column.
# 
# 3. Convert the data type of the Close column to a `float`.
# 
# 4. Review the data for duplicated values, and drop them if necessary.
# 
# 5. Repeat Steps 1–4 for the coinbase DataFrame.

# ### Step 1: For the bitstamp DataFrame, replace or drop all `NaN`, or missing, values in the DataFrame.

# In[ ]:


# For the bitstamp DataFrame, replace or drop all NaNs or missing values in the DataFrame

# First get the total number of row entries in the DataFrame (to determine how many Nan rows there are relative to the total number of rows)
print("\n")
print("Total # of row entries in the bitstamp DataFrame = ", len(bitstamp), "\n")

# Print the total number of NaN's in the DataFrame
print("Sum of of number of Nan entries in the bitstamp DataFrame:")
print(bitstamp.isnull().sum())
print("\n")

# Drop all NaN's from DataFrame (Note, only 0.3% of the row entries are Nan, so OK to drop)
bitstamp = bitstamp.dropna()
print("Sum of of number of Nan entries in the bitstamp DataFrame (AFTER DROP NAN):")
print(bitstamp.isnull().sum())
print("\n")


# ### Step 2: Use the `str.replace` function to remove the dollar signs ($) from the values in the Close column.

# In[ ]:


# Use the str.replace function to remove the dollar sign, $

# Print data types head to confirm the $ is part of the values under the Close column
print("\n")
print("bitstamp (before removal of $)")
display(bitstamp.head())
print("\n")

# Remvoe dollar sign from the Close column
bitstamp.loc[:, 'Close'] = bitstamp.loc[:, 'Close'].str.replace("$", "")

# Print data types head to confirm the $ no longer part of the values under the Close column
print("bitstamp (after removal of $)")
display(bitstamp.head())
print("\n")


# ### Step 3: Convert the data type of the Close column to a `float`.

# In[ ]:


# Convert the Close data type to a float

# First, print the data types of all the columns to determine the type
# (Note, removing the $ character from previous step does not change the type of the field - remanes string/boject)
print("\n")
print("Data types of DataFrame columns (before float converstion):")
print(bitstamp.dtypes)
print("\n")

# Convert the data type of Close column to float
bitstamp.loc[:, 'Close'] = bitstamp.loc[:, 'Close'].astype("float")

# Confirm converted to float by printing data types again
print("Data types of DataFrame columns (after float converstion):")
print(bitstamp.dtypes)
print("\n")


# ### Step 4: Review the data for duplicated values, and drop them if necessary.

# In[ ]:


# Review the data for duplicate values, and drop them if necessary

# Compute the number of duplicates in DataFrame
num_duplicates = bitstamp.duplicated().sum()
# Display number of duplicates
print("\n")
print("Number of duplicates in bitstamp DataFrame = ", num_duplicates)

# if number of duplicates is > 0, drop them
if (num_duplicates > 0):
    bitstamp = bitstamp.drop_duplicates()
    print("Duplicates dropped, Number of duplicates in bitstamp DataFrame now = ", bitstamp.duplicated().sum())
    
print("\n")


# ### Step 5: Repeat Steps 1–4 for the coinbase DataFrame.

# In[ ]:


# Repeat Steps 1–4 for the coinbase DataFrame

# ------
# Step 1
# ------

# For the coinbase DataFrame, replace or drop all NaNs or missing values in the DataFrame

# First get the total number of row entries in the DataFrame (to determine how many Nan rows there are relative to the total number of rows)
print("\n")
print("Total # of row entries in the coinbase DataFrame = ", len(coinbase), "\n")

# Print the total number of NaN's in the DataFrame
print("Sum of of number of Nan entries in the coinbase DataFrame:")
print(coinbase.isnull().sum())
print("\n")

# Drop all NaN's from DataFrame (Note, only 0.3% of the row entries are Nan, so OK to drop)
coinbase = coinbase.dropna()
print("Sum of of number of Nan entries in the coinbase DataFrame (AFTER DROP NAN):")
print(coinbase.isnull().sum())
print("\n")


# ------
# Step 2
# ------

# Use the str.replace function to remove the dollar sign, $

# Print data types head to confirm the $ is part of the values under the Close column
print("coinbase (before removal of $)")
display(coinbase.head())
print("\n")

# Remvoe dollar sign from the Close column
coinbase.loc[:, 'Close'] = coinbase.loc[:, 'Close'].str.replace("$", "")

# Print data types head to confirm the $ no longer part of the values under the Close column
print("coinbase (after removal of $)")
display(coinbase.head())
print("\n")


# ------
# Step 3
# ------

# Convert the Close data type to a float

# First, print the data types of all the columns to determine the type
# (Note, removing the $ character from previous step does not change the type of the field - remanes string/boject)
print("Data types of columns (before float converstion):")
print(coinbase.dtypes)
print("\n")

# Convert the data type of Close column to float
coinbase.loc[:, 'Close'] = coinbase.loc[:, 'Close'].astype("float")

# Confirm converted to float by printing data types again
print("Data types of columns (after float converstion):")
print(coinbase.dtypes)
print("\n")


# ------
# Step 4
# ------

# Review the data for duplicate values, and drop them if necessary

# Compute the number of duplicates in DataFrame
num_duplicates = coinbase.duplicated().sum()
# Display number of duplicates
print("Number of duplicates in coinbase = ", num_duplicates)

# if number of duplicates is > 0, drop them
if (num_duplicates > 0):
    coinbase = coinbase.drop_duplicates()
    print("Duplicates dropped, Number of duplicates in coinbase now = ", coinbase.duplicated().sum())
    
print("\n")


# ## Analyze the Data
# 
# Your analysis consists of the following tasks: 
# 
# 1. Choose the columns of data on which to focus your analysis.
# 
# 2. Get the summary statistics and plot the data.
# 
# 3. Focus your analysis on specific dates.
# 
# 4. Calculate the arbitrage profits.

# ### Step 1: Choose columns of data on which to focus your analysis.
# 
# Select the data you want to analyze. Use `loc` or `iloc` to select the following columns of data for both the bitstamp and coinbase DataFrames:
# 
# * Timestamp (index)
# 
# * Close
# 

# In[ ]:


# Use loc or iloc to select `Timestamp (the index)` and `Close` from bitstamp DataFrame
bitstamp_sliced = bitstamp.loc[:, 'Close']

# Review the first five rows of the DataFrame
# Print the head of the full DataFrame followed by sliced DataFrame (to confirm selected right column)
print("\n")
print("bitstamp Head:")
display(bitstamp.head())
print("\n")
print("bitstamp Sliced Head:")
display(bitstamp_sliced.head())
print("\n")


# In[ ]:


# Use loc or iloc to select `Timestamp (the index)` and `Close` from coinbase DataFrame
coinbase_sliced = coinbase.loc[:, 'Close']

# Review the first five rows of the DataFrame
# Print the head of the full DataFrame followed by sliced DataFrame (to confirm selected right column)
print("\n")
print("coinbase Head:")
display(coinbase.head())
print("\n")
print("coinbase sliced Head:")
display(coinbase_sliced.head())
print("\n")


# ### Step 2: Get summary statistics and plot the data.
# 
# Sort through the time series data associated with the bitstamp and coinbase DataFrames to identify potential arbitrage opportunities. To do so, complete the following steps:
# 
# 1. Generate the summary statistics for each DataFrame by using the `describe` function.
# 
# 2. For each DataFrame, create a line plot for the full period of time in the dataset. Be sure to tailor the figure size, title, and color to each visualization.
# 
# 3. In one plot, overlay the visualizations that you created in Step 2 for bitstamp and coinbase. Be sure to adjust the legend and title for this new visualization.
# 
# 4. Using the `loc` and `plot` functions, plot the price action of the assets on each exchange for different dates and times. Your goal is to evaluate how the spread between the two exchanges changed across the time period that the datasets define. Did the degree of spread change as time progressed?

# In[ ]:


# Generate the summary statistics for the bitstamp DataFrame
print("\n")
print("bistamp summary statistics:")
display(bitstamp_sliced.describe())
print("\n")


# In[ ]:


# Generate the summary statistics for the coinbase DataFrame
print("\n")
print("coinbase summary statistics:")
display(coinbase_sliced.describe())
print("\n")


# In[ ]:


# Create a line plot for the bitstamp DataFrame for the full length of time in the dataset 
# Be sure that the figure size, title, and color are tailored to each visualization
bitstamp_sliced.plot(
    figsize = (10,8),
    title = "Bitstamp Closing Prices",
    color = "blue")


# In[ ]:


# Create a line plot for the coinbase DataFrame for the full length of time in the dataset 
# Be sure that the figure size, title, and color are tailored to each visualization
coinbase_sliced.plot(
    figsize = (10,8),
    title = "Coinbase Closing Prices",
    color = "red")


# In[ ]:


# Overlay the visualizations for the bitstamp and coinbase DataFrames in one plot
# The plot should visualize the prices over the full lenth of the dataset
# Be sure to include the parameters: legend, figure size, title, and color and label
bitstamp_sliced.plot(
    legend = True,
    figsize = (10,8),
    title = "Bitstamp v. Coinbase Closing Prices",
    color = "blue",
    label = "Bitstamp")
coinbase_sliced.plot(
    legend = True,
    figsize = (10,8),
    color = "red",
    label = "Coibbase")


# In[ ]:


# Using the loc and plot functions, create an overlay plot that visualizes 
# the price action of both DataFrames for a one month period early in the dataset
# Be sure to include the parameters: legend, figure size, title, and color and label
bitstamp_sliced.loc['2018-01-01' : '2018-01-31'].plot(
    legend = True,
    figsize = (10,8),
    title = "Bitstamp v. Coinbase Closing Prices (January 2018)",
    color = "blue",
    label = "Bitstamp")
coinbase_sliced.loc['2018-01-01' : '2018-01-31'].plot(
    legend = True,
    figsize = (10,8),
    color = "red",
    label = "Coibbase")


# In[ ]:


# Using the loc and plot functions, create an overlay plot that visualizes 
# the price action of both DataFrames for a one month period later in the dataset
# Be sure to include the parameters: legend, figure size, title, and color and label 
bitstamp_sliced.loc['2018-03-01' : '2018-03-31'].plot(
    legend = True,
    figsize = (10,8),
    title = "Bitstamp v. Coinbase Closing Prices (March 2018)",
    color = "blue",
    label = "Bitstamp")
coinbase_sliced.loc['2018-03-01' : '2018-03-31'].plot(
    legend = True,
    figsize = (10,8),
    color = "red",
    label = "Coibbase")


# **Question** Based on the visualizations of the different time periods, has the degree of spread change as time progressed?
# 
# **Answer** Yes, the earlier time periods have a larger spread.

# ### Step 3: Focus Your Analysis on Specific Dates
# 
# Focus your analysis on specific dates by completing the following steps:
# 
# 1. Select three dates to evaluate for arbitrage profitability. Choose one date that’s early in the dataset, one from the middle of the dataset, and one from the later part of the time period.
# 
# 2. For each of the three dates, generate the summary statistics and then create a box plot. This big-picture view is meant to help you gain a better understanding of the data before you perform your arbitrage calculations. As you compare the data, what conclusions can you draw?

# In[ ]:


# Create python variables to hold the early, middle, and late dates (change in a single place to try out different dates)
sel_early_date = '2018-01-16'
sel_middle_date = '2018-02-24'
sel_late_date = '2018-03-26'


# In[ ]:


# Create an overlay plot that visualizes the two dataframes over a period of one day early in the dataset. 
# Be sure that the plots include the parameters `legend`, `figsize`, `title`, `color` and `label` 
bitstamp_sliced.loc[sel_early_date].plot(
    legend = True,
    figsize = (10,8),
    title = "Bitstamp v. Coinbase Closing Prices (" + sel_early_date + ")",
    color = "blue",
    label = "Bitstamp")
coinbase_sliced.loc[sel_early_date].plot(
    legend = True,
    figsize = (10,8),
    color = "red",
    label = "Coibbase")


# In[ ]:


# Using the early date that you have selected, calculate the arbitrage spread 
# by subtracting the bitstamp lower closing prices from the coinbase higher closing prices
arbitrage_spread_early = coinbase_sliced.loc[sel_early_date] - bitstamp_sliced.loc[sel_early_date]

# Generate summary statistics for the early DataFrame
print("\n")
print("Arbitrage " + sel_early_date + " summary statistics:")
display(arbitrage_spread_early.describe())
print("\n")


# In[ ]:


# Visualize the arbitrage spread from early in the dataset in a box plot
arbitrage_spread_early.plot(
    title = "Arbitrage Spread - " + sel_early_date + "",
    kind = "box")


# In[ ]:


# Create an overlay plot that visualizes the two dataframes over a period of one day from the middle of the dataset. 
# Be sure that the plots include the parameters `legend`, `figsize`, `title`, `color` and `label` 
bitstamp_sliced.loc[sel_middle_date].plot(
    legend = True,
    figsize = (10,8),
    title = "Bitstamp v. Coinbase Closing Prices (" + sel_middle_date + ")",
    color = "blue",
    label = "Bitstamp")
coinbase_sliced.loc[sel_middle_date].plot(
    legend = True,
    figsize = (10,8),
    color = "red",
    label = "Coibbase")


# In[ ]:


# Using the date in the middle that you have selected, calculate the arbitrage spread 
# by subtracting the bitstamp lower closing prices from the coinbase higher closing prices
arbitrage_spread_middle = coinbase_sliced.loc[sel_middle_date] - bitstamp_sliced.loc[sel_middle_date]

# Generate summary statistics for the middle DataFrame
print("\n")
print("Arbitrage " + sel_middle_date + " summary statistics:")
display(arbitrage_spread_middle.describe())
print("\n")


# In[ ]:


# Visualize the arbitrage spread from the middle of the dataset in a box plot
arbitrage_spread_middle.plot(
    title = "Arbitrage Spread - " + sel_middle_date + "",
    kind = "box")


# In[ ]:


# Create an overlay plot that visualizes the two dataframes over a period of one day from late in the dataset. 
# Be sure that the plots include the parameters `legend`, `figsize`, `title`, `color` and `label` 
bitstamp_sliced.loc[sel_late_date].plot(
    legend = True,
    figsize = (10,8),
    title = "Bitstamp v. Coinbase Closing Prices (" + sel_late_date + ")",
    color = "blue",
    label = "Bitstamp")
coinbase_sliced.loc[sel_late_date].plot(
    legend = True,
    figsize = (10,8),
    color = "red",
    label = "Coibbase")


# In[ ]:


# Using the date from the late that you have selected, calculate the arbitrage spread 
# by subtracting the bitstamp lower closing prices from the coinbase higher closing prices
arbitrage_spread_late = coinbase_sliced.loc[sel_late_date] - bitstamp_sliced.loc[sel_late_date]

# Generate summary statistics for the high DataFrame
print("\n")
print("Arbitrage " + sel_late_date + " summary statistics:")
display(arbitrage_spread_late.describe())
print("\n")


# In[ ]:


# Visualize the arbitrage spread from late in the dataset in a box plot
arbitrage_spread_late.plot(
    title = "Arbitrage Spread - " + sel_late_date + "",
    kind = "box")


# ### Step 4: Calculate the Arbitrage Profits
# 
# Calculate the potential profits for each date that you selected in the previous section. Your goal is to determine whether arbitrage opportunities still exist in the Bitcoin market. Complete the following steps:
# 
# 1. For each of the three dates, measure the arbitrage spread between the two exchanges by subtracting the lower-priced exchange from the higher-priced one. Then use a conditional statement to generate the summary statistics for each arbitrage_spread DataFrame, where the spread is greater than zero.
# 
# 2. For each of the three dates, calculate the spread returns. To do so, divide the instances that have a positive arbitrage spread (that is, a spread greater than zero) by the price of Bitcoin from the exchange you’re buying on (that is, the lower-priced exchange). Review the resulting DataFrame.
# 
# 3. For each of the three dates, narrow down your trading opportunities even further. To do so, determine the number of times your trades with positive returns exceed the 1% minimum threshold that you need to cover your costs.
# 
# 4. Generate the summary statistics of your spread returns that are greater than 1%. How do the average returns compare among the three dates?
# 
# 5. For each of the three dates, calculate the potential profit, in dollars, per trade. To do so, multiply the spread returns that were greater than 1% by the cost of what was purchased. Make sure to drop any missing values from the resulting DataFrame.
# 
# 6. Generate the summary statistics, and plot the results for each of the three DataFrames.
# 
# 7. Calculate the potential arbitrage profits that you can make on each day. To do so, sum the elements in the profit_per_trade DataFrame.
# 
# 8. Using the `cumsum` function, plot the cumulative sum of each of the three DataFrames. Can you identify any patterns or trends in the profits across the three time periods?
# 
# (NOTE: The starter code displays only one date. You'll want to do this analysis for two additional dates).

# #### 1. For each of the three dates, measure the arbitrage spread between the two exchanges by subtracting the lower-priced exchange from the higher-priced one. Then use a conditional statement to generate the summary statistics for each arbitrage_spread DataFrame, where the spread is greater than zero.
# 
# *NOTE*: For illustration, only one of the three dates is shown in the starter code below.

# In[ ]:


# For the date early in the dataset, measure the arbitrage spread between the two exchanges
# by subtracting the lower-priced exchange from the higher-priced one
arbitrage_spread_early = coinbase_sliced.loc[sel_early_date] - bitstamp_sliced.loc[sel_early_date]

# Use a conditional statement to generate the summary statistics for each arbitrage_spread DataFrame
arbitrage_spread_early = arbitrage_spread_early[arbitrage_spread_early > 0.0]

print("\n")
print("Arbitrage Spread > 0.0 " + sel_early_date + " summary statistics:")
display(arbitrage_spread_early.describe())
print("\n")



# For the date middle in the dataset, measure the arbitrage spread between the two exchanges
# by subtracting the lower-priced exchange from the higher-priced one
arbitrage_spread_middle = coinbase_sliced.loc[sel_middle_date] - bitstamp_sliced.loc[sel_middle_date]

# Use a conditional statement to generate the summary statistics for each arbitrage_spread DataFrame
arbitrage_spread_middle = arbitrage_spread_middle[arbitrage_spread_middle > 0.0]

print("Arbitrage Spread > 0.0 " + sel_middle_date + " summary statistics:")
display(arbitrage_spread_middle.describe())
print("\n")



# For the date late in the dataset, measure the arbitrage spread between the two exchanges
# by subtracting the lower-priced exchange from the higher-priced one
arbitrage_spread_late = coinbase_sliced.loc[sel_late_date] - bitstamp_sliced.loc[sel_late_date]

# Use a conditional statement to generate the summary statistics for each arbitrage_spread DataFrame
arbitrage_spread_late = arbitrage_spread_late[arbitrage_spread_late > 0.0]

print("Arbitrage Spread > 0.0 " + sel_late_date + " summary statistics:")
display(arbitrage_spread_late.describe())
print("\n")


# #### 2. For each of the three dates, calculate the spread returns. To do so, divide the instances that have a positive arbitrage spread (that is, a spread greater than zero) by the price of Bitcoin from the exchange you’re buying on (that is, the lower-priced exchange). Review the resulting DataFrame.

# In[ ]:


# For the date early in the dataset, calculate the spread returns by dividing the instances when the arbitrage spread is positive (> 0) 
# by the price of Bitcoin from the exchange you are buying on (the lower-priced exchange).
spread_return_early= arbitrage_spread_early / bitstamp_sliced.loc[sel_early_date]

# Review the spread return DataFrame
print("\n")
print("Spread Return " + sel_early_date + " Head:")
display(spread_return_early.head())
print("\n")



# For the date middle in the dataset, calculate the spread returns by dividing the instances when the arbitrage spread is positive (> 0) 
# by the price of Bitcoin from the exchange you are buying on (the lower-priced exchange).
spread_return_middle= arbitrage_spread_middle / bitstamp_sliced.loc[sel_middle_date]

# Review the spread return DataFrame
print("Spread Return " + sel_middle_date + " Head:")
display(spread_return_middle.head())
print("\n")



# For the date late in the dataset, calculate the spread returns by dividing the instances when the arbitrage spread is positive (> 0) 
# by the price of Bitcoin from the exchange you are buying on (the lower-priced exchange).
spread_return_late= arbitrage_spread_late / bitstamp_sliced.loc[sel_late_date]

# Review the spread return DataFrame
print("Spread Return " + sel_late_date + " Head:")
display(spread_return_late.head())
print("\n")


# #### 3. For each of the three dates, narrow down your trading opportunities even further. To do so, determine the number of times your trades with positive returns exceed the 1% minimum threshold that you need to cover your costs.

# In[ ]:


# For the date early in the dataset, determine the number of times your trades with positive returns 
# exceed the 1% minimum threshold (.01) that you need to cover your costs
profitable_trades_early = spread_return_early[spread_return_early > 0.01]

# Review the first five profitable trades
print("\n")
print("Profitable Trades " + sel_early_date + " Head:")
display(profitable_trades_early.head())
print("\n")



# For the date middle in the dataset, determine the number of times your trades with positive returns 
# exceed the 1% minimum threshold (.01) that you need to cover your costs
profitable_trades_middle = spread_return_middle[spread_return_middle > 0.01]

# Review the first five profitable trades
print("Profitable Trades " + sel_middle_date + " Head:")
display(profitable_trades_middle.head())
print("\n")



# For the date late in the dataset, determine the number of times your trades with positive returns 
# exceed the 1% minimum threshold (.01) that you need to cover your costs
profitable_trades_late = spread_return_late[spread_return_late > 0.01]

# Review the first five profitable trades
print("Profitable Trades " + sel_late_date + " Head:")
display(profitable_trades_late.head())
print("\n")


# #### 4. Generate the summary statistics of your spread returns that are greater than 1%. How do the average returns compare among the three dates?

# In[ ]:


# For the date early in the dataset, generate the summary statistics for the profitable trades
# or you trades where the spread returns are are greater than 1%
print("\n")
print("Profitable Trades > 1% " + sel_early_date + " summary statistics:")
display(profitable_trades_early.describe())
print("\n")



# For the date middle in the dataset, generate the summary statistics for the profitable trades
# or you trades where the spread returns are are greater than 1%
print("Profitable Trades > 1% " + sel_middle_date + " summary statistics:")
display(profitable_trades_middle.describe())
print("\n")



# or you trades where the spread returns are are greater than 1%
print("Profitable Trades > 1% " + sel_late_date + " summary statistics:")
display(profitable_trades_late.describe())
print("\n")


# #### 5. For each of the three dates, calculate the potential profit, in dollars, per trade. To do so, multiply the spread returns that were greater than 1% by the cost of what was purchased. Make sure to drop any missing values from the resulting DataFrame.

# In[ ]:


# For the date early in the dataset, calculate the potential profit per trade in dollars 
# Multiply the profitable trades by the cost of the Bitcoin that was purchased
profit_early = profitable_trades_early * bitstamp_sliced.loc[sel_early_date]

# Drop any missing values from the profit DataFrame
profit_per_trade_early = profit_early.dropna()

# View the early profit DataFrame
print("\n")
print("Profit Per Trade " + sel_early_date + ":")
display(profit_per_trade_early)
print("\n")



# For the date middle in the dataset, calculate the potential profit per trade in dollars 
# Multiply the profitable trades by the cost of the Bitcoin that was purchased
profit_middle = profitable_trades_middle * bitstamp_sliced.loc[sel_middle_date]

# Drop any missing values from the profit DataFrame
profit_per_trade_middle = profit_middle.dropna()

# View the middle profit DataFrame
print("Profit Per Trade " + sel_middle_date + ":")
display(profit_per_trade_middle)
print("\n")



# For the date late in the dataset, calculate the potential profit per trade in dollars 
# Multiply the profitable trades by the cost of the Bitcoin that was purchased
profit_late = profitable_trades_late * bitstamp_sliced.loc[sel_late_date]

# Drop any missing values from the profit DataFrame
profit_per_trade_late = profit_late.dropna()

# View the late profit DataFrame
print("Profit Per Trade " + sel_late_date + ":")
display(profit_per_trade_late)
print("\n")


# #### 6. Generate the summary statistics, and plot the results for each of the three DataFrames.

# In[ ]:


# Generate the summary statistics for the early profit per trade DataFrame
print("\n")
print("Profits Per Trade - " + sel_early_date + " summary statistics:")
display(profit_per_trade_early.describe())
print("\n")



# Generate the summary statistics for the middle profit per trade DataFrame
print("Profits Per Trade - " + sel_middle_date + " summary statistics:")
display(profit_per_trade_middle.describe())
print("\n")



# Generate the summary statistics for the late profit per trade DataFrame
print("Profits Per Trade - " + sel_late_date + " summary statistics:")
display(profit_per_trade_late.describe())
print("\n")


# In[ ]:


# Plot the results for the early profit per trade DataFrame
if (len(profit_per_trade_early) > 0):
    profit_per_trade_early.plot(
        figsize = (10,8),
        title = "Profit Per Trade - " + sel_early_date + "",
        color = "magenta")
else:
    print("\n")
    print("Ther are 0 profits per trade for ", sel_early_date)
    print("\n")


# In[ ]:


# Plot the results for the middle profit per trade DataFrame
if (len(profit_per_trade_middle) > 0):
    profit_per_trade_middle.plot(
        figsize = (10,8),
        title = "Profit Per Trade - " + sel_middle_date + "",
        color = "magenta")
else:
    print("\n")
    print("Ther are 0 profits per trade for ", sel_middle_date)
    print("\n")


# In[ ]:


if (len(profit_per_trade_late) > 0):
    profit_per_trade_late.plot(
        figsize = (10,8),
        title = "Profit Per Trade - " + sel_late_date + "",
        color = "magenta")
else:
    print("\n")
    print("Ther are 0 profits per trade for ", sel_late_date)
    print("\n")


# #### 7. Calculate the potential arbitrage profits that you can make on each day. To do so, sum the elements in the profit_per_trade DataFrame.

# In[ ]:


# Calculate the sum of the potential profits for the early profit per trade DataFrame
sum_profit_early = profit_per_trade_early.sum()

print("\n")
print("Sum of Profits, " + sel_early_date + " = ", sum_profit_early)
print("\n")



# Calculate the sum of the potential profits for the middle profit per trade DataFrame
sum_profit_middle = profit_per_trade_middle.sum()

print("Sum of Profits, " + sel_middle_date + " = ", sum_profit_middle)
print("\n")



# Calculate the sum of the potential profits for the late profit per trade DataFrame
sum_profit_late = profit_per_trade_late.sum()

print("Sum of Profits, " + sel_late_date + " = ", sum_profit_late)
print("\n")


# #### 8. Using the `cumsum` function, plot the cumulative sum of each of the three DataFrames. Can you identify any patterns or trends in the profits across the three time periods?

# In[ ]:


# Use the cumsum function to calculate the cumulative profits over time for the early profit per trade DataFrame
cumulative_profit_early = profit_per_trade_early.cumsum()



# Use the cumsum function to calculate the cumulative profits over time for the middle profit per trade DataFrame
cumulative_profit_middle = profit_per_trade_middle.cumsum()



# Use the cumsum function to calculate the cumulative profits over time for the late profit per trade DataFrame
cumulative_profit_late = profit_per_trade_late.cumsum()


# In[ ]:


# Plot the cumulative sum of profits for the early profit per trade DataFrame
if (len(cumulative_profit_early) > 0):
    cumulative_profit_early.plot(
        figsize = (10,8),
        title = "Cumulative Profits - " + sel_early_date + "",
        color = "magenta")
else:
    print("\n")
    print("Ther are 0 cumulative profits for ", sel_early_date)
    print("\n")


# In[ ]:


# Plot the cumulative sum of profits for the middle profit per trade DataFrame
if (len(cumulative_profit_middle) > 0):
    cumulative_profit_middle.plot(
        figsize = (10,8),
        title = "Cumulative Profits - " + sel_middle_date + "",
        color = "magenta")
else:
    print("\n")
    print("Ther are 0 cumulative profits for ", sel_middle_date)
    print("\n")


# In[ ]:


# Plot the cumulative sum of profits for the late profit per trade DataFrame
if (len(cumulative_profit_late) > 0):
    cumulative_profit_late.plot(
        figsize = (10,8),
        title = "Cumulative Profits - " + sel_late_date + "",
        color = "magenta")
else:
    print("\n")
    print("Ther are 0 cumulative profits for ", sel_late_date)
    print("\n")


# **Question:** After reviewing the profit information across each date from the different time periods, can you identify any patterns or trends?
#     
# **Answer:** 
# 
# Observation 1: Early date selection had a lot more opportunities to make a profit - and got less in later dates.  
# 
# Observation 2: When overlaying the all the prices between bitstamp and coinbase, just visually you can see that there seemed to be more differences in the early dates than the latter dates.  This was supported / confirmed by Observation 1 above.
# 
# Observation 3: At "start" and "end" of a (single) day seemed to be more profitable then the "middle" part of the day

# In[ ]:




