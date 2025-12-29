from src.create_dataframes import create_from_dict
from src.basic_operations import explore_dataframe
from src.data_manipulation import manipulate_data
from src.groupby_aggregation import group_by_city
from src.missing_data import create_missing_data, handle_missing
from src.file_io import save_to_csv, load_from_csv


def main():
    df = create_from_dict()
    explore_dataframe(df)

    df = manipulate_data(df)

    avg_salary, stats, counts = group_by_city(df)
    print("\nAverage salary by city:\n", avg_salary)

    missing_df = create_missing_data()
    handled = handle_missing(missing_df)

    save_to_csv(df, "data/raw/people_data.csv")
    print("\nSaved CSV successfully")

    df_loaded = load_from_csv("data/raw/people_data.csv")
    print("\nLoaded CSV preview:")
    print(df_loaded.head())


if __name__ == "__main__":
    main()
