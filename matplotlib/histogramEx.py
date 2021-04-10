import matplotlib.pyplot as plt, numpy


y = numpy.random.randn(5,5)
plt.hist(y)
plt.grid(True)
plt.show()
