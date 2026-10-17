import numpy as np
from numpy.typing import NDArray
import math

class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        if len(y_true) == len(y_pred):
            loss = 0
            eps = 1e-7
            for i in range(len(y_true)):
                if y_pred[i] == 0 and y_true[i] == 0:
                    loss += 0
                elif y_pred[i] == 1 and y_true[i] == 1:
                    loss += 0
                else:
                   p = min(max(y_pred[i], eps), 1 - eps)
                   loss += y_true[i] * math.log(p) + (1-y_true[i]) * math.log(1 - p)
            loss = loss * (-1/len(y_true))
            loss = round(loss, 4) + 0.0
           
        return loss
        
        
        
        
        
    

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
       sum1 = 0
       eps = 1e-7
       for i in range(len(y_true)):
        for j in range(len(y_true[i])):
            if y_true[i][j] == 1:
                if y_pred[i][j] == 0:
                    sum1 = sum1 + math.log(eps)

                else:
                   sum1 = sum1 + math.log(y_pred[i][j])
       loss = -(1/len(y_true)) * sum1
       loss = round(loss, 4) + 0.0
       return loss