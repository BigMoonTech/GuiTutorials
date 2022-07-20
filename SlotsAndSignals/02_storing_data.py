# Often it is useful to store the current state of a widget in a Python variable. This allows you
# to work with the values like any other Python variable and without accessing the original
# widget. You can either store these values as individual variables or use a dictionary if you
# prefer. In the next example we store the checked value of our button in a variable called
# button_is_checked on self.

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print(self.button_is_checked)


# You can use this same pattern with any PySide widgets. If a widget does not provide a
# signal that sends the current state, you will need to retrieve the value from the widget
# directly in your handler. For example, here we're checking the checked state in a pressed
# handler.


class MainWindowOtherExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = False

        self.setWindowTitle("My App")

        # Note:
        # We need to keep a reference to the button on self, so we can access it in our slot.
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    main_window = MainWindow()
    # main_window = MainWindowOtherExample()

    main_window.show()

    app.exec()
