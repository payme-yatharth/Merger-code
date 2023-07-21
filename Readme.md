The file "user_pincode_address.csv" contains three cols named as 'user', 'pincode' and the 'address' and correspondingly contains many tuples in it.
The file "first_run_till_merged.csv" contains two cols named as 'user' and 'distance' and correspondingly many tuples.
The script file aims to merge the two tables with user as the PK as it is unique and also pushing null values in the 'distance' for which the 'user' is not present in both tables.
The merged data is eventually stored in a new file named "merged_data.csv" which is saved in the directory.
