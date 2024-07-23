import pandas as pd
import numpy as np

# #Controls the number of columns to be printed
#pd.set_option('display.max_columns', None)

# Importing raw data that was collected from data_collection_final.py
data_raw = pd.read_csv('data/raw/data_collection_raw.csv',header=None)

# Creating a new header
new_headers=['Rank','Player_Name','Nation','Position','Club','Age','Born','Matches_Played','Starts','Minutes_Played',
         'Ninety_Mins_Played','Goals','Assists','Goals_Assists','Non_Penalty_Goals','Penalty_Made',
         'Penalty_Attempted','Yellow_Card','Red_Card','Expected_Goals','Non_Penalty_Expected_Goals',
         'Expected_Assists','Non_Penalty_Expected_Goals_Assists','Progressive_Carries','Progressive_Passes',
         'Progressive_Passes_Received','Goals_90','Assists_90','Goals_Assists_90','Non_Penalty_Goals_90',
         'Non_Penalty_Goals_Assists_90','Expected_Goals_90','Expected_Assists_90','Expected_Goals_Assists_90',
         'Non_Penalty_Expected_Goals_90','Non_penalty_Expected_Goals_Assists_90','Matches']

# Adding a new header to the raw data
data_raw.columns=new_headers

# Converting into DataFrame
df_raw=pd.DataFrame(data_raw)

# Removing the first 2 rows from the raw data
df_raw.drop([0,1],inplace=True)

# Removing the headers from the raw data repeating after 25 entries
df_raw = df_raw[df_raw.Rank !='Rk']

'''Filling the empty cells of 'Nation' column with 'EMT' 
& taking only last 3 letters which contain the initials of the nation''' 
df_raw['Nation'] = df_raw.Nation.replace(to_replace = np.nan,value='EMT').str[-3:]  #Can use fillna instead of replace 

# Dropping 'Rank' and 'Matches' columns
df_raw = df_raw.drop(['Rank','Matches'],axis=1)

# Filling the empty cells of 'Age' column with -1
df_raw['Age'] = df_raw.Age.fillna(-1)

# Filling the empty cells of 'Born' column with 'unknown'
df_raw['Born'] = df_raw.Born.fillna('unknown')

# Filling the empty cells of entire ddataframe with 0
df_raw = df_raw.fillna(0)

#print(df_raw.head())
#print(df_raw.info())


df_raw.to_csv('data/cleaned/data_cleaned.csv',index=False)

print("Data has been successfully cleaned and saved to data/cleaned/data_cleaned.csv")



