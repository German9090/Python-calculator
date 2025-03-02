# Python-calculator
This code is a simple Python calculator using Tkinter.
How the Code Works
1. Window Initialization:

The main application window is created with the title "Calculator", a size of 400x500 pixels, and a light blue background.

2. Input Field:

An input field is created for displaying and entering numbers and results. The input field is placed in the first row and spans four columns.

3. Global Variables:

Global variables are declared to store the current value and the current operation.

4. Button Click Handling Function:

This function handles button clicks. If a digit is pressed, it is added to the current value in the input field. If an operation (+, -, *, /) is pressed, the current value is saved and the input field is cleared. If the "=" button is pressed, the corresponding operation is performed with the current and second values, and the result is displayed in the input field. If the "C" button is pressed, the input field is cleared and the global variables are reset.

5. Creating Buttons:

Buttons with digits and operations are created and placed in the corresponding grid cells. The buttons receive additional styles to improve their appearance.

6. Main Loop Execution:

The main event loop is started, allowing interaction with the interface.
