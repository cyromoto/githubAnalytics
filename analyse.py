# import basic libraries for DA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#import the data file to frame
githubdf=pd.read_csv(".//github.csv")

#Plot bar chart for language used
githubdf['language'].value_counts().plot(kind='bar')
plt.show()


#Plot pie chart for language used
kwargs = dict(
    startangle = 90,
    colormap   = 'Pastel2',
    fontsize   = 13,
    figsize    = (60,5),
    autopct    = '%1.1f%%',
    title      = 'Used Languages'
)

dfForLanguage=githubdf.copy()
s = dfForLanguage['language'].value_counts()

#Split into major languages and minor languages
dfForLanguageSmall=dfForLanguage[dfForLanguage.isin(s.index[s <= 25]).values]
dfForLanguageLarge=dfForLanguage[dfForLanguage.isin(s.index[s > 25]).values]

# Group together the minor languages and append as Other languages
s = dfForLanguageLarge['language'].value_counts()
s['Others']=dfForLanguageSmall.groupby(['language'])['language'].count().sum()
s.plot.pie(**kwargs)
plt.savefig("output.png")
plt.show()


# #Pie for state
# githubdf['state'].value_counts().plot.pie(**kwargs)
# plt.show()


# df['coeff']=[-3.63693144e-04, -2.52929190e-07, -1.54264402e-06,
#                1.37321862e-04, -3.23741228e-05,  2.81550405e-06,
#                2.81550405e-06,  9.24001782e-01, -5.82090870e-01,
#               -4.43066925e-01,  2.81550405e-06, -2.05548705e-02,
#                3.78903330e-01]

# df['feature']=['commits', 'additions', 'deletions', 'changed_files',
#      'open_issues_count', 'watchers_count', 'forks_count', 'has_discussions',
#       'has_wiki', 'has_projects', 'stargazers_count', 'title_size', 'review_comments']


plt.bar(['commits', 'additions', 'deletions', 'changed_files',
     'open_issues_count', 'watchers_count', 'forks_count', 'has_discussions',
      'has_wiki', 'has_projects', 'stargazers_count', 'title_size', 'review_comments'],
            [-3.63693144e-04, -2.52929190e-07, -1.54264402e-06,
               1.37321862e-04, -3.23741228e-05,  2.81550405e-06,
               2.81550405e-06,  9.24001782e-01, -5.82090870e-01,
              -4.43066925e-01,  2.81550405e-06, -2.05548705e-02,
               3.78903330e-01],
        color ='maroon')
plt.show()