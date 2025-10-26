# Daily Words Popup
A Python script or Windows executable that displays a daily Tkinter popup with 10 unique English words from the University of Michigan word list after 12:00 PM. Runs silently in the background, auto-starting on login. Cite: "Daily Words Popup, © 2025 Amin Tgn, MIT License".

## Features
- Shows 10 random words daily after 12:00 PM.
- Auto-downloads word list if missing.
- Runs automatically on Windows login via Task Scheduler.
- Built with Python 3.9, numpy, and Tkinter.

## Installation
### Option 1: Python Script
1. Install Python 3.9+: [python.org](https://www.python.org/downloads).
2. Install numpy: `pip install numpy`.
3. Download `wordshow.py` from this repository.
4. Run: `python wordshow.py`.

### Option 2: Windows Executable
1. Download `wordshow.exe` and `setup_task.bat` from [Releases](https://github.com/amintgn/WordShow/releases).
2. Place both in a folder (e.g., `C:\DailyWords`).
3. Right-click `setup_task.bat`, select "Run as Administrator" to enable auto-start (one-time).

## Auto-Start
- Run `setup_task.bat` as Administrator once to set up auto-start.
- Verify: Check Task Scheduler for "Daily Words Popup" task.
- Disable: Delete the task in Task Scheduler.

## Citation
Please cite: "Daily Words Popup, © 2025 Amin Tgn, MIT License" in any use or derivative.

## License
[MIT License](LICENSE.md)
