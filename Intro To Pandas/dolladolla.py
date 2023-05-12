import pandas as pd

df = pd.read_csv("pokemon_data.csv")

with pd.option_context("display.max_rows", None, "display.max_columns", None):
    print(df.head(15))
    print(df.columns)

