import numpy as np
import pandas as pd 
from pandas.core.reshape.merge import merge

import utils 

days_file = r"/Users/sberkson/Desktop/Gonzaga/CPSC222/DA3/days_of_week_9-20-20_9-20-21.csv"
youtube_file = r"/Users/sberkson/Desktop/Gonzaga/CPSC222/DA3/youtube_analytics_9-20-20_9-20-21.csv"

days_header = ["Date", "Day of Week"]
youtube_header = ["Views", "Average percentage viewed (%)", "Unique viewers", "Subscribers", "Watch time (hours)", "Average view duration", "Shares", "Likes", "Dislikes", "Comments added", "Impressions", "Impressions click-through rate (%)"]
df_days = utils.load_file(days_file)
df_youtube = utils.load_file(youtube_file)

'''
start_date = input("Please enter a start date (inclusive): ")
end_date = input("Please enter an end date (exclusive): ")
user_column = int(input("Please enter the number of the column that you wish to view: \n0)  Views\n1)  Average percentage viewed (%)\n2)  Unique viewers\n3)  Subscribers\n4)  Watch time (hours)\n5)  Average view duration\n6)  Shares\n7)  Likes\n8)  Dislikes\n9)  Comments added\n10) Impressions\n11) Impressions click-through rate ($)\n"))
'''

start_date = utils.grab_input("Please enter a start date (inclusive): ")
end_date = utils.grab_input("Please enter an end date (exclusive): ")
user_column = int(utils.grab_input("Please enter the number of the column that you wish to view: \n0)  Views\n1)  Average percentage viewed (%)\n2)  Unique viewers\n3)  Subscribers\n4)  Watch time (hours)\n5)  Average view duration\n6)  Shares\n7)  Likes\n8)  Dislikes\n9)  Comments added\n10) Impressions\n11) Impressions click-through rate ($)\n"))


sliced_youtube_df = df_youtube.loc[start_date:end_date]
print(sliced_youtube_df)
user_ser = df_youtube[youtube_header[user_column]]

series_mean, series_std, series_median, series_sum, series_smallest, series_largest = utils.compute_stats(user_ser)
computed_ser = utils.stats_to_series(series_mean, series_std, series_median, series_sum, series_smallest, series_largest)
computed_ser.to_csv("YoutubeStats.csv")

merged_df = df_youtube.merge(df_days, on="Date")
merged_df.to_csv("MergedDF.csv")

combined_mean_ser = utils.apply_split_combine(merged_df, youtube_header, user_column)
combined_mean_ser.to_csv("ApplySplitCombine.csv")