import pandas as pd
import re

line = "=================================================================================="

print(line)
print("Reading only 3 first rows of data")

data_frame = pd.read_csv('pokemon_data.csv')
print(data_frame.head(3))

print(line)
print("Reading only 3 last rows of data")

print(data_frame.tail(3))

print(line)
print("Reading data from txt file")

txt_data_frame = pd.read_csv('pokemon_data.txt', delimiter='\t')
print(txt_data_frame.head(3))

print(line)
print("Reading only columns \"Name\" and \"Type 1\"")

print(data_frame[['Name', 'Type 1']][:5])

print(line)
print("Printing only data from first row")

print(data_frame.iloc[0])

print(line)
print("Printing data from specific location")

print(data_frame.iloc[5, 1])

print(line)
print("Printing data column contains specific data")

print(data_frame.loc[data_frame['Type 1'] == 'Fire'])

#data_frame.to_csv('modified.csv', index=False)

#data_frame.to_excel('excel_mod.xlsx', index=False)

#data_frame.to_csv('data_txt.txt', index=False, sep='\t')

print(line)
print("regex")

print(data_frame.loc[data_frame['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])
print(data_frame.loc[data_frame['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])
