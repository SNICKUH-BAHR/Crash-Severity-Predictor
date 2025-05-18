# Run this script to clean, save, and export data
import pandas as pd
import os
from clean_data import filter_data
from save_data import save_df


# Crash data years
years = [2018, 2019, 2020, 2021]

# Initial selected features 
include_cols = [
    'TOTAL_UNITS', 'AUTOMOBILE_COUNT', 'PED_COUNT' ,'COLLISION_TYPE', 'CRASH_MONTH', 'DEC_LAT', 'DEC_LONG', 
    'ILLUMINATION_DARK', 'INTERSECT_TYPE', 'TIME_OF_DAY', 'WEATHER', 'URBAN_RURAL', 'VEHICLE_COUNT',
    'DRIVER_COUNT_16YR', 'DRIVER_COUNT_17YR','DRIVER_COUNT_18YR', 'DRIVER_COUNT_19YR', 'DRIVER_COUNT_20YR', 
    'DRIVER_COUNT_50_64YR', 'DRIVER_COUNT_65_74YR', 'DRIVER_COUNT_75PLUS',
    'FATAL_COUNT', 'INJURY_COUNT', 'TOT_INJ_COUNT', 'MAX_SEVERITY_LEVEL'
]

# Extraneous values
exclude_vals = {
    'TIME_OF_DAY': [9999], 
    'INTERSECT_TYPE': [10, 99], 
    'WEATHER': [98], 
    'MAX_SEVERITY_LEVEL': [8, 9]
}

# Converting strings to integers
substitute = {
    'ILLUMINATION_DARK': {
        'Yes': 1, 
        'No': 0
    }
}

# Formatting data using above parameters
crash_data = []

for year in years:
    pth = f'data/crash_data/crash-data-{year}.csv' 
    if os.path.exists(pth):
        df = filter_data(pth, include_cols=include_cols, exclude_vals=exclude_vals, substitute=substitute)
        crash_data.append(df[include_cols])
    else:
        print(f"The file at '{pth}' does not exist.")

train_set = pd.concat([crash_data[0], crash_data[1]], ignore_index=True)
val_set, test_set = crash_data[2], crash_data[3]

# Uncomment this to save training, testing, and validation datasets
'''
df_names = ['train', 'validate', 'test']
for i, df in enumerate([train_set, val_set, test_set]):
    save_df(df, df_names[i], 'data/train_test_split')
'''