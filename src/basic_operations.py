def explore_dataframe(df):
    print("\nINFO:")
    print(df.info())

    print("\nHEAD:")
    print(df.head(3))

    print("\nTAIL:")
    print(df.tail(2))

    print("\nDESCRIBE:")
    print(df.describe())
