import pandas as pd
import numpy as np

# Read the first CSV file
df1 = pd.read_csv('user_pincode_address.csv')

# Read the second CSV file
df2 = pd.read_csv('first_run_till_merged.csv')

# Merge the two dataframes using 'user' as the primary key (Left Join)
merged_df = pd.merge(df1, df2, on='user', how='left')

# Rename the distance column from the second table to 'distance' if needed
merged_df.rename(columns={'distance_y': 'distance'}, inplace=True)

# If a user is not present in the second table, set distance as null
merged_df['distance'].fillna(value=np.nan, inplace=True)

# Save the merged dataframe to a new CSV file
merged_df.to_csv('merged_data.csv', index=False)
