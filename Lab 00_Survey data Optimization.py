import pandas as pd
#load the file
file_path = "survey_data_updated 5.csv" 
#convert as a dataframe
data = pd.read_csv(file_path)
print("Dataframe successfully loaded ! Size :", data.shape)
#select variables of interest
df = data[['ResponseId','Country','Employment','EdLevel','Age',
         'LanguageHaveWorkedWith','DatabaseHaveWorkedWith','PlatformHaveWorkedWith','WebframeHaveWorkedWith',
        'LanguageWantToWorkWith','DatabaseWantToWorkWith','PlatformWantToWorkWith','WebframeWantToWorkWith']]
#check the df
print("Dataframe successfully selected ! Size :", df.shape)
#check the first 5 rows
print(df.head())
#split and explode all the 8 columns with multiple values
#Split LanguageHaveWorkedWith into list
df['LanguageHaveWorkedWith'] = df['LanguageHaveWorkedWith'].str.split(';')
df = df.explode('LanguageHaveWorkedWith')
print("Step 1 - Dataframe successfully exploded ! Size :", df.shape)
#Split DatabaseHaveWorkedWith into list
df['DatabaseHaveWorkedWith'] = df['DatabaseHaveWorkedWith'].str.split(';')
df = df.explode('DatabaseHaveWorkedWith')
print("Step 2 - Dataframe successfully exploded ! Size :", df.shape)
#Split PlatformHaveWorkedWith into list
df['PlatformHaveWorkedWith'] = df['PlatformHaveWorkedWith'].str.split(';')
df = df.explode('PlatformHaveWorkedWith')
print("Step 3 - Dataframe successfully exploded ! Size :", df.shape)
#Split WebframeHaveWorkedWith into list
df['WebframeHaveWorkedWith'] = df['WebframeHaveWorkedWith'].str.split(';')
df = df.explode('WebframeHaveWorkedWith')
print("Step 4 - Dataframe successfully exploded ! Size :", df.shape)
#Split LanguageWantToWorkWith into list
df['LanguageWantToWorkWith'] = df['LanguageWantToWorkWith'].str.split(';')
df = df.explode('LanguageWantToWorkWith')
print("Step 5 - Dataframe successfully exploded ! Size :", df.shape)
#Split DatabaseWantToWorkWith into list
df['DatabaseWantToWorkWith'] = df['DatabaseWantToWorkWith'].str.split(';')
df = df.explode('DatabaseWantToWorkWith')
print("Step 6 - Dataframe successfully exploded ! Size :", df.shape)
#Split PlatformWantToWorkWith into list
df['PlatformWantToWorkWith'] = df['PlatformWantToWorkWith'].str.split(';')
df = df.explode('PlatformWantToWorkWith')
print("Step 7 - Dataframe successfully exploded ! Size :", df.shape)
#Split WebframeWantToWorkWith into list
df['WebframeWantToWorkWith'] = df['WebframeWantToWorkWith'].str.split(';')
df = df.explode('WebframeWantToWorkWith')
print("Step 8 - Dataframe successfully exploded ! Size :", df.shape)
#display the top 10 of each of the 8 tools
#top 10 LanguageHaveWorkedWith
LanguageHaveWorkedWith_count = df['LanguageHaveWorkedWith'].value_counts() 
top10_LanguageHaveWorkedWith = LanguageHaveWorkedWith_count.head(10)
top10_LanguageHaveWorkedWith
print("top 10 LanguageHaveWorkedWith :", top10_LanguageHaveWorkedWith)
#top 10 DatabaseHaveWorkedWith
DatabaseHaveWorkedWith_count = df['DatabaseHaveWorkedWith'].value_counts() 
top10_DatabaseHaveWorkedWith = DatabaseHaveWorkedWith_count.head(10)
top10_DatabaseHaveWorkedWith
print("top 10 DatabaseHaveWorkedWith :", top10_DatabaseHaveWorkedWith)
#top 10 PlatformHaveWorkedWith:
PlatformHaveWorkedWith_count = df['PlatformHaveWorkedWith'].value_counts() 
top10_PlatformHaveWorkedWith = PlatformHaveWorkedWith_count.head(10)
top10_PlatformHaveWorkedWith
print("top 10 PlatformHaveWorkedWith :", top10_PlatformHaveWorkedWith)
#top 10 WebframeHaveWorkedWith  
WebframeHaveWorkedWith_count = df['WebframeHaveWorkedWith'].value_counts() 
top10_WebframeHaveWorkedWith = WebframeHaveWorkedWith_count.head(10)
top10_WebframeHaveWorkedWith
print("top 10 WebframeHaveWorkedWith :", top10_WebframeHaveWorkedWith)
#top 10 LanguageWantToWorkWith
LanguageWantToWorkWith_count = df['LanguageWantToWorkWith'].value_counts() 
top10_LanguageWantToWorkWith = LanguageWantToWorkWith_count.head(10)
top10_LanguageWantToWorkWith
print("top 10 LanguageWantToWorkWith :", top10_LanguageWantToWorkWith)
#top 10 DatabaseWantToWorkWith
DatabaseWantToWorkWith_count = df['DatabaseWantToWorkWith'].value_counts() 
top10_DatabaseWantToWorkWith = DatabaseWantToWorkWith_count.head(10)
top10_DatabaseWantToWorkWith
print("top 10 DatabaseWantToWorkWith :", top10_DatabaseWantToWorkWith)
#top 10 PlatformWantToWorkWith
PlatformWantToWorkWith_count = df['PlatformWantToWorkWith'].value_counts() 
top10_PlatformWantToWorkWith = PlatformWantToWorkWith_count.head(10)
top10_PlatformWantToWorkWith
print("top 10 PlatformWantToWorkWith :", top10_PlatformWantToWorkWith)
#top 10 WebframeWantToWorkWith
WebframeWantToWorkWith_count = df['WebframeWantToWorkWith'].value_counts() 
top10_WebframeWantToWorkWith = WebframeWantToWorkWith_count.head(10)
top10_WebframeWantToWorkWith
print("top 10 WebframeWantToWorkWith :", top10_WebframeWantToWorkWith)

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

# Apply the function
df['Employment_status'] = df['Employment'].map(mapping_employment)
# Check the process execution
print("Employment status successfully simplified ! Size :", df.shape)
# Drop the original Employment column
df.drop(columns=['Employment'], inplace=True)
print("Employment column successfully dropped ! Size :", df.shape)
# Check the new dataframe
print("Dataframe successfully updated ! Size :", df.shape)
# Save the updated dataframe to a new CSV file
df.to_csv('survey_data_u5_optimized.csv', index=False)
print("Csv file successfully saved !")
