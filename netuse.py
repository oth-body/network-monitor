import time
import psutil
import datetime
import csv

prev_sent = 0
prev_recv = 0

while True:
    # Get current network usage
    net_usage = psutil.net_io_counters()
    sent = net_usage.bytes_sent
    recv = net_usage.bytes_recv

    # Calculate difference in usage from the previous iteration
    sent_diff = sent - prev_sent
    recv_diff = recv - prev_recv

    # Update the variables for the next iteration
    prev_sent = sent
    prev_recv = recv

    # Print network usage data
    print("Sent: {sent_diff/1024}KB/s, Received: {recv_diff/1024}KB/s")

    # Print 'close with Ctrl +C' every minute
    if time.time() % 3 == 0:
        print("close with Ctrl +C")

    # Sleep for 1 second before checking usage again
    time.sleep(1)
