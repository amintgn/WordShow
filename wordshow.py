# -*- coding: utf-8 -*-
"""
Daily Random Words Popup
- Selects 10 random words from Uni Michigan word list daily.
- Shows a popup window after 12:00 PM each day.
- Handles missed days by showing on next run after noon.
- Runs continuously in the background.

BY: Amin Tgn
"""

import numpy as np
import tkinter as tk
from tkinter import scrolledtext
import datetime
import time
import sys
import os
import urllib.request

# Function to download wordlist.txt if not present
def download_wordlist(url="https://www-personal.umich.edu/~jlawler/wordlist", filename="wordlist.txt"):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
            print(f"Downloaded {filename} successfully.")
        except Exception as e:
            print(f"Error downloading wordlist: {e}", file=sys.stderr)
            sys.exit(1)

# Function to get 10 random words from wordlist.txt
def get_daily_words(word_file='wordlist.txt'):
    try:
        with open(word_file, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip() and len(line.strip()) >= 3 and line.strip().isalpha()]
        if not words:
            print("Error: No valid words found in wordlist.txt.", file=sys.stderr)
            return None
        return np.random.choice(words, size=10, replace=False).tolist()
    except Exception as e:
        print(f"Error reading wordlist.txt: {e}", file=sys.stderr)
        return None

# Function to show popup with words
def show_words_popup(words):
    root = tk.Tk()
    root.title("Today's 10 Random Words")
    root.geometry("400x300")
    root.resizable(False, False)

    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (400 // 2)
    y = (root.winfo_screenheight() // 2) - (300 // 2)
    root.geometry(f"400x300+{x}+{y}")

    tk.Label(root, text="Your daily vocabulary words:", font=("Arial", 12, "bold")).pack(pady=10)
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15, font=("Arial", 10))
    for i, word in enumerate(words, 1):
        text_area.insert(tk.END, f"{i}. {word}\n")
    text_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
    text_area.config(state=tk.DISABLED)
    tk.Button(root, text="Close", command=root.destroy, font=("Arial", 10)).pack(pady=10)
    root.grab_set()
    root.wait_window(root)

# Main loop
def main():
    print("Daily Words Popup started. Running in background...")
    print("Waiting for 12:00 PM to show today's words.")
    print("Press Ctrl+C to stop.")

    shown_today = False
    last_date = None

    try:
        while True:
            now = datetime.datetime.now()
            current_date = now.date()

            if current_date != last_date:
                shown_today = False
                last_date = current_date

            if now.hour >= 12 and not shown_today:
                words = get_daily_words()
                if words:
                    show_words_popup(words)
                    shown_today = True
                    print(f"Words shown for {current_date} at {now.strftime('%H:%M:%S')}")

            time.sleep(60)

    except KeyboardInterrupt:
        print("\nDaily Words Popup stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)

if __name__ == "__main__":
    download_wordlist()
    if not os.path.exists('wordlist.txt'):
        print("Error: wordlist.txt not found and could not be downloaded.", file=sys.stderr)
        sys.exit(1)
    main()