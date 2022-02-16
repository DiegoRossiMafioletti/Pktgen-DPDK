from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
# refresh time, in secs
interval = 1000

xs = []
y1s = []
fig, ax = plt.subplots()

# index = count()


def animate(i, xs:list, y1s:list):
    data = pd.read_csv('logfile.txt', delimiter = ';', comment = '#')
    x = data['x_value']
    y1 = data['sw_latency']
    #y2 = data['hw_latency']

    plt.cla()
    # Limit x and y lists to 20 items
    xs = x[-20:]
    y1s = y1[-20:]
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, y1s, label='SW Latency')

    plt.xticks(rotation=45, ha='right')
    #plt.ylim([2000,2500])
    #plt.plot(x, y1, label='SW Latency')
    #plt.plot(x, y2, label='HW Latency')
    
    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, fargs=(xs,y1s), interval=interval)

plt.tight_layout()
plt.show()