import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.ma.core import concatenate
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom
from pylab import bone , pcolor , colorbar , plot , show

#Importing dataset
dataset = pd.read_csv('Credit_Card_Applications.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#Feature scaling
sc = MinMaxScaler(feature_range=(0, 1))
x = sc.fit_transform(x)

#Training the SOM
som = MiniSom(x = 10 , y = 10 , input_len= 15 , sigma = 1 , learning_rate = 0.5)
som.random_weights_init(x)
som.train_random(data = x , num_iteration = 100)

#Visualizing the results
bone()
pcolor(som.distance_map().T)
colorbar()
markers = ['o', 's']
colors = ['r', 'g']
for i, x_val in enumerate(x):
    w = som.winner(x_val)
    plot(w[0] + 0.5 , w[1] + 0.5 , markers[y[i]], markeredgecolor = colors[y[i]] , markerfacecolor = 'None', markersize = 10 , markeredgewidth = 2 )
show()

#Finding the frauds
mappings = som.win_map(x)
frauds = np.concatenate((mappings[(8,1)], mappings[(6,8)]) , axis = 0)
frauds = sc.inverse_transform(frauds)