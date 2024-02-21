import numpy as np
from scipy.misc import derivative

def f(x):
    R = 5
    L = 10
    array_matrix = np.array([x,x*R/L*np.cos(360),x*R/L*np.sin(360)])
    return array_matrix
x= np.linspace(0,10,20)
derv = derivative(f,x,dx=1e-6)
print(derv)