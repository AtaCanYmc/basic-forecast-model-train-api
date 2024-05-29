import pandas as pd


def clean_nulls(dataframe, clean_list=['?', '-'], strategy='drop'):

    for char in clean_list:
        dataframe.replace(char, pd.NA, inplace=True)

    if strategy == 'drop':
        dataframe = dataframe.dropna()
    elif strategy == 'most_frequent':
        for column in dataframe.columns:
            most_frequent = dataframe[column].mode().iloc[0]
            dataframe[column].fillna(most_frequent, inplace=True)
    elif strategy == 'mean':
        for column in dataframe.select_dtypes(include=[float, int]).columns:
            mean_value = dataframe[column].mean()
            dataframe[column].fillna(mean_value, inplace=True)
    elif strategy == 'median':
        for column in dataframe.select_dtypes(include=[float, int]).columns:
            median_value = dataframe[column].median()
            dataframe[column].fillna(median_value, inplace=True)
    else:
        raise ValueError("Strategy not recognized. Use 'drop', 'most_frequent', 'mean', or 'median'.")

    return dataframe
