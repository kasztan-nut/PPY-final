import tkinter as tk
from tkinter import ttk


class Help:
    """
    A class to display the help information for the calculator.

    Attributes:
        legend_text (str): The text containing the legend information.

    Methods:
        show_help(): Opens a help window displaying the legend information.

    """
    def __init__(self):
        """
        Constructs a new Help instance.

        Initializes the legend text containing the button names and descriptions
        of what they do.

        """

        self.legend_text = '''
        Button:Action performed
        OFF:Close calculator
        C:Clear
        Del:Delete the last character
        [0-9]:Number input
        .:Input the decimal point
        +:Addition
        -:Subtraction
        *:Multiplication
        /:Division
        =:Perform calculation
        +/-:Change the sign
        %:Calculate the percentage
        x^y:Raise to power
        x!:Factorial
        1/x:Reciprocal
        mod:Modulo
        √:Square root
        MC:Memory clear
        M+:Add to memory
        M-:Subtract from memory
        '''

    def show_help(self):
        """
       Opens a help window displaying the legend information.

       This method creates a new window and populates it with a table displaying the legend information
        """
        help_window = tk.Toplevel()
        help_window.title("Help")
        help_window.resizable(width=False, height=False)

        legend_lines = self.legend_text.strip().split('\n')
        num_rows = len(legend_lines)
        num_cols = len(legend_lines[0].split(':'))

        # Create a Table widget to display the data
        table = ttk.Treeview(help_window, columns=list(range(num_cols)), show='headings')

        # Add column headings
        for j in range(num_cols):
            table.heading(j, text=legend_lines[0].split(':')[j])

        # Add data to table
        for i in range(1, num_rows):
            line_parts = legend_lines[i].split(':')
            table.insert('', tk.END, values=line_parts)

        table.column(0, width=100)
        table.column(1, width=200)
        table.configure(padding=(0, 0, 0, 10))

        table.pack()
