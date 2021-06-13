import pandas as pd

data = pd.read_csv("data_housing.csv")

for num in data:
    clean_data = data["rent"].str.extract(r'^(\d{0,10})', expand=False)
    data["rent"] = pd.to_numeric(clean_data)


# It needs more knowledge about processing DataFrames.
# In a theory it can optimize with loops and no duplicate code






