def manipulate_data(df):
    df["bonus"] = df["salary"] * 0.1
    df["age"] += 1
    return df


def sort_data(df):
    return {
        "by_salary": df.sort_values("salary", ascending=False),
        "by_city_age": df.sort_values(["city", "age"]),
    }
