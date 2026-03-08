import pandas as pd

df = pd.read_csv("data/housing.csv")

df_5k = df.head(5000)

df_5k.to_csv("data/housing.csv", index=False)

print("Dataset truncated to 5000 rows")