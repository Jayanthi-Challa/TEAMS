def tiger_success_index(row):
    return (
        row["population_growth"] * 0.6 +
        row["area_sq_km"] * 0.4
    )