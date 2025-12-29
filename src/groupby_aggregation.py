def group_by_city(df):
    avg_salary = df.groupby("city")["salary"].mean()
    stats = df.groupby("city").agg({"salary": ["mean", "min", "max"], "age": "mean"})
    counts = df["city"].value_counts()

    return avg_salary, stats, counts
