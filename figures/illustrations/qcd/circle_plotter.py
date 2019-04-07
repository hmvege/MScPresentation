import matplotlib.pyplot as plt
import numpy as np

N = 100
theta = np.linspace(0, 2*np.pi, N)
x = np.cos(theta)*0.5
y = np.sin(theta)*0.5

x1 = np.cos(theta)*0.5*np.exp(np.cos(theta))
y1 = np.sin(theta)*0.5

fig = plt.figure()

ax = fig.add_subplot(111)

ax.plot(x, y, zorder=0)
ax.plot(x1, y1, zorder=0)
n_arr_pos = 20
ax.arrow(x[n_arr_pos], y[n_arr_pos], np.cos(theta[n_arr_pos+2]+np.pi/2)*1e-4,
         np.sin(theta[n_arr_pos+2]+np.pi/2)*1e-4, head_width=0.08, fill=False, zorder=1,
         edgecolor="black", shape="full", overhang=1.0)

ax.axis("square")
plt.show()
