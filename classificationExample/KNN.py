#Algorithm knn
#First define test and train from datasets
#Then find distance between Xtrain and Xtest
#Then find index minimum distance

import numpy as.np
class NearestNeighbour:
  def __init__(self):
    Pass
  def train(self,X,Y):
    self Xtr=X
    self Ytr=Y
  def predict(self,X):
    num_test=X_shape[0]
    Y_pred=np.zeros(num_test,dtype=self.Ytr.dtype)
    for i in xrange(num_test):
      distance=np.sum(np.abs(self.Xtr-X[i,:]),axis=1)
      min_index=np.argmin(distance)
      Y_pred[i]=self.Ytr[min_index]
   return Y_pred
  
