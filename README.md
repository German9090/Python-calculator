# Python-calculator
This code is a simple Python calculator using Tkinter.
### How the Code Works

1. **Window Initialization**:

   The main application window is created with the title "Calculator", a size of 400x500 pixels, and a light blue background.

2. **Input Field**:

   An input field is created for displaying and entering numbers and results. The input field is placed in the first row and spans four columns.

3. **Global Variables**:

   Global variables are declared to store the current value and the current operation.

4. **Button Click Handling Function**:

   This function handles button clicks. If a digit is pressed, it is added to the current value in the input field. If an operation (+, -, *, /) is pressed, the current value is saved and the input field is cleared. If the "=" button is pressed, the corresponding operation is performed with the current and second values, and the result is displayed in the input field. If the "C" button is pressed, the input field is cleared and the global variables are reset.

5. **Creating Buttons**:

   Buttons with digits and operations are created and placed in the corresponding grid cells. The buttons receive additional styles to improve their appearance.

6. **Main Loop Execution**:

   The main event loop is started, allowing interaction with the interface.

### How to Run This File in VS Code and PyCharm

#### Visual Studio Code

1. **Open the File**:
   - Open Visual Studio Code.
   - Go to `File` -> `Open File...` and select the file `Python Calculator.py`.

2. **Set Up Python Interpreter**:
   - Make sure Python is installed. If not, download and install it from the [official Python website](https://www.python.org/).
   - In Visual Studio Code, press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the command palette.
   - Type `Python: Select Interpreter` and select the installed Python interpreter.

3. **Run the File**:
   - Open the terminal in Visual Studio Code by pressing `Ctrl+` (or `Cmd+` on macOS).
   - In the terminal, type the command:
     ```sh
     python "path/to/your/Python Calculator.py"
     ```
   - Press `Enter` to run the file.

#### PyCharm

1. **Open the Project**:
   - Open PyCharm.
   - Go to `File` -> `Open...` and select the folder containing the file `Python Calculator.py`.

2. **Set Up Python Interpreter**:
   - Make sure Python is installed. If not, download and install it from the [official Python website](https://www.python.org/).
   - In PyCharm, go to `File` -> `Settings...` (or `PyCharm` -> `Preferences...` on macOS).
   - In the `Project: <your_project_name>` section, select `Python Interpreter` and add the installed Python interpreter.

3. **Run the File**:
   - In the project window, find the file `Python Calculator.py` and open it.
   - Right-click on the file and select `Run 'Python Calculator'`.
   - PyCharm will run the file, and you will see the calculator window.

By following these steps, you can run your `Python Calculator.py` file in both Visual Studio Code and PyCharm.

### IMPORTANT

To ensure that your file runs, please check the installation of the Tkinter library. Here is an example of how to do this:

1. **Verify Tkinter Installation**:

   Open a terminal and run the following command:
   ```sh
   python -m tkinter
   ```
   If Tkinter is installed, a window with a test interface will open. If not, follow the next step to install it.

2. **Install Tkinter**:

   On Windows and macOS, Tkinter is usually installed with Python. On Linux, you may need to install it separately. For Ubuntu, run:
   ```sh
   sudo apt-get install python3-tk
   ```
