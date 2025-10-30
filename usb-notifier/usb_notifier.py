#!/usr/bin/env python3
import pyudev
import subprocess
from datetime import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "logs", "usb_events.log")

def log_event(event_type, device):
    vendor = device.get('ID_VENDOR', 'Unknown')
    model = device.get('ID_MODEL', 'Unknown')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"[{timestamp}] USB device {event_type}: {vendor} {model}"
    print(message)
    with open(LOG_FILE, "a") as log_file:
        log_file.write(message + "\n")
    try:
        subprocess.run(["notify-send", "USB Notifier", message], check=False)
    except FileNotFoundError:
        pass  # notify-send not installed

def monitor_usb():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('usb')
    print("USB Notifier started. Listening for USB events...\n")
    for device in iter(monitor.poll, None):
        if device.action == 'add':
            log_event("connected", device)
        elif device.action == 'remove':
            log_event("disconnected", device)

if __name__ == "__main__":
    try:
        monitor_usb()
    except KeyboardInterrupt:
        print("\nExiting USB Notifier.")
