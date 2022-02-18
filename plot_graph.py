from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import paramiko

plt.style.use('fivethirtyeight')
# refresh time, in secs
interval = 500

plot_style='line'

HOST="localhost"
PORT=2522
USERNAME="root"
ID_RSA_FILE="/home/diego/.ssh/id_rsa"
LOGFILE="/root/logfile.txt"

sftp_key = paramiko.RSAKey.from_private_key_file(ID_RSA_FILE)
transport = paramiko.Transport((HOST, PORT))
transport.start_client(event=None, timeout=15)
transport.get_remote_server_key()
transport.auth_publickey(username=USERNAME, key=sftp_key)
sftp = paramiko.SFTPClient.from_transport(transport) 

xs = []
y1s = []
y2s = []
fig, (ax1, ax2) = plt.subplots(2)

# index = count()


def animate(i, xs:list, y1s:list, y2s:list):
    #data = pd.read_csv('logfile.txt', delimiter = ';', comment = '#')
    with sftp.open(LOGFILE, mode='r') as f:
        f.prefetch()
        data = pd.read_csv(f, delimiter = ';', comment = '#')
        x = data['x_value']
        y1 = data['sw_latency']
        y1 = [y for y in y1 if y != 0]
        y2 = data['hw_latency']
        y2 = [y for y in y2 if y != 0]

        plt.cla()
        # Limit x and y lists to 20 items
        xs = x[-20:]
        y1s = y1[-20:]
        y2s = y2[-20:]
        ax1.clear()
        ax2.clear()
        fig.suptitle('Fast Intercept Demonstration: RTT Latency')
        # Draw x and y lists
        if (plot_style == 'bar'):
            ax1.bar(xs, y1s, label='SW Latency', color='blue')
            ax2.bar(xs, y2s, label='HW Latency', color='red')
        else:
            ax1.plot(xs, y1s, label='SW Latency', color='blue')
            ax2.plot(xs, y2s, label='HW Latency', color='red')

        ax1.legend(loc='upper left')
        ax2.legend(loc='upper left')

        plt.xticks(rotation=45, ha='right')
        plt.ylabel('Latency (µs)')
        
        plt.tight_layout()


ani1 = FuncAnimation(plt.gcf(), animate, fargs=(xs,y1s,y2s), interval=interval)

plt.tight_layout()
plt.show()