#!/usr/bin/env python
# coding: utf-8

# <h1>Exploration and Optimization of the Dataset to Facilitate Visualization in IBM Cognos</h1>

# <h3>🎯Objective</h3>

# The goal of the analysis and visualization is to highlight current and future trends in technologies and identify the most popular tools in the IT industry through the analysis of this survey of more than **65000 respondents** conducted in **2024**.
# 
# The objective of this notebook is to optimize data storage within the dataset to **facilitate visualization in IBM Cognos**. More specifically, the dataset originates from a survey where respondents were allowed to select multiple answers, particularly regarding languages, technologies, tools, and databases of interest. These items must be identified individually to **extract the top 10 based on their occurrence**.

# <h3>🛠️Import Necessary Libraries</h3>

# In[ ]:


get_ipython().system('pip install pandas')


# In[ ]:


import pandas as pd


# <h3>💻Load The Dataset as Dataframe</h3>

# In[ ]:


file_path = r"D:\Download\survey_data_updated 5.csv" # Utilise 'r' pour éviter les erreurs liées aux antislash

data = pd.read_csv(file_path)


# <h3>🔍Exploratory Analysis of the Quality of Variables of Interest</h3>

# **Check unique entry for LanguageHaveWorkedWith, DatabaseHaveWorkedWith, PlatformHaveWorkedWith and WebframeHaveWorkedWith**

# In[ ]:


data['LanguageHaveWorkedWith'].unique()


# In[ ]:


data['DatabaseHaveWorkedWith'].unique()


# In[ ]:


data['PlatformHaveWorkedWith'].unique()


# In[ ]:


data['WebframeHaveWorkedWith'].unique()


# **Check unique entry for LanguageWantToWorkWith, DatabaseWantToWorkWith, PlatformWantToWorkWith and WebframeWantToWorkWith**

# In[ ]:


data['LanguageWantToWorkWith'].unique()


# In[ ]:


data['DatabaseWantToWorkWith'].unique()


# In[ ]:


data['PlatformWantToWorkWith'].unique()


# In[ ]:


data['WebframeWantToWorkWith'].unique()


# **Check unique entry for Employment**

# In[ ]:


data['Employment'].nunique()


# In[ ]:


employment_counts = data['Employment'].value_counts()
print(employment_counts)


# **Check unique entry for Education Level**

# In[ ]:


data['EdLevel'].unique()


# In[ ]:


data['ResponseId'].nunique()


# <h3>✨Clean and Optimize the Dataset for Future Visualization</h3>

# **Refining the Dataframe to Focus on Variables of Interest and Removing Missing Data**

# In[ ]:


#select variables of interest
df = data[['ResponseId','Country','Employment','EdLevel','Age',
         'LanguageHaveWorkedWith','DatabaseHaveWorkedWith','PlatformHaveWorkedWith','WebframeHaveWorkedWith',
        'LanguageWantToWorkWith','DatabaseWantToWorkWith','PlatformWantToWorkWith','WebframeWantToWorkWith']]


# In[ ]:


#check the df
df.head()


# In[ ]:


df.shape


# In[ ]:


#identify column with high % of NaN
df.isna().sum() / len(df) * 100


# **Split and explode all technologies and tools variables**
# 
# The split method separates the multiple choices in the original column into a list for each respondent. The explode method then transforms these lists into individual rows, effectively multiplying the number of rows for each respondent based on their number of choices. The original column is modified, and other columns remain unchanged but are duplicated for the new rows. 

# >'Have Worked With' Tools

# In[ ]:


#Split LanguageHaveWorkedWith into list
df['LanguageHaveWorkedWith'] = df['LanguageHaveWorkedWith'].str.split(';')
df = df.explode('LanguageHaveWorkedWith')


# In[ ]:


#Split DatabaseHaveWorkedWith into list
df['DatabaseHaveWorkedWith'] = df['DatabaseHaveWorkedWith'].str.split(';')
df = df.explode('DatabaseHaveWorkedWith')


# In[ ]:


#Split PlatformHaveWorkedWith into list
df['PlatformHaveWorkedWith'] = df['PlatformHaveWorkedWith'].str.split(';')
df = df.explode('PlatformHaveWorkedWith')


# In[ ]:


#Split WebframeHaveWorkedWith into list
df['WebframeHaveWorkedWith'] = df['WebframeHaveWorkedWith'].str.split(';')
df = df.explode('WebframeHaveWorkedWith')


# >'Want to Work With' Tools

# In[ ]:


#Split LanguageWantToWorkWith into list
df['LanguageWantToWorkWith'] = df['LanguageWantToWorkWith'].str.split(';')
df = df.explode('LanguageWantToWorkWith')


# In[ ]:


#Split DatabaseWantToWorkWith into list
df['DatabaseWantToWorkWith'] = df['DatabaseWantToWorkWith'].str.split(';')
df = df.explode('DatabaseWantToWorkWith')


# In[ ]:


#Split PlatformWantToWorkWith into list
df['PlatformWantToWorkWith'] = df['PlatformWantToWorkWith'].str.split(';')
df = df.explode('PlatformWantToWorkWith')


# In[ ]:


#Split WebframeWantToWorkWith into list
df['WebframeWantToWorkWith'] = df['WebframeWantToWorkWith'].str.split(';')
df = df.explode('WebframeWantToWorkWith')


# **Top 10 of each Tools 'HaveWorkedWith'** for further check while creating dashboard

# In[ ]:


LanguageHaveWorkedWith_count = df['LanguageHaveWorkedWith'].value_counts() 
top10_LanguageHaveWorkedWith = LanguageHaveWorkedWith_count.head(10)
top10_LanguageHaveWorkedWith


# In[ ]:


DatabaseHaveWorkedWith_count = df['DatabaseHaveWorkedWith'].value_counts() 
top10_DatabaseHaveWorkedWith = DatabaseHaveWorkedWith_count.head(10)
top10_DatabaseHaveWorkedWith


# In[ ]:


PlatformHaveWorkedWith_count = df['PlatformHaveWorkedWith'].value_counts() 
top10_PlatformHaveWorkedWith = PlatformHaveWorkedWith_count.head(10)
top10_PlatformHaveWorkedWith


# In[ ]:


WebframeHaveWorkedWith_count = df['WebframeHaveWorkedWith'].value_counts() 
top10_WebframeHaveWorkedWith = WebframeHaveWorkedWith_count.head(10)
top10_WebframeHaveWorkedWith


# **Top 10 of each Tools 'WantToWorkWith'** for further check while creating dashboard

# In[ ]:


LanguageWantToWorkWith_count = df['LanguageWantToWorkWith'].value_counts() 
top10_LanguageWantToWorkWith = LanguageWantToWorkWith_count.head(10)
top10_LanguageWantToWorkWith


# In[ ]:


DatabaseWantToWorkWith_count = df['DatabaseWantToWorkWith'].value_counts() 
top10_DatabaseWantToWorkWith = DatabaseWantToWorkWith_count.head(10)
top10_DatabaseWantToWorkWith


# In[ ]:


PlatformWantToWorkWith_count = df['PlatformWantToWorkWith'].value_counts() 
top10_PlatformWantToWorkWith = PlatformWantToWorkWith_count.head(10)
top10_PlatformWantToWorkWith


# In[ ]:


WebframeWantToWorkWith_count = df['WebframeWantToWorkWith'].value_counts() 
top10_WebframeWantToWorkWith = WebframeWantToWorkWith_count.head(10)
top10_WebframeWantToWorkWith


# **Simplify the Employment status**

# The survey includes **60 employment status categories**, some of which reveal inconsistencies and present a methodological limitation that may affect the results. However, to extract the most valuable insights from the survey, I have chosen to implement a mapping strategy for employment statuses designed to mitigate interpretation biases.
# 
# The mapping has been streamlined to minimize the impact of inconsistencies (for example, being both employed full-time and part-time simultaneously).

# In[ ]:


#simplify Employment status

def mapping_employment(status):
    if 'Retired' in status:
        return 'Retired'
    elif 'Student, full-time' in status: ########
        return 'Full-time Student'
    elif 'Employed, part-time' in status: #####
        return 'Part-time Employment'
    elif 'Employed, full-time' in status and 'Independent contractor, freelancer, or self-employed' in status: ####
        return 'Freelancer/Full-time Employment'
    elif 'Employed, full-time' in status: ######
        return 'Full-time Employment'
    elif 'Independent contractor, freelancer, or self-employed' in status: ######
        return 'Freelancer'
    elif 'Not employed, but looking for work' in status: ######
        return 'Seeking Employment'
    elif ';' in status: 
        return 'Multiple Status'#######
    else:
        return 'Other' #######

# Apply the function
df['SimplifiedEmployment'] = df['Employment'].map(mapping_employment)


# In[ ]:


df.shape


# <h3>📂Save the Dataset as a CSV File</h3>

# In[ ]:


df.to_csv('survey_data_u5_optimized.csv', index=False)

