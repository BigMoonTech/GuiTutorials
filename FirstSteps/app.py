import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QApplication,
)

# allows for setting class properties in a pythonic way
from __feature__ import true_property, snake_case


# subclass QtMainWindow to create a custom main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.window_title = 'My App'
        self.set_fixed_size(QSize(400, 300))

        self.button = QPushButton('Press Me!')
        self.button.enabled = True

        self.layout = QVBoxLayout()
        self.layout.add_widget(self.button)

        self.central_widget = QWidget()
        self.central_widget.set_layout(self.layout)

        self.set_central_widget(self.central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
