# Basic application stub for QLayout notes

import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My Basic App')

        colored_widget = Color('red')
        self.setCentralWidget(colored_widget)


# In this code, we subclass QWidget to create our own custom widget Color.
class Color(QWidget):

    # We accept a single parameter when creating the widget — color (a str).
    def __init__(self, color):

        super(Color, self).__init__()

        #  We first set .setAutoFillBackground to True to tell the widget to
        #  automatically fill its background with the window color.
        self.setAutoFillBackground(True)

        # Next, we get the current palette (which is the global desktop
        # palette by default) and change the current QPalette.Window color to a new QColor
        # described by the value color we passed in.
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))

        #  Finally, we apply this palette back to the widget. The end result
        #  is a widget that is filled with a solid color, that we specified
        #  when we created it.
        self.setPalette(palette)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
