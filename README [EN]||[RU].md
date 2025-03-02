### [EN]
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
### May be supplemented

### [RU]
# Python-калькулятор
Этот код представляет собой простой калькулятор на Python с использованием Tkinter.
### Как работает код

1. **Инициализация окна**:

   Создается главное окно приложения с заголовком "Калькулятор", размером 400x500 пикселей и светло-голубым фоном.

2. **Поле ввода**:

   Создается поле ввода для отображения и ввода чисел и результатов. Поле ввода размещается в первой строке и занимает четыре столбца.

3. **Глобальные переменные**:

   Объявляются глобальные переменные для хранения текущего значения и текущей операции.

4. **Функция обработки нажатий кнопок**:

   Эта функция обрабатывает нажатия кнопок. Если нажата цифра, она добавляется к текущему значению в поле ввода. Если нажата операция (+, -, *, /), текущее значение сохраняется, а поле ввода очищается. Если нажата кнопка "=", выполняется соответствующая операция с текущим и вторым значениями, и результат отображается в поле ввода. Если нажата кнопка "C", поле ввода очищается, а глобальные переменные сбрасываются.

5. **Создание кнопок**:

   Создаются кнопки с цифрами и операциями и размещаются в соответствующих ячейках сетки. Кнопки получают дополнительные стили для улучшения внешнего вида.

6. **Выполнение основного цикла**:

   Запускается основной цикл событий, позволяющий взаимодействовать с интерфейсом.

### Как запустить этот файл в VS Code и PyCharm

#### Visual Studio Code

1. **Открыть файл**:
   - Откройте Visual Studio Code.
   - Перейдите в `Файл` -> `Открыть файл...` и выберите файл `Python Calculator.py`.

2. **Настроить интерпретатор Python**:
   - Убедитесь, что Python установлен. Если нет, скачайте и установите его с [официального сайта Python](https://www.python.org/).
   - В Visual Studio Code нажмите `Ctrl+Shift+P` (или `Cmd+Shift+P` на macOS), чтобы открыть командную палитру.
   - Введите `Python: Select Interpreter` и выберите установленный интерпретатор Python.

3. **Запустить файл**:
   - Откройте терминал в Visual Studio Code, нажав `Ctrl+` (или `Cmd+` на macOS).
   - В терминале введите команду:
     ```sh
     python "path/to/your/Python Calculator.py"
     ```
   - Нажмите `Enter`, чтобы запустить файл.

#### PyCharm

1. **Открыть проект**:
   - Откройте PyCharm.
   - Перейдите в `Файл` -> `Открыть...` и выберите папку, содержащую файл `Python Calculator.py`.

2. **Настроить интерпретатор Python**:
   - Убедитесь, что Python установлен. Если нет, скачайте и установите его с [официального сайта Python](https://www.python.org/).
   - В PyCharm перейдите в `Файл` -> `Настройки...` (или `PyCharm` -> `Настройки...` на macOS).
   - В разделе `Проект: <your_project_name>` выберите `Python Interpreter` и добавьте установленный интерпретатор Python.

3. **Запустить файл**:
   - В окне проекта найдите файл `Python Calculator.py` и откройте его.
   - Щелкните правой кнопкой мыши на файле и выберите `Запустить 'Python Calculator'`.
   - PyCharm выполнит файл, и вы увидите окно калькулятора.

Следуя этим шагам, вы сможете запустить ваш файл `Python Calculator.py` как в Visual Studio Code, так и в PyCharm.

### ВАЖНО

Чтобы убедиться, что ваш файл работает, проверьте установку библиотеки Tkinter. Вот пример, как это сделать:

1. **Проверка установки Tkinter**:

   Откройте терминал и выполните следующую команду:
   ```sh
   python -m tkinter
   ```
   Если Tkinter установлен, откроется окно с тестовым интерфейсом. Если нет, выполните следующий шаг для его установки.

2. **Установка Tkinter**:

   На Windows и macOS Tkinter обычно устанавливается вместе с Python. На Linux его может потребоваться установить отдельно. Для Ubuntu выполните:
   ```sh
   sudo apt-get install python3-tk
   ```
### Возможно будет дополнятся
