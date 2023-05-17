import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
dataframe = pd.read_csv('Iris.csv')
dataframe.head()

def frequency_graph():
  y=dataframe['Species'].value_counts()
  y.plot.bar(color=['red','orange','yellow'])
  plt.title('Frequency graph')
  plt.xlabel('Species')
  plt.ylabel('Frequency')
  plt.show()

def pcacomponent():
  X = dataframe[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
  pca = PCA(n_components=2)
  components = pca.fit_transform(X)
  
  principalDf=pd.DataFrame(data=components,columns=['principal component 1'#
                         ,'principal component 2']) 
  principalDf.head()
  finalDf=pd.concat([principalDf,dataframe[['Species']]],axis=1)
  finalDf.head()
  fig=plt.figure(figsize=(8,8))  
  ax=fig.add_subplot(1,1,1)  
  ax.set_xlabel('Principal Component 1',fontsize = 15)  
  ax.set_ylabel('Principal Component 2',fontsize = 15)  
  ax.set_title('Two Principle Components',fontsize=20)  
  targets=['Iris-setosa','Iris-versicolor','Iris-virginica'] 
  colors=['r','g','b']  
  for target,color in zip(targets,colors):    
     indicesToKeep = finalDf['Species'] == target  
     ax.scatter(finalDf.loc[indicesToKeep,'principal component 1'],
              finalDf.loc[indicesToKeep,'principal component 2'],
             c=color,
             s=50)
  ax.legend(targets)  
  ax.grid()
  plt.show()
  
def histogram():
  dataframe['SepalLengthCm'].plot(kind='hist')
  plt.title('Sepal Length Histogram')
  plt.xlabel('Sepal Length')
  plt.ylabel('Distribution')
  plt.show()
  dataframe['SepalWidthCm'].plot(kind='hist')
  plt.title('Sepal Width Histogram')
  plt.xlabel('Sepal Width')
  plt.ylabel('Distribution')
  plt.show()
  dataframe['PetalLengthCm'].plot(kind='hist')
  plt.title('Petal Length Histogram')
  plt.xlabel('Petal Length')
  plt.ylabel('Distribution')
  plt.show()
  dataframe['PetalWidthCm'].plot(kind='hist')
  plt.title('Petal Width Histogram')
  plt.xlabel('Petal Width')
  plt.ylabel('Distribution')
  plt.show()

frequency_graph()
pcacomponent()
histogram()
