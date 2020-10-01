import matplotlib.pyplot as plt, numpy as np
y=np.random.randn(100,100)
plt.grid(label='green')
plt.legend()
plt.xlabel('xaxis')
plt.ylabel('yaxis')

plt.hist(y)
plt.show()
