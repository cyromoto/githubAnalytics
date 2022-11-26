# import basic libraries for DA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#import the data file to frame
githubdf=pd.read_csv(".//github.csv")

#Plot bar chart for language used
githubdf['language'].value_counts().plot(kind='bar')
plt.show()





