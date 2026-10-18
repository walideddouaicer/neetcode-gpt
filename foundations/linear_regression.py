import numpy as np
from numpy.typing import NDArray

class Solution:

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        model_prediciton = []
        model_prediciton = np.dot(X, weights)
        model_prediciton  = [round(i, 5) for i in model_prediciton ]
        return model_prediciton 
       

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        alpha = 0
        for i in range(len(model_prediction)):
            alpha += (model_prediction[i] - ground_truth[i]) ** 2  
        error = np.mean(alpha)
        error = error/len(model_prediction)
        error = round(error, 5)
        return error
        
