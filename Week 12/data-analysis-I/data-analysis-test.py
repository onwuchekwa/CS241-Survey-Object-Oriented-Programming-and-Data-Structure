import pandas as pd # Our data manipulation library
import seaborn as sns # Used for graphing/plotting
import matplotlib.pyplot as plt # If we need any low level methods
import os # Used to change the directory to the right place

# This line isn't necessary, but it makes it so the later commands (e.g., read_csv)
# are in a consistent place (You will obviously need to change this to the correct location on _your_ computer.)
# If you have put the data files and your Python script in the same folder, you
# don't need this line.
os.chdir("/Users/osunday/Documents/School/BYUI/Winter 2020/CS 241 Survey Object Oriented Programming and Data Structure/Week 12/data-analysis-I/nba_basketball_data/")

# Load in the data
# The players data (basketball_players.csv) has the season stats
players = pd.read_csv("basketball_players.csv")

# Show player data
print(players)

print()

# View available table columns
print(players.columns)

print()

# We can look at statistics about certain variables. For example,
# we can look at the min, max, mean, and median for a column like
# rebounds
min = players["rebounds"].min()
max = players["rebounds"].max()
mean = players["rebounds"].mean()
median = players["rebounds"].median()

print("Rebounds per season: Min:{}, Max:{}, Mean:{:.2f}, Median:{}".format(min, max, mean, median))

'''
    Instructor Tip:
    When working with existing columns, you can either use the dot
    notation "players.rebounds" or the square bracket notation
    "players["rebounds"]". If you are creating a new column or if your
    column name has a space in it, you must use the square bracket notation.
'''
'''
    Perhaps we want to look at the highest rebounding seasons to see the
    player that had that amount and the team they played on. We can sort
    the data by rebounds and print out the top 10 rows:
'''
print(players.sort_values("rebounds", ascending=False).head(10))

'''
    That is showing a lot of columns and making it hard to read, so we
    might repeat it and only show a few:
'''
print(players[["playerID", "year", "tmID", "rebounds"]].sort_values("rebounds", ascending=False).head(10))

# Merging or Joining Separate Datasets
# The "master" data (basketball_master.csv) has names, biographical information, etc.
master = pd.read_csv("basketball_master.csv")

# We can do a left join to "merge" these two datasets together
nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")

'''
    At this point the variable nba contains a full dataset with many
    different rows and columns. By printing that variable or its columns,
    you can see a summary of the dataset.
'''
print(nba.columns)

'''
    With this additional information, we can return to printing out the
    top rebounders, but this time, we will use the nba variable and use
    different columns:
'''

print()

print(nba[["year", "useFirst", "lastName", "tmID", "rebounds"]].sort_values("rebounds", ascending=False).head(10))

'''
    Creating new columns
    While the total number of rebounds in a season is interesting, most
    people like to compare an average of rebounds per game. Unfortunately,
    a column for this is not available in this dataset, however, there is
    a column for rebounds, and one for games played (GP) so we can make a
    new column on our own that contains this information by dividing
    rebounds by games played:
'''
print()

nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]
print(nba[["year", "useFirst", "lastName", "rebounds", "GP", "reboundsPerGame"]].sort_values("reboundsPerGame", ascending=False).head(10))

'''
    This gives us a nice view of the top performers for rebounds per
    game. As we look at the dataset, we should see if this makes sense.
    The first thing that should stand out is that Mike Conley is listed
    has having rebounds in 2007 and 2008 without playing any games.
    This must clearly be an error in the data. It turns out this kind of
    thing happens all the time in real datasets, so we always need to be
    on the lookout for it. If we have the ability, we could talk to the
    people that produced the data and see if they could fix the problem,
    but in this case, we don't have that option. So our best choice is
    probably to remove any rows that don't have games played.
'''
# Let's just remove any rows with GP=0
nba = nba[nba.GP > 0]
print()
nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]
print(nba[["year", "useFirst", "lastName", "rebounds", "GP", "reboundsPerGame"]].sort_values("reboundsPerGame", ascending=False).head(10))

'''
    Basic Plotting with Seaborn
    First, let's begin with a boxplot of rebounds. There are ways to do
    this directly in pandas (nba.boxplot(column=["rebounds"])), but we
    are going to use the Seaborn library which is a little more powerful
    and user friendly. It is using the same matplotlib library that
    pandas is, but it wraps it in nicer functions. The following shows
    how to produce a boxplot in Seaborn:
'''
sns.boxplot(data=nba.reboundsPerGame)

'''
    Depending on your environment, running a command like the one above
    may bring up the plot automatically for viewing. Or it may just
    prepare it in the background and wait for you to tell it to show it
    or save it to a file, etc. This can be done with the matplotlib
    library that we imported earlier as plt. With this, we can show
    the current plot or save it to a file:
'''
# Show the current plot
plt.show()

# Save the current plot to a file
# plt.savefig("boxplot_reboundsPerGame.png")

'''
    If we want to do a box plot of multiple columns we can also do that.
    Here are rebounds, offensive rebounds, and defensive rebounds shown
    together:
'''
sns.boxplot(data=nba[["rebounds", "oRebounds", "dRebounds"]])
plt.show()

'''
    Rebounds Over Time - Approach 1: FacetGrid
    
    With some basic plotting in place, we are ready to revisit the
    question of whether rebounding trends have changed over time.

    One approach could be to use "facets," and put a whole bunch of
    small boxplots all next to each other. Seaborn has a facet grid
    function that makes this fairly easy. It might be too much to have
    a separate plot for every year from 1930-2010, so let's focus just
    on the '80s first.
'''
# Get a subset of the data where the year is between 1980 and 1990
eighties = nba[(nba.year >= 1980) & (nba.year < 1990)]

'''
    Now let's play around with this to see what we want each facet or
    mini-plot to look like:
'''
sns.boxplot(eighties["reboundsPerGame"], orient="v")
plt.show()

'''
    That seems to look ok, so now we will set up a FacetGrid and map
    this function for each facet.
'''
grid = sns.FacetGrid(eighties, col="year")
grid.map(sns.boxplot, "reboundsPerGame", orient="v")
plt.show()

'''
    This is nice and contains a lot of information. But it is really
    hard to see anything related to the trend we want, namely rebounds
    from the '60s and '70s versus today. So I don't like it. At this
    point let's abandon the facet grid approach, and instead, perhaps
    we could just plot a single point per year, like the median number
    of rebounds for all players for that year, and look for trends in
    that.
'''

'''
    Instructor Tip:

    Whoa! Why did we even do these previous steps if we are just going
    to abandon them?

    It turns out that data science is a process of discovery, trial, and
    error. Sometimes we have an idea, we try it and find out we don't
    like it, so we have to consider other options. Most tutorials out
    there (including this one) mostly show the finished product of
    someone else's discovery process. This is hard, because the
    important thing for you to learn is actually the process, not the
    end result.
'''
'''
    Rebounds Over Time - Approach 2: Grouping by Year

    To plot rebounds per year, we first need to group the statistics by
    year. When we do so, we need to specify how we want to aggregate the
    data of that year. In this case, we'll use the median of the
    reboundsPerGame.
'''
nba_grouped_year = nba[["reboundsPerGame", "year"]].groupby("year").median()
print(nba_grouped_year)

'''
    Notice that we assigned this to a new variable nba_grouped_year so
    that we can work with this new version of the dataset that is
    oriented differently.

    In order to plot this data, we need to change the index to be the
    year now, rather than the id that it was previously. Then we can
    plot it along with a linear regression line as follows:
'''
nba_grouped_year = nba_grouped_year.reset_index()
sns.regplot(data=nba_grouped_year, x="year", y="reboundsPerGame")
plt.show()

'''
    It looks like there are a lot of years where rebounds must not have
    been tracked (at least in this dataset), so let's remove any years
    where the median was 0. This time, let's also put a title on the
    plot.
'''
nba_grouped_year = nba_grouped_year[nba_grouped_year["reboundsPerGame"] > 0]
sns.regplot(data=nba_grouped_year, x="year", y="reboundsPerGame").set_title("Median rebounds per Year")
plt.show()

'''
    Judging from this plot, it looks like there has certainly been a
    difference in the rebounding from the '60s versus later years.

    One question we might ask though is, could this be the result of
    the fact that we just used the median? Maybe there are a lot more
    players now, and the top rebounders are still just as productive.
    We could repeat the previous steps, but this time use the max
    instead of the median.
'''

nba_grouped_year = nba[["reboundsPerGame", "year"]].groupby("year").max()
nba_grouped_year = nba_grouped_year.reset_index()

# Remove the zeros
nba_grouped_year = nba_grouped_year[nba_grouped_year["reboundsPerGame"] > 0]
sns.regplot(data=nba_grouped_year, x="year", y="reboundsPerGame").set_title("Max rebounds per year")
plt.show()

'''
    Summarizing in More Complicated ways

    From the previous plot, we can still see a similar trend, which makes
    us feel a little better about our conclusion. However, this summary
    is still a little bit troubling, because it could be skewed a lot by
    the top rebounder of that year. Perhaps that rebounder was a major
    outlier from the rest of the league. Another way to consider this is
    to find the top 10 rebounders of the year and look at their median.
'''

# Get the top 10 rebounders per year
nba_topRebounders_perYear = nba[["reboundsPerGame", "year"]].groupby("year")["reboundsPerGame"].nlargest(10)

# Get the median of these 10
nba_topRebounders_median_perYear = nba_topRebounders_perYear.groupby("year").median()

# Put year back in as a column
nba_topRebounders_median_perYear = nba_topRebounders_median_perYear.reset_index()

# Again no zeros...
nba_topRebounders_median_perYear_noZeros = nba_topRebounders_median_perYear[nba_topRebounders_median_perYear["reboundsPerGame"] > 0]

# Now plot
sns.regplot(data=nba_topRebounders_median_perYear_noZeros, x="year", y="reboundsPerGame").set_title("Median of Top 10 Rebounders Each Year")
plt.show()

