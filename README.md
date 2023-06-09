# Calculator Project

## Purpose
The purpose of this project is to develop a basic calculator application using Python and the Tkinter library. The calculator provides a graphical user interface that allows users to perform mathematical calculations.

## Functionality
The calculator application provides the following features:
- Numeric input: Users can enter numeric values using the number buttons (0-9).
- Basic arithmetic operations: Addition (+), subtraction (-), multiplication (*), and division (/) can be performed on the entered numbers.
- Additional operations: The calculator supports percentage calculation (%), raising to a power (x^y), square root (√), factorial (x!), reciprocal (1/x), and modulo (mod).
- Memory functionality: Users can store values in memory (MC), add to memory (M+), and subtract from memory (M-).
- Error handling: The calculator handles various error scenarios, such as division by zero and invalid input for square root and factorial.

## How to Run the Program
To run the calculator program, follow these steps:
1. Ensure that you have Python 3.x installed on your computer.
2. Install the Tkinter library, if it is not already installed.
3. Clone this repository.
4. Open a terminal and navigate to the project directory.
5. Run the `calculator.py` file by executing the command: `python calculator.py`.
6. The calculator window will open, allowing you to perform calculations.

## Dependencies
- Python 3.x
- Tkinter library

## Usage
Once you have the calculator running, you can use it as follows:
- Enter numbers: Click the number buttons (0-9) to enter numeric values.
- Perform calculations: Click the arithmetic operation buttons (+, -, *, /) to perform calculations on the entered numbers.
- Use additional operations: Use the corresponding buttons for percentage (%), raising to a power (x^y), square root (√), factorial (x!), reciprocal (1/x), and modulo (mod).
- Clear input: Press the 'C' button to clear the input.
- Delete last character: Press the 'Del' button to delete the last character entered.
- Memory functions: Use the memory buttons (MC, M+, M-) to manage the calculator's memory.
- Get help: Click the "Help" button to open a separate window with information about each button and its corresponding action.
- Close the calculator: Press the 'OFF' button to close the calculator application.

## Challenges Faced

While working on the calculator project, I encountered some specific challenges that were a result of my underestimating the complexity of a calculator. Fortunately i was able to solve these problems. 
These challenges included:

1. **Handling Iterative Calculations**: One challenge was handling iterative calculations when the user performs consecutive operations on the same number without adding a second one. For example, when pressing "2+=", the expected result should be 4, but it used to give no output, waiting for a second number to be inputted. 

2. **Handling Clearing of Information**: Another challenge was the behavior of the program when a number is pressed after obtaining a result. Currently, the information is cleared, only when another number or decimal point is pressed and the result is displayed unchanged. Eg. when the result is equal to 123 and the `Del` key is pressed, when another number is inputted that number is appended to the modified result. 

3. **User Input Validation**: Validating user input to handle potential errors and unexpected scenarios presented a challenge. The calculator needed to handle cases such as division by zero, square root of negative numbers, and factorial calculations for non-integer or negative values. 


## Lessons Learned

1. **Creating a GUI with Tkinter**: Developing a GUI using the Tkinter library helped me gain experience in building interactive applications.

2. **Error Handling and Input Validation**: Dealing with various mathematical calculations required robust error handling and input validation. Handling exceptions, providing informative error messages, and ensuring the correctness of calculations taught me how to make the application more user-friendly.

3. **Code Organization and Modularity**: Structuring the code into separate files and classes helped improve code organization and readability. 

## Code Structure

This project implements a basic calculator application using Python and the Tkinter library. The project consists of two Python files: `calculator.py` and `help.py`. 
The `calculator.py` file contains the main calculator class, while the `help.py` file contains a helper class for displaying a help window.

### calculator.py

#### Class: Calculator
- The `Calculator` class represents the main calculator application.

**Attributes:**
- `root`: Tkinter root window object.
- `entry`: Tkinter entry widget for displaying the calculator's current expression and result.
- `expression`: A string that stores the current mathematical expression entered by the user.
- `result`: A string that stores the evaluated expression.
- `memory`: A string that stores the value of the memory.
- `numbers`: A tuple of strings representing the numbers 0-9.
- `equals_pressed`: A boolean flag indicating whether the equals button has been pressed.

**Methods:**
- `__init__()`: Initializes the calculator by creating the root window, setting up the entry widget, and configuring the button elements.
- `button_press(symbol)`: Handles button presses by performing the corresponding action based on the provided symbol.
- `mem_clear()`: Clears the memory and updates the entry widget.
- `mem_add(num)`: Adds the given number to the memory.
- `mem_sub(num)`: Subtracts the given number from the memory.
- `run()`: Starts the main event loop of the Tkinter application, allowing the calculator to run.

### help.py

#### Class: Help
- The `Help` class represents the help window for displaying information about the calculator's buttons and their actions.

**Attributes:**
- `legend_text`: A string that contains the legend information for the calculator's buttons.

**Methods:**
- `__init__` : initializes the `legend_text` attribute, which contains the information to display in the help window.
- `show_help()`: Creates a new window and displays the help information from `legend_text` using a Treeview widget.

