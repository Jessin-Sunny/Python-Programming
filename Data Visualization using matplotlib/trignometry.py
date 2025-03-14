from matplotlib import pyplot as plt
import math
import numpy as np

x = np.arange(0, math.pi*2, 0.05)
plt.plot(x, np.sin(x), 'r--', label='sin(x)')
plt.plot(x, np.cos(x), 'g--', label='cos(x)')
#plt.plot(x, np.tan(x), 'b--')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Values')
plt.legend(loc='upper right')
plt.title('Sine & Cosine Waves')
plt.show()
