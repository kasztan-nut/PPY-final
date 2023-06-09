import math
import tkinter as tk
from tkinter import messagebox
from help import Help


class Calculator:
    """
    A simple calculator application with basic arithmetic operations.

    Attributes:
        root (tkinter.Tk): The main window of the calculator.
        entry (tkinter.Entry): The input/output field for displaying and entering numbers.
        expression (str): The current mathematical expression being evaluated.
        result (str): The result of the evaluated expression.
        memory (str): The memory storage for arithmetic operations.
        numbers (tuple): A tuple containing the valid numbers (0-9) for input.
        equals_pressed (bool): Flag indicating whether the equals button has been pressed,
                                needed to evaluate if the entry field should be cleared.

    Methods:
        __init__(): Initializes the Calculator object and sets up the GUI.
        button_press(symbol): Handles button press events and performs the corresponding action.
        mem_clear(): Clears the memory storage.
        mem_add(num): Adds a number to the memory storage.
        mem_sub(num): Subtracts a number from the memory storage.
        run(): Starts the main event loop of the calculator application.
    """
    def __init__(self):
        """
        Initializes the Calculator object and sets up the GUI.

        The GUI consists of a main window, an input/output field,
        and various buttons allowing for the basic functions of a calculator.

        """
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("600x500")
        self.entry = tk.Entry(self.root, width=20, font=('Arial', 24), justify='center')
        self.entry.insert(tk.END, '0')
        self.entry.configure(state='readonly')
        self.entry.grid(row=0, column=1, columnspan=4, padx=10, pady=10, sticky='nsew')
        self.entry.grid_propagate(False)

        self.expression = ''
        self.result = ''
        self.memory = '0.0'
        self.numbers = ('7', '8', '9', '4', '5', '6', '1', '2', '3', '0')
        self.equals_pressed = False

        self.root.grid_rowconfigure(0, weight=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

        self.button_elements = {
            # row 1
            'OFF': lambda: self.root.destroy(),
            'C': lambda: self.button_press('C'),
            '+/-': lambda: self.button_press('+/-'),
            '%': lambda: self.button_press('percent'),
            'Del': lambda: self.button_press('Del'),
            '/': lambda: self.button_press('/'),
            # row 2
            'x^y': lambda: self.button_press('**'),
            'MC': lambda: self.mem_clear(),
            '7': lambda: self.button_press('7'),
            '8': lambda: self.button_press('8'),
            '9': lambda: self.button_press('9'),
            '*': lambda: self.button_press('*'),
            # row 3
            '√': lambda: self.button_press('sqrt'),
            'M+': lambda: self.mem_add(self.entry.get()),
            '4': lambda: self.button_press('4'),
            '5': lambda: self.button_press('5'),
            '6': lambda: self.button_press('6'),
            '-': lambda: self.button_press('-'),
            # row 4
            'mod': lambda: self.button_press('%'),
            'M-': lambda: self.mem_sub(self.entry.get()),
            '1': lambda: self.button_press('1'),
            '2': lambda: self.button_press('2'),
            '3': lambda: self.button_press('3'),
            '+': lambda: self.button_press('+'),
            # row 5
            'x!': lambda: self.button_press('factorial'),
            '1/x': lambda: self.button_press('1/x'),
            '0': lambda: self.button_press('0'),
            '.': lambda: self.button_press('.'),
            '=': lambda: self.button_press('=')
        }
        row = 1
        col = 0
        for label, action in self.button_elements.items():
            if label == '0':
                button = tk.Button(self.root, text=label, padx=50, pady=10, font=('Arial', 14), command=action)
                button.grid(row=row, column=col, columnspan=2, sticky='nsew')
                col += 2
            else:
                button = tk.Button(self.root, text=label, padx=15, pady=10, font=('Arial', 14), command=action)
                button.grid(row=row, column=col, sticky='nsew')
                col += 1
            if col > 5:
                col = 0
                row += 1

        help_button = tk.Button(self.root, text="Help", padx=15, pady=10, font=('Arial', 14),
                                command=Help().show_help)
        help_button.grid(row=0, column=5, sticky='nsew')

    def button_press(self, symbol):
        """
        Handles button press events and performs the corresponding action.

        Args:
            symbol (str): The symbol associated with the pressed button.

        """

        self.entry.configure(state='normal')

        class NegativeRootError(Exception):
            """
            Exception raised for calculating the square root of a negative number.
            """
            pass

        class FactorialError(Exception):
            """
            Exception raised for calculating the factorial of a negative number or non-integer.
            """
            pass

        def reset_fields():
            """
            This function clears the calculator entry and result,
            setting them to their initial state.
            """
            self.result = ''
            self.entry.configure(state='normal')
            self.entry.delete(0, tk.END)
            self.entry.insert(0, '0')
            self.entry.configure(state='readonly')

        # Clear entry field
        if symbol == 'C':
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, '0')
        # Delete last number entered from entry field
        elif symbol == 'Del':
            self.current = self.entry.get()
            self.entry.delete(len(self.current) - 1, tk.END)
            if len(self.entry.get()) == 0:
                self.entry.insert(tk.END, '0')
            self.equals_pressed = False
        # Change the sign of the number
        elif symbol == '+/-':
            self.current = self.entry.get()
            if self.current.startswith('-'):
                self.entry.delete(0)
            else:
                self.entry.insert(0, '-')
        # Change the value of the number to the percent value
        elif symbol == 'percent':
            self.current = self.entry.get()
            self.current += '/100'
            self.result = str(eval(self.current))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.result)
        # Compute reciprocal
        elif symbol == '1/x':
            self.current = self.entry.get()
            self.current += '**(-1)'
            try:
                self.result = str(eval(self.current))
                if self.result == 'inf' or self.result == '-inf':
                    raise ZeroDivisionError()
            except ZeroDivisionError:
                reset_fields()
                messagebox.showerror("Error", "ERROR: You cannot divide by 0")
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.result)
        # Compute square root
        elif symbol == 'sqrt':
            self.current = self.entry.get()
            try:
                num = float(self.current)
                if num < 0:
                    raise NegativeRootError()
                self.current = 'math.sqrt(' + self.current + ')'
                self.result = str(eval(self.current))
                if self.result.endswith('.0'):
                    self.result = self.result[:-2]
            # Raise error if number to compute the root is negative
            except NegativeRootError:
                reset_fields()
                messagebox.showerror("Error", "ERROR: Square root of a negative number")
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.result)
        # Compute factorial of the number
        elif symbol == 'factorial':
            current = self.entry.get()
            try:
                if '.' in current or int(current) < 0:
                    raise FactorialError()
                current = 'math.factorial(' + current + ')'
                self.result = str(eval(current))
            # Error is raised if number to compute the factorial
            # is a negative number or a non-natural number
            except FactorialError:
                reset_fields()
                messagebox.showerror("Error", "ERROR: Factorial of a negative number or non-integer")
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.result)
        # Compute the value of the expression
        elif symbol == '=':
            if len(self.entry.get()) != 0:
                self.expression += self.entry.get()
                try:
                    self.result = str(eval(self.expression))
                    if self.result.endswith('.0'):
                        self.result = self.result[:-2]
                    if self.result == 'inf' or self.result == '-inf':
                        raise ZeroDivisionError()
                # Raise an error if division by zero is detected
                except ZeroDivisionError:
                    reset_fields()
                    messagebox.showerror("Error", "ERROR: You cannot divide by 0")
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, self.result)
                self.expression = ''
                self.equals_pressed = True
        # Insert number
        elif symbol in self.numbers:
            # Clear the entry field if the entry contains
            # an unmodified result of a previous operation
            # and insert the number
            if self.equals_pressed:
                self.entry.delete(0, tk.END)
                self.equals_pressed = False
            # Replace the last symbol in the entry field
            # if the field contains 0 or -0
            if self.entry.get() == '0' or self.entry.get() == '-0':
                self.entry.delete(len(self.entry.get()) - 1, tk.END)
            self.entry.insert(tk.END, symbol)
        # Insert decimal point
        elif symbol == '.':
            # Clear the entry field if the entry contains
            # an unmodified result of a previous operation
            # and insert 0.
            if self.equals_pressed:
                self.entry.delete(0, tk.END)
                self.equals_pressed = False
                self.entry.insert(tk.END, '0.')
            elif '.' not in self.entry.get():
                self.entry.insert(tk.END, symbol)
        # Handle the other operations (+,-,*,/)
        else:
            if len(self.expression) == 0 and len(self.entry.get()) == 0:
                # Inserting a negative number
                if symbol == '-':
                    self.expression += symbol
            else:
                # Add the value of the entry field to the expression,
                # clear the field and add the operator to the expression
                self.expression += self.entry.get() + symbol
                self.entry.delete(0, tk.END)
        self.entry.configure(state='readonly')

    def mem_clear(self):
        """
        Displays the value of memory in the entry field and resets its value memory to zero.
        """
        self.entry.configure(state='normal')
        self.equals_pressed = True
        self.result = str(eval(self.memory))
        if self.result.endswith('.0'):
            self.result = self.result[:-2]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.result)
        self.memory = '0.0'
        self.entry.configure(state='readonly')

    def mem_add(self, num):
        """
        Adds the given number to the memory.

        Args:
            num (str): The number to be added to the memory.
        """
        self.memory += '+' + num

    def mem_sub(self, num):
        """
        Subtracts the given number from the memory.

        Args:
            num (str): The number to be subtracted from the memory.
        """
        self.memory += '-' + num

    def run(self):
        """
        Runs the main loop of the calculator.
        """
        self.root.mainloop()


if __name__ == '__main__':
    Calculator().run()
