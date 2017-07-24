import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

X = np.array([[1,2],
             [1.5, 1.8],
             [5, 8],
             [8,8],
             [1,0.6],
             [9,11]])

clf = KMeans(n_clusters=2)
clf.fit(X)
centroids = clf.cluster_centers_
label =clf.labels_
color = ["g.","r.","c.", "b.", "k.", "o."]
for i in range(len(X)):
    plt.plot(X[i][0],X[i][1], color[label[i]],markersize=10)

plt.scatter(centroids[:,0], centroids[:,1], marker='x',s=150, linewidths=5)
plt.show()
#plt.scatter(X[:,0], X[:,1], s=150, linewidths=5)
#plt.show()