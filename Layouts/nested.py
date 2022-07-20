# Notes for Nested Layouts

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QColor, QPalette


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout_1 = QHBoxLayout()
        layout_2 = QVBoxLayout()
        layout_3 = QVBoxLayout()
        layout_1.addLayout(layout_2)
        layout_1.addLayout(layout_3)

        layout_1.addWidget(Color('yellow'))
        layout_2.addWidget(Color('red'))
        layout_2.addWidget(Color('green'))
        layout_2.addWidget(Color('blue'))
        layout_3.addWidget(Color('purple'))
        layout_3.addWidget(Color('orange'))

        layout_1.setContentsMargins(20, 0, 20, 0)
        layout_1.setSpacing(5)

        central_widget = QWidget()
        central_widget.setLayout(layout_1)
        self.setCentralWidget(central_widget)


# subclass QWidget to create our own custom widget Color.
class Color(QWidget):

    def __init__(self, color):

        super(Color, self).__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))

        self.setPalette(palette)


if __name__ == "__main__":
    w = 1920
    h = 1080
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.resize(w, h)
    main_window.show()
    sys.exit(app.exec())
