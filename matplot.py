import matplotlib.pyplot as mt
import numpy
x=numpy.arange(0,5,0.001)
# value=[1,2,1,7,3,1]
# print([i**2 for i in value])
mt.plot([i**2 for i in x])
mt.show()