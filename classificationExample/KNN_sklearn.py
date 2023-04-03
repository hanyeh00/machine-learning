from packaging import version
import sklearn

assert version.parse(sklearn.__version__) >= version.parse("1.0.2")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

#DataLoad

#download data:
import urllib.request
data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

#
lifesat.loc[lifesat['Country']=="Turkey"]
#plot

lifesat.plot(kind="scatter",x='GDP per capita (USD)'
             ,y='Life satisfaction'
             )
plt.show()

#plot with 

lifesat.plot(kind="scatter",x='GDP per capita (USD)'
             ,y='Life satisfaction'
             )
plt.axis([23_500,62_500,4,9])
plt.show()



model2=KNeighborsRegressor()
model2.fit(X,y)

y_pred=model2.predict(X)

#test our model
X_new=[[27287.08]]
print(model2.kneighbors(X_new))

#validation
from sklearn.metrics import mean_squared_error


mean_squared_error(y,Y_pred)

