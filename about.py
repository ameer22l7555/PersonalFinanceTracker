import tkinter as tk
from tkinter import ttk

class AboutWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("About Personal Finance Tracker")
        
        # Set window size and position
        window_width = 500
        window_height = 450
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Configure dark theme colors
        self.colors = {
            'bg': '#1e1e1e',
            'secondary': '#252526',
            'text': '#ffffff',
            'accent': '#007acc',
            'border': '#404040'
        }
        
        self.window.configure(bg=self.colors['bg'])
        
        # Create main frame with border effect
        outer_frame = tk.Frame(self.window, bg=self.colors['border'], padx=1, pady=1)
        outer_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        main_frame = tk.Frame(outer_frame, bg=self.colors['bg'], padx=25, pady=25)
        main_frame.pack(fill="both", expand=True)
        
        # Logo or icon placeholder
        logo_frame = tk.Frame(main_frame, bg=self.colors['bg'], height=60)
        logo_frame.pack(fill="x", pady=(0, 20))
        logo_frame.pack_propagate(False)
        
        logo_label = tk.Label(
            logo_frame,
            text="💰",  # Unicode money bag emoji
            font=("Segoe UI", 32),
            fg=self.colors['accent'],
            bg=self.colors['bg']
        )
        logo_label.pack(expand=True)
        
        # App title with underline effect
        title_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        title_frame.pack(fill="x", pady=(0, 5))
        
        title_label = tk.Label(
            title_frame,
            text="Personal Finance Tracker",
            font=("Segoe UI", 24, "bold"),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        title_label.pack()
        
        # Underline
        underline = tk.Frame(title_frame, height=2, bg=self.colors['accent'])
        underline.pack(fill="x", pady=(5, 0))
        
        # Version info
        version_label = tk.Label(
            main_frame,
            text="Version 1.0.0",
            font=("Segoe UI", 12),
            fg=self.colors['accent'],
            bg=self.colors['bg']
        )
        version_label.pack(pady=(10, 20))
        
        # Description in a scrolled frame
        desc_frame = tk.Frame(main_frame, bg=self.colors['secondary'], padx=15, pady=15)
        desc_frame.pack(fill="both", expand=True)
        
        description = """Personal Finance Tracker is a powerful tool designed to help you manage your finances effectively. Track your income and expenses, visualize your financial data, and make informed decisions about your money.

Features:
• Income and expense tracking with detailed history
• Visual financial analytics with interactive charts
• Advanced transaction search functionality
• Secure data persistence with CSV export
• Professional dark theme interface
• Real-time balance calculations
• Customizable categories

Created by: Your Name
Contact: your.email@example.com
Website: www.yourwebsite.com"""
        
        desc_label = tk.Label(
            desc_frame,
            text=description,
            font=("Segoe UI", 11),
            fg=self.colors['text'],
            bg=self.colors['secondary'],
            justify="left",
            wraplength=400,
            padx=10,
            pady=10
        )
        desc_label.pack()
        
        # Button frame with gradient effect
        button_frame = tk.Frame(main_frame, bg=self.colors['bg'], height=50)
        button_frame.pack(fill="x", pady=(20, 0))
        
        # Configure style for the button
        style = ttk.Style()
        style.configure(
            "Accent.TButton",
            font=("Segoe UI", 11),
            padding=10
        )
        
        # Close button
        close_button = ttk.Button(
            button_frame,
            text="Close",
            command=self.window.destroy,
            style="Accent.TButton"
        )
        close_button.pack()
        
        # Make window modal
        self.window.transient()
        self.window.grab_set()
        self.window.focus_set()
        
        # Prevent window resize
        self.window.resizable(False, False) 