import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

class FinancialCharts:
    def __init__(self, parent, colors):
        self.colors = colors
        self.setup_charts(parent)
    
    def setup_charts(self, parent):
        """Setup charts section"""
        self.charts_frame = ttk.LabelFrame(parent, text="Financial Overview", padding="20")
        self.charts_frame.pack(fill="both", expand=True)
        
        # Create figure for matplotlib with professional dark theme
        self.fig, (self.pie_ax, self.bar_ax) = plt.subplots(2, 1, figsize=(8, 10), dpi=100)
        self.fig.patch.set_facecolor(self.colors['card_bg'])
        
        # Style the charts
        plt.style.use('dark_background')
        
        # Professional styling configuration
        plt.rcParams.update({
            'font.family': 'Inter',
            'font.size': 11,
            'axes.labelsize': 12,
            'axes.titlesize': 14,
            'axes.facecolor': self.colors['card_bg'],
            'axes.edgecolor': self.colors['border'],
            'axes.labelcolor': self.colors['text'],
            'axes.grid': True,
            'grid.color': self.colors['chart_grid'],
            'grid.alpha': 0.1,
            'xtick.color': self.colors['text_secondary'],
            'ytick.color': self.colors['text_secondary'],
            'figure.constrained_layout.use': True
        })
        
        # Create canvas with higher DPI for sharper rendering
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.charts_frame)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Configure resize event
        self.charts_frame.bind('<Configure>', self.on_resize)
        
        # Initial empty charts
        self.update_charts([])
    
    def on_resize(self, event):
        """Handle resize event"""
        w, h = event.width - 50, event.height - 50  # Increased padding
        if w > 0 and h > 0:
            self.fig.set_size_inches(w/100, h/100)  # Adjusted for higher DPI
            self.canvas.draw()
    
    def update_charts(self, transactions):
        """Update the charts with current data"""
        # Calculate totals from transactions
        total_income = 0
        total_expenses = 0
        
        for transaction in transactions:
            if transaction['type'] == 'Income':
                total_income += transaction['amount']
            else:
                total_expenses += transaction['amount']
        
        # Clear previous charts
        self.pie_ax.clear()
        self.bar_ax.clear()
        
        # Set background color
        self.pie_ax.set_facecolor(self.colors['card_bg'])
        self.bar_ax.set_facecolor(self.colors['card_bg'])
        
        # Pie chart for Income vs Expenses
        labels = ['Income', 'Expenses']
        sizes = [total_income, total_expenses]
        colors = [self.colors['success'], self.colors['warning']]
        
        # Check if we have any data
        if total_income == 0 and total_expenses == 0:
            self.pie_ax.text(0.5, 0.5, 'No transaction data available',
                           horizontalalignment='center',
                           verticalalignment='center',
                           transform=self.pie_ax.transAxes,
                           fontsize=12,
                           color=self.colors['text_secondary'],
                           style='italic')
        else:
            wedges, texts, autotexts = self.pie_ax.pie(
                sizes, 
                labels=labels, 
                colors=colors,
                autopct='%1.1f%%', 
                startangle=90,
                textprops={'color': self.colors['text'], 'fontsize': 11},
                wedgeprops={'edgecolor': self.colors['card_bg'], 
                           'linewidth': 2,
                           'antialiased': True}
            )
            
            # Enhance percentage labels
            plt.setp(autotexts, color=self.colors['text'], 
                    weight='bold', fontsize=11)
            plt.setp(texts, fontsize=12)
        
        self.pie_ax.set_title('Income vs Expenses Distribution',
                             pad=20,
                             fontsize=14,
                             color=self.colors['text'],
                             fontweight='bold')
        
        # Bar chart for recent transactions
        recent_dates = []
        recent_amounts = []
        
        # Get the 5 most recent transactions
        recent_transactions = transactions[-5:] if len(transactions) > 0 else []
        
        for transaction in recent_transactions:
            # Handle both datetime objects and string dates
            if hasattr(transaction['date'], 'strftime'):
                date_str = transaction['date'].strftime("%b %d")
            else:
                # If date is already a string (e.g., from loaded data)
                date_str = transaction['date']
                if len(date_str) > 6:  # If it's a full date string, try to shorten it
                    try:
                        from datetime import datetime
                        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                        date_str = date_obj.strftime("%b %d")
                    except:
                        # If parsing fails, just use the first 6 chars
                        date_str = date_str[:6]
            
            recent_dates.append(date_str)
            amount = transaction['amount']
            if transaction['type'] == 'Expense':
                amount = -amount
            recent_amounts.append(amount)
        
        if recent_dates:
            bars = self.bar_ax.bar(recent_dates, recent_amounts,
                                 width=0.7,  # Slightly thinner bars
                                 alpha=0.9)  # More solid bars
            
            for bar in bars:
                height = bar.get_height()
                if height >= 0:
                    bar.set_color(self.colors['success'])
                else:
                    bar.set_color(self.colors['warning'])
                
                # Enhanced value labels
                self.bar_ax.text(
                    bar.get_x() + bar.get_width()/2.,
                    height,
                    f'${abs(height):,.0f}',  # Added thousands separator
                    ha='center',
                    va='bottom' if height >= 0 else 'top',
                    color=self.colors['text'],
                    fontsize=10,
                    fontweight='bold'
                )
        else:
            self.bar_ax.text(0.5, 0.5, 'No recent transaction data available',
                           horizontalalignment='center',
                           verticalalignment='center',
                           transform=self.bar_ax.transAxes,
                           fontsize=12,
                           color=self.colors['text_secondary'],
                           style='italic')
        
        self.bar_ax.set_title('Recent Transaction History',
                             pad=20,
                             fontsize=14,
                             color=self.colors['text'],
                             fontweight='bold')
        
        # Enhanced bar chart styling
        self.bar_ax.spines['top'].set_visible(False)
        self.bar_ax.spines['right'].set_visible(False)
        self.bar_ax.spines['bottom'].set_color(self.colors['border'])
        self.bar_ax.spines['left'].set_color(self.colors['border'])
        
        # Refined grid
        self.bar_ax.grid(True, axis='y', linestyle='--', 
                        alpha=0.15, color=self.colors['chart_grid'])
        
        # Adjust tick labels
        self.bar_ax.tick_params(axis='x', rotation=0)
        self.bar_ax.tick_params(axis='both', length=0)
        
        # Update the canvas with proper spacing
        self.fig.set_constrained_layout(True)
        self.canvas.draw() 