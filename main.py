import tkinter as tk
from modules.ui import SecurityUI
from modules.capture import start_capture, stop_event
import ctypes
import sys
import threading

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def on_closing(root, capture_thread):
    """Handle UI window close event."""
    stop_event.set()  # Signal all monitoring threads to stop
    root.destroy()    # Close the Tkinter window
    if capture_thread and capture_thread.is_alive():
        capture_thread.join(timeout=2)  # Wait up to 2 seconds for thread to finish
    print("Security Event Recorder stopped.")

def main():
    if not is_admin():
        print("Please run as administrator for full functionality")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    # Start capture in a thread
    capture_thread = threading.Thread(target=start_capture)
    capture_thread.daemon = True
    capture_thread.start()

    # Start UI in the main thread
    root = tk.Tk()
    app = SecurityUI(root)
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, capture_thread))
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        on_closing(root, capture_thread)

if __name__ == "__main__":
    main()