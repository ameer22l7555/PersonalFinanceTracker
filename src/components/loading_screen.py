import tkinter as tk
from tkinter import ttk
import time

class LoadingScreen:
    def __init__(self, root):
        self.root = root
        self.loading_window = tk.Toplevel(root)
        self.loading_window.overrideredirect(True)
        self.loading_window.attributes('-topmost', True)
        
        # Center the loading window
        window_width = 400
        window_height = 250
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.loading_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Configure loading window background
        self.loading_window.configure(bg='#1a237e')  # Deep blue background
        
        # Create frame for content
        content_frame = tk.Frame(self.loading_window, bg='#1a237e')
        content_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Loading text with professional font
        self.loading_label = tk.Label(
            content_frame,
            text="Personal Finance Tracker",
            font=("Segoe UI", 20, "bold"),
            fg='#ffffff',
            bg='#1a237e'
        )
        self.loading_label.pack(pady=(0, 20))
        
        # Loading message
        self.status_label = tk.Label(
            content_frame,
            text="Initializing...",
            font=("Segoe UI", 12),
            fg='#90caf9',  # Light blue text
            bg='#1a237e'
        )
        self.status_label.pack(pady=(0, 20))
        
        # Progress bar with custom style
        self.progress = ttk.Progressbar(
            content_frame,
            length=300,
            mode='determinate',
            style="Loading.Horizontal.TProgressbar"
        )
        self.progress.pack()
        
        # Start progress animation
        self.animate_progress()
    
    def animate_progress(self):
        status_messages = [
            "Loading components...",
            "Preparing interface...",
            "Setting up charts...",
            "Almost ready..."
        ]
        
        for i in range(101):
            self.progress['value'] = i
            if i % 25 == 0 and i//25 < len(status_messages):
                self.status_label.config(text=status_messages[i//25])
            self.loading_window.update()
            time.sleep(0.02)
        self.loading_window.destroy() 