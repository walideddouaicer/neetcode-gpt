import numpy as np
from numpy.typing import NDArray
from math import *

class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        maximum = max(z)
        softmax_solution = []
        for i in range(len(z)):
            gamma =  exp(z[i]-maximum)/sum(exp(x-maximum) for x in z)
            softmax_solution.append(gamma)
        rounded_softmax_solution =[round(x, 4) for x in softmax_solution]
        return rounded_softmax_solution
        pass
