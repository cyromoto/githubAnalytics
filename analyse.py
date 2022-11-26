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
plt.show()
  


