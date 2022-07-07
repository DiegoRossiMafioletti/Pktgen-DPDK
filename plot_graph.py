#!/usr/bin/python3

from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
# import cv2
from matplotlib.animation import FuncAnimation
import paramiko

plt_style='fivethirtyeight'
#plt_style='fast'

# remote/local
plt_mode='remote'

plt.style.use(plt_style)
# refresh time, in secs
interval = 1000

# img = cv2.imread('testbed.png') 
# cv2.imshow('Testbed', img)

plot_style='line'

LOGFILE="/tmp/logfile.txt"
if (plt_mode == 'remote'):
    HOST="localhost"
    PORT=2522
    USERNAME="root"
    ID_RSA_FILE="/home/diego/.ssh/id_rsa"

    # SSH connection: remote testbed
    sftp_key = paramiko.RSAKey.from_private_key_file(ID_RSA_FILE)
    transport = paramiko.Transport((HOST, PORT))
    transport.start_client(event=None, timeout=15)
    transport.get_remote_server_key()
    transport.auth_publickey(username=USERNAME, key=sftp_key)
    sftp = paramiko.SFTPClient.from_transport(transport) 

xs = []
y1s = []
y2s = []
fig, (ax1, ax2) = plt.subplots(2, figsize=(10, 5))

# index = count()


def animate(i, xs:list, y1s:list, y2s:list):
    if (plt_mode == 'local'):
        data = pd.read_csv(LOGFILE, delimiter = ';', comment = '#')
    elif (plt_mode == 'remote'):
        with sftp.open(LOGFILE, mode='r') as f:
            f.prefetch()
            data = pd.read_csv(f, delimiter = ';', comment = '#')

    x = data['x_value']
    y1 = data['sw_latency']
    # y1 = [y for y in y1 if y != 0]
    y2 = data['hw_latency']
    # y2 = [y for y in y2 if y != 0]

    plt.cla()
    # Limit x and y lists to 10 items
    xs = x[-10:]
    y1s = y1[-10:]
    y2s = y2[-10:]

    if (len(y1s) < 10 or len(y2s) < 10):
        return

    ax1.clear()
    ax2.clear()
    fig.suptitle('Fast Intercept Demonstration: RTT Latency')
    # Draw x and y lists
    if (plot_style == 'bar'):
        ax1.bar(xs, y1s, label='SW Latency', color='blue')
        ax2.bar(xs, y2s, label='HW Latency', color='red')
    else:
        ax1.plot(xs, y1s, label='SW Latency', color='blue', marker='o')
        ax2.plot(xs, y2s, label='HW Latency', color='red', marker='o')

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper left')

    # ax1.set_ylim(bottom=0)
    # ax2.set_ylim(bottom=0)

    # plt.xticks(rotation=45, ha='right')
    plt.ylabel('Latency (µs)')
    plt.xlabel('Sample number')
    plt.tight_layout()

ani1 = FuncAnimation(plt.gcf(), animate, fargs=(xs,y1s,y2s), interval=interval)
plt.tight_layout()
plt.show()
