def tiger_success_index(row):
    return (
        row["population_growth"] * 0.5 +
        row["area_sq_km"] * 0.3 +
        row["funding_crore"] * 0.2
    )