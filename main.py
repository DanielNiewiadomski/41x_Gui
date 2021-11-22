import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import graph



ani = animation.FuncAnimation(graph.fig, graph.animate, interval=500)
plt.show()
