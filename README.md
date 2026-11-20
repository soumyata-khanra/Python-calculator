Python Calculator

A simple, lightweight graphical user interface (GUI) calculator built using Python's built-in tkinter library. It supports basic arithmetic operations and provides an easy-to-use button layout.

Features

Basic Arithmetic Operations: Perform addition (+), subtraction (-), multiplication (*), division (/), and modulus/remainder (%).

Decimal Support: Supports floating-point calculations using the decimal point (.).

Clear Function (AC): Quickly reset the display screen to start a new calculation.

Error Handling: Catches invalid mathematical expressions (such as division by zero or syntax errors) and displays "error" on the screen without crashing the application.

Zero External Dependencies: Built entirely with Python's standard library.

Prerequisites

Python 3.x installed on your system.

Tkinter (included by default with most standard Python installations on Windows and macOS).

Note for Linux users: If Tkinter is not installed, you can install it via your package manager (e.g., sudo apt-get install python3-tk on Ubuntu/Debian).

How to Run

Clone the repository:

git clone https://github.com/your-username/Python-calculator.git


Navigate to the project directory:

cd Python-calculator


Run the Python script:
(Replace calculator.py with the actual name of your Python file)

python calculator.py


How It Works

GUI Layout: The interface uses a Tk() root window (644x429), an Entry widget acting as the calculator display screen, and a Frame utilizing a .grid() layout manager to organize the numeric (0-9) and operator buttons.

Event Handling: Every button is bound to a single result(event) function via <Button-1> (left mouse click).

Calculation Logic:

Clicking numbers or operators appends their text to a StringVar (calvalue).

Clicking AC clears the StringVar.

Clicking = evaluates the mathematical expression on the screen using Python's eval() function inside a try-except block.

Future Improvements

If you plan to expand this project, consider adding:

Keyboard support so users can type numbers and press Enter to calculate.

A backspace (⌫) button to delete single digits.

Expanded grid column spans (columnspan) for the = and AC buttons to make the bottom row symmetrical.
