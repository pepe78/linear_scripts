import matplotlib.pyplot as plt
import numpy as np

p = np.arange(0.5, 1.0, 0.01)
pp = 3 * p * p - 2 * p * p * p
ppp = 3 * pp * pp - 2 * pp * pp * pp

pppp = p**9 + 9 * p**8 * (1-p) + 36 * p**7 * (1-p)**2 + 84 * p**6 * (1-p)**3 + 126 * p**5 * (1-p)**4

fig, ax = plt.subplots()
ax.plot(p, ppp, 'r')
ax.plot(p, pppp, 'b')

plt.show()


fig, ax = plt.subplots()
ax.plot(p, ppp-pppp, 'g')

plt.show()
