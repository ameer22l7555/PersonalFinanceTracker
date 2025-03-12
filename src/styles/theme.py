from tkinter import ttk

class AppTheme:
    def __init__(self):
        self.colors = {
            'primary': '#4F46E5',      # Professional indigo
            'secondary': '#3730A3',     # Darker indigo
            'accent': '#0EA5E9',        # Professional blue
            'warning': '#EF4444',       # Professional red
            'success': '#10B981',       # Professional green
            'background': '#111827',    # Rich dark background
            'card_bg': '#1F2937',       # Professional dark card
            'text': '#F9FAFB',          # Crisp white text
            'text_secondary': '#9CA3AF', # Professional gray
            'border': '#374151',        # Professional border
            'hover': '#2D3748',         # Subtle hover
            'input_bg': '#1E293B',      # Lighter input background for better contrast
            'chart_grid': '#374151',    # Professional grid
            'chart_bg': '#1F2937',      # Chart background
            'income_color': '#10B981',  # Professional green
            'expense_color': '#EF4444', # Professional red
            'pie_colors': ['#4F46E5', '#0EA5E9', '#10B981', '#EF4444', '#F59E0B'] # Professional palette
        }
    
    def setup_styles(self, style):
        """Configure custom styles for widgets"""
        # Configure fonts
        default_font = ("Inter", 10)
        header_font = ("Inter", 28, "bold")
        balance_font = ("Inter", 22, "bold")
        
        # Main frame style
        style.configure(
            "Main.TFrame",
            background=self.colors['background']
        )
        
        # Card style
        style.configure(
            "Card.TFrame",
            background=self.colors['card_bg']
        )
        
        # LabelFrame style
        style.configure(
            "TLabelframe",
            background=self.colors['card_bg'],
            bordercolor=self.colors['border']
        )
        
        style.configure(
            "TLabelframe.Label",
            font=("Inter", 13, "bold"),
            foreground=self.colors['text'],
            background=self.colors['card_bg']
        )
        
        # Header style
        style.configure(
            "Header.TLabel",
            font=header_font,
            foreground=self.colors['text'],
            background=self.colors['background']
        )
        
        # Balance section styles
        style.configure(
            "Balance.TLabel",
            font=balance_font,
            foreground=self.colors['text'],
            background=self.colors['card_bg']
        )
        
        style.configure(
            "PositiveBalance.TLabel",
            font=balance_font,
            foreground=self.colors['success'],
            background=self.colors['card_bg']
        )
        
        style.configure(
            "NegativeBalance.TLabel",
            font=balance_font,
            foreground=self.colors['warning'],
            background=self.colors['card_bg']
        )
        
        # Button styles
        style.configure(
            "Action.TButton",
            font=("Inter", 11, "bold"),
            background=self.colors['primary'],
            foreground=self.colors['text'],
            padding=(15, 8)
        )
        
        style.map(
            "Action.TButton",
            background=[('active', self.colors['secondary'])],
            foreground=[('active', self.colors['text'])]
        )
        
        # Treeview styles
        style.configure(
            "Treeview",
            font=("Inter", 10),
            rowheight=40,
            background=self.colors['card_bg'],
            foreground=self.colors['text'],
            fieldbackground=self.colors['card_bg'],
            borderwidth=1,
            relief="solid"
        )
        
        style.configure(
            "Treeview.Heading",
            font=("Inter", 11, "bold"),
            background=self.colors['background'],
            foreground=self.colors['text'],
            relief="flat",
            borderwidth=0,
            padding=10
        )
        
        style.map(
            "Treeview",
            background=[('selected', self.colors['primary'])],
            foreground=[('selected', self.colors['text'])]
        )
        
        style.map(
            "Treeview.Heading",
            background=[('active', self.colors['hover'])]
        )
        
        # Entry styles
        style.configure(
            "TEntry",
            font=("Inter", 11),
            background=self.colors['input_bg'],
            foreground=self.colors['text'],
            fieldbackground=self.colors['input_bg'],
            insertcolor=self.colors['text'],
            insertwidth=2,
            padding=8,
            borderwidth=1,
            relief="solid"
        )
        
        style.map(
            "TEntry",
            fieldbackground=[
                ('readonly', self.colors['input_bg']),
                ('disabled', self.colors['input_bg']),
                ('focus', self.colors['input_bg'])
            ],
            foreground=[
                ('readonly', self.colors['text']),
                ('disabled', self.colors['text_secondary']),
                ('focus', self.colors['text'])
            ],
            bordercolor=[('focus', self.colors['primary'])]
        )
        
        # Combobox styles (for dropdown)
        style.configure(
            "TCombobox",
            font=("Inter", 11),
            background=self.colors['input_bg'],
            foreground=self.colors['text'],
            fieldbackground=self.colors['input_bg'],
            arrowcolor=self.colors['text'],
            padding=8,
            borderwidth=1,
            relief="solid"
        )
        
        style.map(
            "TCombobox",
            fieldbackground=[
                ('readonly', self.colors['input_bg']),
                ('disabled', self.colors['input_bg']),
                ('focus', self.colors['input_bg'])
            ],
            foreground=[
                ('readonly', self.colors['text']),
                ('disabled', self.colors['text_secondary']),
                ('focus', self.colors['text'])
            ],
            bordercolor=[('focus', self.colors['primary'])]
        )
        
        # Loading bar style
        style.configure(
            "Loading.Horizontal.TProgressbar",
            troughcolor=self.colors['background'],
            background=self.colors['primary'],
            bordercolor=self.colors['border'],
            lightcolor=self.colors['primary'],
            darkcolor=self.colors['secondary']
        ) 