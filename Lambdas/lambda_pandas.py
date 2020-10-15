import pandas as pd

# Define simple dictionary
my_dict = dict(names=["Joe", "Mike", "Otto"], ages=[23, 12, 54])

# Read in dictionary to dataframe
df = pd.DataFrame(my_dict)

# Applymap example using lambda
df.applymap(lambda x: len(str(x)))

# Lambda usage example on a series
df["names"].apply(lambda x: x[::-1])

# Lambda usage example on 'loc' property
df.loc[lambda df: df["ages"] > 18]
