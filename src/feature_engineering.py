import pandas as pd

def merge_features(population, funding):
    df = population.merge(funding, on="reserve_id", how="left")
    df["population_growth"] = df.groupby("reserve_id")["population"].diff().fillna(0)
    return df