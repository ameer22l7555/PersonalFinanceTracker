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
        
        # Use tk.Entry with explicit styling
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
            highlightbackground="#374151"
        )
        self.amount_entry.grid(row=1, column=1, sticky="ew", pady=10)
        
        # Transaction type - Row 1, Column 2-3
        ttk.Label(
            self.input_frame,
            text="Type:",
            style="TLabel",
            font=("Inter", 11)
        ).grid(row=1, column=2, sticky="w", padx=(20, 10), pady=10)
        
        # Create a custom style for the combobox
        style = ttk.Style()
        style.configure(
            "Custom.TCombobox",
            fieldbackground="#1E293B",
            background="#1E293B",
            foreground="#F9FAFB",
            arrowcolor="#F9FAFB",
            bordercolor="#374151",
            lightcolor="#1E293B",
            darkcolor="#1E293B"
        )
        
        # Transaction type dropdown
        self.transaction_type = tk.StringVar(value="Income")
        self.type_combo = ttk.Combobox(
            self.input_frame,
            textvariable=self.transaction_type,
            values=["Income", "Expense"],
            state="readonly",
            style="Custom.TCombobox",
            font=("Inter", 11),
            width=10
        )
        self.type_combo.grid(row=1, column=3, sticky="ew", pady=10)
        
        # Add button - Row 2
        self.add_button = tk.Button(
            self.input_frame,
            text="Add Transaction",
            font=("Inter", 11, "bold"),
            bg="#4F46E5",
            fg="#FFFFFF",
            activebackground="#3730A3",
            activeforeground="#FFFFFF",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.add_transaction
        )
        self.add_button.grid(row=2, column=0, columnspan=4, sticky="e", pady=(10, 0))
        
        # Bind events for visual feedback
        self.description_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.description_entry.bind("<FocusOut>", self.on_entry_focus_out)
        self.amount_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.amount_entry.bind("<FocusOut>", self.on_entry_focus_out)
        self.add_button.bind("<Enter>", self.on_button_hover)
        self.add_button.bind("<Leave>", self.on_button_leave)
    
    def on_entry_focus_in(self, event):
        """Handle entry focus in event"""
        widget = event.widget
        widget.config(highlightcolor="#6366F1", highlightthickness=2)
    
    def on_entry_focus_out(self, event):
        """Handle entry focus out event"""
        widget = event.widget
        widget.config(highlightcolor="#4F46E5", highlightthickness=1)
    
    def on_button_hover(self, event):
        """Handle button hover event"""
        self.add_button.config(bg="#3730A3")
    
    def on_button_leave(self, event):
        """Handle button leave event"""
        self.add_button.config(bg="#4F46E5")
    
    def add_transaction(self):
        """Add a new transaction"""
        # Get input values
        description = self.description_entry.get().strip()
        amount_str = self.amount_entry.get().strip()
        transaction_type = self.transaction_type.get()
        
        # Validate inputs
        if not description:
            messagebox.showerror("Input Error", "Please enter a description.")
            self.description_entry.focus_set()
            return
        
        try:
            amount = float(amount_str)
            if amount <= 0:
                messagebox.showerror("Input Error", "Amount must be greater than zero.")
                self.amount_entry.focus_set()
                return
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid amount.")
            self.amount_entry.focus_set()
            return
        
        # Create transaction object
        transaction = {
            'date': datetime.now(),
            'description': description,
            'amount': amount,
            'type': transaction_type
        }
        
        # Call the callback function
        self.on_transaction_added(transaction)
        
        # Clear inputs
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.transaction_type.set("Income")
        
        # Set focus back to description
        self.description_entry.focus_set()


class TransactionList:
    def __init__(self, parent):
        self.parent = parent
        self.transactions = []  # Store transactions for save/load functionality
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
            foreground=[('selected', '#FFFFFF')]
        )
        
        # Configure hover effect for headings
        style.map(
            "TransactionTree.Treeview.Heading",
            background=[('active', '#4F46E5')],
            foreground=[('active', '#FFFFFF')]
        )
        
        # Create the treeview with custom style
        self.tree = ttk.Treeview(
            container,
            columns=("date", "description", "type", "amount"),
            show="headings",
            style="TransactionTree.Treeview",
            height=10
        )
        
        # Configure column headings
        self.tree.heading("date", text="Date")
        self.tree.heading("description", text="Description")
        self.tree.heading("type", text="Type")
        self.tree.heading("amount", text="Amount")
        
        # Configure column widths and alignment
        self.tree.column("date", width=120, anchor="w")
        self.tree.column("description", width=300, anchor="w")
        self.tree.column("type", width=100, anchor="center")
        self.tree.column("amount", width=100, anchor="e")
        
        # Create a scrollbar
        scrollbar = ttk.Scrollbar(
            container, 
            orient="vertical", 
            command=self.tree.yview,
            style="Vertical.TScrollbar"
        )
        
        # Configure scrollbar style
        style.configure(
            "Vertical.TScrollbar",
            background="#1F2937",
            troughcolor="#111827",
            arrowcolor="#F9FAFB"
        )
        
        # Configure the treeview to use the scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack the treeview and scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Configure tags for different transaction types
        self.tree.tag_configure('income', foreground="#10B981")  # Green for income
        self.tree.tag_configure('expense', foreground="#EF4444")  # Red for expenses
        
        # Bind resize event to adjust column widths
        self.tree.bind("<Configure>", self.on_list_resize)
        
        # Show placeholder if no transactions
        self.show_placeholder()
    
    def show_placeholder(self):
        """Show placeholder message if no transactions"""
        if len(self.tree.get_children()) == 0:
            self.tree.insert(
                "", 
                "end", 
                values=("", "No transactions yet. Add a new transaction to get started.", "", "")
            )
    
    def on_list_resize(self, event):
        """Adjust column widths when the list is resized"""
        width = event.width
        self.tree.column("date", width=int(width * 0.15))
        self.tree.column("description", width=int(width * 0.45))
        self.tree.column("type", width=int(width * 0.15))
        self.tree.column("amount", width=int(width * 0.15))
    
    def add_transaction(self, transaction, update_ui=True):
        """Add a transaction to the list"""
        # Add to internal list for save/load functionality
        self.transactions.append(transaction)
        
        # Clear placeholder if this is the first transaction
        if len(self.tree.get_children()) == 1:
            item = self.tree.get_children()[0]
            if self.tree.item(item, "values")[1] == "No transactions yet. Add a new transaction to get started.":
                self.tree.delete(item)
        
        # Format the amount with currency symbol
        amount_str = f"${transaction['amount']:.2f}"
        
        # Determine tag based on transaction type
        tag = 'income' if transaction['type'] == 'Income' else 'expense'
        
        # Format date for display
        if isinstance(transaction['date'], datetime):
            date_str = transaction['date'].strftime("%b %d, %Y")
        else:
            # If date is already a string (e.g., from loaded data)
            date_str = transaction['date']
        
        # Insert with appropriate tag
        item = self.tree.insert(
            "", 
            "end", 
            values=(
                date_str,
                transaction['description'],
                transaction['type'],
                amount_str
            ),
            tags=(tag,)
        )
        
        # Scroll to show new transaction if update_ui is True
        if update_ui:
            self.tree.see(item)
    
    def clear_transactions(self):
        """Clear all transactions"""
        # Clear internal list
        self.transactions = []
        
        # Clear treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Show placeholder
        self.show_placeholder()
    
    def get_all_transactions(self):
        """Get all transactions"""
        return self.transactions