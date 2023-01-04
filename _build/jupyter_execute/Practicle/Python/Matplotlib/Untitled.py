#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as mpla

T = np.linspace(0, 2*np.pi, 100)
S = np.sin(T)

line, = plt.plot(T, S)

def animate(i):
    line.set_ydata(np.sin(T+i/50))

anim = mpla.FuncAnimation(
    plt.gcf(), animate, interval=5)

plt.show()


# In[ ]:




