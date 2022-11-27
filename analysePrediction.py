# import basic libraries for DA
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import numpy as np
from wordcloud import WordCloud

colors = np.random.rand(19191)
#import the data file to frame
githubdf=pd.read_csv(".//github_predicted.csv")


githubdfTemp=githubdf.iloc[:, 14:]
githubdfTemp=pd.get_dummies(githubdfTemp).idxmax(1)

githubdf.drop(columns=githubdf.iloc[:,14:].columns.tolist(), inplace=True)
githubdf['language']=githubdfTemp
# githubdf.to_csv(".//samplePrediction.csv",index=False)

# Plot language bar chart
githubdf['language'].value_counts().plot(kind='bar')
plt.show()

# Plot Histograms
githubdf['Status'] = pd.cut(x=githubdf['merged'], bins=[-1,.9, 1.1],labels=['Pending','Merged'])
print(githubdf)
githubdf['Status'].value_counts().plot(kind='bar')
plt.show()


# plt.bar(githubdf['Status'],githubdf['additions'],
#         color ='maroon')
# plt.show()


plt.scatter(githubdf['Status'],githubdf['stargazers_count'],c=colors, alpha=0.5)
plt.show()

dataFrameAuthor = pd.DataFrame(githubdf['language'].values.tolist()).value_counts().rename_axis('Model').reset_index(name='counts')
dataFrameAuthor.columns = ['Term','Count']
wordCloudInputCountry = dataFrameAuthor.set_index('Term').to_dict()['Count']
wcCountry= WordCloud(background_color="white", width=1000, height=500, max_words=200).generate_from_frequencies(wordCloudInputCountry)
plt.figure(figsize=(15, 15))
plt.imshow(wcCountry, interpolation='bilinear')
plt.axis('off')

plt.show()