from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

# In the following example we connect the .windowTitleChanged signal on the QMainWindow
# to a method slot the_window_title_changed. This slot also receives the new window title.
# When we click the button the window title will change at random. If the new window
# title equals "Something went wrong" the button will be disabled.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        # Note: this signal won't fire if the window title is the same as before.
        # Therefore, the window_title_changed method won't be called unless
        # it actually changes. It is important to double-check the conditions
        # under which signals fire, to avoid being surprised when using them in your app.
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
