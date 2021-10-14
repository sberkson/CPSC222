import pandas as pd

def load_file(file_name):
    df = pd.read_csv(file_name, header = 0)

    return df

def grab_input(output_string):
    return input(output_string)

def compute_stats(user_ser):
    series_mean = user_ser.mean()
    series_std = user_ser.std()
    series_median = user_ser.median()
    series_sum = user_ser.sum()
    series_smallest = user_ser.min()
    series_largest = user_ser.max()

    return series_mean, series_std, series_median, series_sum, series_smallest, series_largest

def stats_to_series(series_mean, series_std, series_median, series_sum, series_smallest, series_largest):
    computed_ser = pd.Series(dtype=int)
    computed_ser["Sum"] = series_sum
    computed_ser["Mean"] = series_mean
    computed_ser["StdDev"] = series_std
    computed_ser["Median"] = series_median
    computed_ser["Smallest"] = series_smallest
    computed_ser["Largest"] = series_largest

    return computed_ser

def apply_split_combine(merged_df, header, column):
    grouped_by_day = merged_df.groupby("Day of Week")
    combined_mean_ser = pd.Series(dtype=int)

    combined_mean_ser = grouped_by_day[header[column]].mean()
    return combined_mean_ser