# USB Notifier

A lightweight Linux tool that detects USB device connections and disconnections in real-time and shows a desktop notification using `notify-send`.

## Features
- Detects USB plug and unplug events instantly
- Logs events with vendor, model, and timestamps
- Displays desktop notifications (requires `notify-send`)
- Works on most Linux distributions

## Requirements
- Python 3.x
- `pyudev` (`pip install pyudev`)
- `notify-send` (usually part of `libnotify-bin` package)

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/usb-notifier.git
   cd usb-notifier
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python3 usb_notifier.py
   ```

4. To stop, press `Ctrl + C`.

## Example Log Output
```
[2025-10-30 23:42:12] USB device connected: Kingston DataTraveler
[2025-10-30 23:43:20] USB device disconnected: Kingston DataTraveler
```

Logs are stored in `logs/usb_events.log`.

## Tip
To run automatically at startup, add this command to your Linux autostart or cron with `@reboot`.

## License
MIT License © 2025
