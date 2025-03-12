import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class TransactionInput:
    def __init__(self, parent, on_transaction_added):
        self.parent = parent
        self.on_transaction_added = on_transaction_added
        self.setup_transaction_input()
    
    def setup_transaction_input(self):
        """Create transaction input section"""
        # Create main frame
        self.input_frame = ttk.LabelFrame(self.parent, text="Add New Transaction", padding="20")
        self.input_frame.pack(fill="x", pady=(0, 20))
        
        # Create a grid layout for better organization
        self.input_frame.columnconfigure(0, weight=0)  # Label column
        self.input_frame.columnconfigure(1, weight=1)  # Input column
        self.input_frame.columnconfigure(2, weight=0)  # Type label
        self.input_frame.columnconfigure(3, weight=0)  # Type dropdown
        
        # Description input - Row 0
        ttk.Label(
            self.input_frame,
            text="Description:",
            style="TLabel",
            font=("Inter", 11)
        ).grid(row=0, column=0, sticky="w", padx=(0, 10), pady=10)
        
        # Use tk.Entry with explicit styling
        self.description_entry = tk.Entry(
            self.input_frame,
            font=("Inter", 11),
            bg="#1E293B",
            fg="#F9FAFB",
            insertbackground="#F9FAFB",
            insertwidth=2,
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightcolor="#4F46E5",
            highlightbackground="#374151"
        )
        self.description_entry.grid(row=0, column=1, columnspan=3, sticky="ew", pady=10)
        
        # Amount input - Row 1
        ttk.Label(
            self.input_frame,
            text="Amount:",
            style="TLabel",
            font=("Inter", 11)
        ).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        
        self.amount_entry = tk.Entry(
            self.input_frame,
            font=("Inter", 11),
            bg="#1E293B",
            fg="#F9FAFB",
            insertbackground="#F9FAFB",
            insertwidth=2,
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightcolor="#4F46E5",
            highlightbackground="#374151",
            width=15
        )
        self.amount_entry.grid(row=1, column=1, sticky="w", pady=10)
        
        # Transaction type - Row 1, Column 2-3
        ttk.Label(
            self.input_frame,
            text="Type:",
            style="TLabel",
            font=("Inter", 11)
        ).grid(row=1, column=2, sticky="w", padx=(20, 10), pady=10)
        
        # Use tk.OptionMenu with explicit styling
        self.type_var = tk.StringVar(value="Income")
        type_options = ["Income", "Expense"]
        
        self.type_menu = tk.OptionMenu(
            self.input_frame,
            self.type_var,
            *type_options
        )
        self.type_menu.configure(
            font=("Inter", 11),
            bg="#1E293B",
            fg="#F9FAFB",
            activebackground="#2D3748",
            activeforeground="#F9FAFB",
            highlightthickness=0,
            bd=1,
            relief="solid",
            padx=10,
            width=10
        )
        # Configure the dropdown menu style
        self.type_menu["menu"].configure(
            font=("Inter", 11),
            bg="#1E293B",
            fg="#F9FAFB",
            activebackground="#4F46E5",
            activeforeground="#F9FAFB"
        )
        self.type_menu.grid(row=1, column=3, sticky="w", pady=10)
        
        # Add button - Row 2
        self.add_button = tk.Button(
            self.input_frame,
            text="Add Transaction",
            font=("Inter", 11, "bold"),
            bg="#4F46E5",
            fg="#F9FAFB",
            activebackground="#3730A3",
            activeforeground="#F9FAFB",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            bd=0
        )
        self.add_button.grid(row=2, column=0, columnspan=4, pady=(15, 5))
        self.add_button.configure(command=self.add_transaction)
        
        # Add hover effect to button
        self.add_button.bind("<Enter>", self.on_button_hover)
        self.add_button.bind("<Leave>", self.on_button_leave)
        
        # Bind focus events to change background color
        self.description_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.description_entry.bind("<FocusOut>", self.on_entry_focus_out)
        self.amount_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.amount_entry.bind("<FocusOut>", self.on_entry_focus_out)
    
    def on_entry_focus_in(self, event):
        """Handle entry focus in"""
        event.widget.configure(
            bg="#2D3748",
            highlightcolor="#4F46E5",
            highlightthickness=2
        )
    
    def on_entry_focus_out(self, event):
        """Handle entry focus out"""
        event.widget.configure(
            bg="#1E293B",
            highlightthickness=1,
            highlightbackground="#374151"
        )
    
    def on_button_hover(self, event):
        """Handle button hover"""
        self.add_button.configure(bg="#3730A3")
    
    def on_button_leave(self, event):
        """Handle button leave"""
        self.add_button.configure(bg="#4F46E5")
    
    def add_transaction(self):
        """Add a new transaction"""
        try:
            description = self.description_entry.get().strip()
            amount_text = self.amount_entry.get().strip()
            
            if not description:
                messagebox.showerror("Error", "Please enter a description")
                self.description_entry.focus_set()
                return
                
            if not amount_text:
                messagebox.showerror("Error", "Please enter an amount")
                self.amount_entry.focus_set()
                return
            
            try:
                amount = float(amount_text)
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be greater than zero")
                    self.amount_entry.focus_set()
                    return
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for amount")
                self.amount_entry.focus_set()
                return
            
            transaction_type = self.type_var.get()
            
            # Create transaction
            transaction = {
                'date': datetime.now(),
                'description': description,
                'type': transaction_type,
                'amount': amount
            }
            
            # Call the callback
            self.on_transaction_added(transaction)
            
            # Clear inputs
            self.description_entry.delete(0, "end")
            self.amount_entry.delete(0, "end")
            self.type_var.set("Income")
            self.description_entry.focus_set()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

class TransactionList:
    def __init__(self, parent):
        self.parent = parent
        self.setup_transaction_list()
    
    def setup_transaction_list(self):
        """Create transaction list section"""
        self.list_frame = ttk.LabelFrame(self.parent, text="Transaction History", padding="20")
        self.list_frame.pack(fill="both", expand=True)
        
        # Create a container frame for the treeview and scrollbar
        container = ttk.Frame(self.list_frame)
        container.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Create custom style for the treeview
        style = ttk.Style()
        
        # Configure the Treeview
        style.configure(
            "TransactionTree.Treeview",
            background="#1F2937",
            foreground="#F9FAFB",
            fieldbackground="#1F2937",
            font=("Inter", 10),
            rowheight=40,
            borderwidth=0
        )
        
        # Configure the Treeview Headings - Use a completely different color
        style.configure(
            "TransactionTree.Treeview.Heading",
            background="#3730A3",  # Darker indigo for headers
            foreground="#FFFFFF",  # Pure white text
            font=("Inter", 11, "bold"),
            relief="raised",
            borderwidth=1,
            padding=10
        )
        
        # Configure selection colors
        style.map(
            "TransactionTree.Treeview",
            background=[('selected', '#4F46E5')],
            foreground=[('selected', '#F9FAFB')]
        )
        
        # Configure heading hover effect
        style.map(
            "TransactionTree.Treeview.Heading",
            background=[('active', '#4F46E5')],  # Brighter on hover
            foreground=[('active', '#FFFFFF')]
        )
        
        # Create treeview for transactions with custom style
        columns = ("Date", "Description", "Type", "Amount")
        self.tree = ttk.Treeview(
            container, 
            columns=columns, 
            show="headings", 
            style="TransactionTree.Treeview"
        )
        
        # Configure column headings with explicit styling
        for col in columns:
            self.tree.heading(
                col, 
                text=col,
                anchor="w" if col != "Amount" else "e"
            )
        
        # Configure column widths and alignment
        self.tree.column("Date", width=100, minwidth=100, anchor="w")
        self.tree.column("Description", width=300, minwidth=200, anchor="w")
        self.tree.column("Type", width=100, minwidth=100, anchor="w")
        self.tree.column("Amount", width=100, minwidth=100, anchor="e")
        
        # Add scrollbar with custom styling
        scrollbar = ttk.Scrollbar(
            container, 
            orient="vertical", 
            command=self.tree.yview
        )
        
        # Configure scrollbar style
        style.configure(
            "Vertical.TScrollbar",
            background="#1F2937",
            troughcolor="#111827",
            arrowcolor="#F9FAFB",
            borderwidth=0
        )
        
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack layout for better control
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Configure tag styles for income and expense
        self.tree.tag_configure('income', foreground='#10B981')
        self.tree.tag_configure('expense', foreground='#EF4444')
        
        # Add a placeholder message when empty
        self.show_placeholder()
        
        # Configure resize event for the treeview
        self.list_frame.bind('<Configure>', self.on_list_resize)
    
    def show_placeholder(self):
        """Show a placeholder message when no transactions exist"""
        # First clear any existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Add placeholder item
        self.tree.insert(
            "", 
            "end", 
            values=("", "No transactions yet. Add a new transaction to get started.", "", ""),
            tags=('placeholder',)
        )
        
        # Style the placeholder text
        self.tree.tag_configure('placeholder', foreground='#9CA3AF')
    
    def on_list_resize(self, event):
        """Handle list resize event"""
        width = event.width - 30  # Account for scrollbar and padding
        if width > 0:
            # Distribute width proportionally
            self.tree.column("Date", width=int(width * 0.15))
            self.tree.column("Description", width=int(width * 0.55))
            self.tree.column("Type", width=int(width * 0.15))
            self.tree.column("Amount", width=int(width * 0.15))
    
    def add_transaction(self, transaction):
        """Add a transaction to the list"""
        # Clear placeholder if this is the first transaction
        if len(self.tree.get_children()) == 1:
            item = self.tree.get_children()[0]
            if self.tree.item(item, "values")[1] == "No transactions yet. Add a new transaction to get started.":
                self.tree.delete(item)
        
        # Format the amount with currency symbol
        amount_str = f"${transaction['amount']:.2f}"
        
        # Determine tag based on transaction type
        tag = 'income' if transaction['type'] == 'Income' else 'expense'
        
        # Insert with appropriate tag
        item = self.tree.insert(
            "", 
            "end", 
            values=(
                transaction['date'].strftime("%b %d, %Y"),
                transaction['description'],
                transaction['type'],
                amount_str
            ),
            tags=(tag,)
        )
        
        # Scroll to show new transaction
        self.tree.see(item) 