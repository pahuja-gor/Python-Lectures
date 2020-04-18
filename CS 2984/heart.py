# -*- coding: utf-8 -*-
"""
This program draws a heart using MatPlotLib.

You don't have to worry about how it does it, just make sure that it runs.
If it's successful, a heart will appear in the upper-right (or lower-right
if you enable inline plotting).
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm


cmap = ListedColormap(['r', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)

t = np.arange(0,2*np.pi, 0.1)
x = 16*np.sin(t)**3
y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)

plt.xkcd()
plt.plot(x,y, c='r')
plt.show()