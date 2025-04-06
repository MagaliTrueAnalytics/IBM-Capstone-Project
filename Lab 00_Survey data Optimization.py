import pandas as pd
#load the file from google drive
url = "https://drive.google.com/uc?export=download&id=1sY69yUa9gQ0b0MOUjVY6T0B3wG9Yu-aR"

#convert as a dataframe
data = pd.read_csv(url)
print("Dataframe successfully loaded ! Size :", data.shape)
#select variables of interest
df = data[['ResponseId','Country','Employment','EdLevel','Age',
         'LanguageHaveWorkedWith','DatabaseHaveWorkedWith','PlatformHaveWorkedWith','WebframeHaveWorkedWith',
        'LanguageWantToWorkWith','DatabaseWantToWorkWith','PlatformWantToWorkWith','WebframeWantToWorkWith']]
#check the df
print("Dataframe successfully selected ! Size :", df.shape)
#check the first 5 rows
print(df.head())
##create the CSV file for demographics CSV0##
#Employment has 60 unique values, we will simplify it to 9 values
#simplify Employment status function
def mapping_employment(status):
    if 'Retired' in status:
        return 'Retired'
    elif 'Student, full-time' in status:
        return 'Full-time Student'
    elif 'Employed, part-time' in status:
        return 'Part-time Employment'
    elif 'Employed, full-time' in status and 'Independent contractor, freelancer, or self-employed' in status:
        return 'Freelancer/Full-time Employment'
    elif 'Employed, full-time' in status:
        return 'Full-time Employment'
    elif 'Independent contractor, freelancer, or self-employed' in status:
        return 'Freelancer'
    elif 'Not employed, but looking for work' in status: 
        return 'Seeking Employment'
    elif ';' in status: 
        return 'Multiple Status'
    else:
        return 'Other'

df_csv0 = df[['ResponseId', 'Employment','Country', 'EdLevel', 'Age']]
# Apply the function
df_csv0['Employment_status'] = df_csv0['Employment'].map(mapping_employment)
# Check the process execution
print("Employment status successfully simplified ! Size :", df.shape)
# Drop the original Employment column
df_csv0.drop(columns=['Employment'], inplace=True)
print("Employment column successfully dropped ! Size :", df.shape)
#save the updated dataframe to a new CSV file
df_csv0.to_csv('csv0_demographics.csv', index=False)
print("csv0_demographics.csv successfully created ! Size :", df.shape)
##Create the first CSV file CSV1##
# Créer une nouvelle DataFrame pour CSV 1
df_csv1 = df[['ResponseId', 'LanguageHaveWorkedWith', 'DatabaseHaveWorkedWith']]
# Split/explode
df_csv1['LanguageHaveWorkedWith'] = df_csv1['LanguageHaveWorkedWith'].str.split(';')
df_csv1 = df_csv1.explode('LanguageHaveWorkedWith')
df_csv1['DatabaseHaveWorkedWith'] = df_csv1['DatabaseHaveWorkedWith'].str.split(';')
df_csv1 = df_csv1.explode('DatabaseHaveWorkedWith')
print("Step 1 - Dataframe successfully exploded ! Size :", df.shape)
# Sauvegarder le fichier CSV 1
df_csv1.to_csv("csv1_language_database_hww.csv", index=False)
print("csv1_language_database_hww.csv successfully created ! Size :", df_csv1.shape)
# Créer une nouvelle DataFrame pour CSV 2
df_csv2 = df[['ResponseId', 'PlatformHaveWorkedWith', 'WebframeHaveWorkedWith']]
# Split/explode
df_csv2['PlatformHaveWorkedWith'] = df_csv2['PlatformHaveWorkedWith'].str.split(';')
df_csv2 = df_csv2.explode('PlatformHaveWorkedWith')
df_csv2['WebframeHaveWorkedWith'] = df_csv2['WebframeHaveWorkedWith'].str.split(';')
df_csv2 = df_csv2.explode('WebframeHaveWorkedWith')
print("Step 2 - Dataframe successfully exploded ! Size :", df.shape)
# Sauvegarder le fichier CSV 2
df_csv2.to_csv("csv2_platform_webframe_hww.csv", index=False)
print("csv2_platform_webframe_hww.csv successfully created ! Size :", df_csv2.shape)
# Créer une nouvelle DataFrame pour CSV 3
df_csv3 = df[['ResponseId', 'LanguageWantToWorkWith', 'DatabaseWantToWorkWith']]
# Split/explode
df_csv3['LanguageWantToWorkWith'] = df_csv3['LanguageWantToWorkWith'].str.split(';')
df_csv3 = df_csv3.explode('LanguageWantToWorkWith')
df_csv3['DatabaseWantToWorkWith'] = df_csv3['DatabaseWantToWorkWith'].str.split(';')
df_csv3 = df_csv3.explode('DatabaseWantToWorkWith')
print("Step 3 - Dataframe successfully exploded ! Size :", df.shape)
# Sauvegarder le fichier CSV 3
df_csv3.to_csv("csv3_language_database_wtw.csv", index=False)
print("csv3_language_database_wtw.csv successfully created ! Size :", df_csv3.shape)
# Créer une nouvelle DataFrame pour CSV 4
df_csv4 = df[['ResponseId', 'PlatformWantToWorkWith', 'WebframeWantToWorkWith']]
# Split/explode
df_csv4['PlatformWantToWorkWith'] = df_csv4['PlatformWantToWorkWith'].str.split(';')
df_csv4 = df_csv4.explode('PlatformWantToWorkWith')
df_csv4['WebframeWantToWorkWith'] = df_csv4['WebframeWantToWorkWith'].str.split(';')
df_csv4 = df_csv4.explode('WebframeWantToWorkWith')
print("Step 4 - Dataframe successfully exploded ! Size :", df.shape)
# Sauvegarder le fichier CSV 4
df_csv4.to_csv("csv4_platform_webframe_wtw.csv", index=False)
print("csv4_platform_webframe_wtw.csv successfully created ! Size :", df_csv4.shape)

print("Process completed successfully !")