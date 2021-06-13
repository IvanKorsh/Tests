import pandas as pd
import numpy as np

data = pd.read_csv("data_housing.csv")

clean = data["rent"].str.extract(r'^(\d{3})', expand=False)
to_num = data["rent"] = pd.to_numeric(clean)


print(lol)