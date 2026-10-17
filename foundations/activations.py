import numpy as np
from numpy.typing import NDArray
import math


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        sig_sol = []
        for i in range(len(z)):
            sig = 1 / (1 + math.exp(-z[i]))
            sig_sol.append(sig)
        sig_sol = np.round(sig_sol, 5)
        return sig_sol
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        relu_sol = []
        for i in range(len(z)):
            if z[i] < 0:
                relu_sol.append(0.0)
            else:
                relu_sol.append(z[i])
        pass
        relu_sol = np.round(relu_sol, 5)
        return relu_sol