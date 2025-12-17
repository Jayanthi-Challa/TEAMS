import pandas as pd

def load_data():
    population = pd.read_csv("data/raw/tiger_population.csv")
    funding = pd.read_csv("data/raw/reserve_funding.csv")
    poaching = pd.read_csv("data/raw/poaching_incidents.csv")
    patrol = pd.read_csv("data/raw/patrol_paths.csv")
    return population, funding, poaching, patrol