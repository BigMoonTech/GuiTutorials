import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)
from Layouts.grid import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My Stacked Layout')

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacked_layout = QStackedLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stacked_layout)

        left_button = QPushButton('Purple')
        left_button.pressed.connect(self.show_purple_stack)
        button_layout.addWidget(left_button)
        self.stacked_layout.addWidget(Color('purple'))

        middle_button = QPushButton('Orange')
        middle_button.pressed.connect(self.show_orange_stack)
        button_layout.addWidget(middle_button)
        self.stacked_layout.addWidget(Color('orange'))

        right_button = QPushButton('Brown')
        right_button.pressed.connect(self.show_brown_stack)
        button_layout.addWidget(right_button)
        self.stacked_layout.addWidget(Color('brown'))

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def show_purple_stack(self):
        self.stacked_layout.setCurrentIndex(0)

    def show_orange_stack(self):
        self.stacked_layout.setCurrentIndex(1)

    def show_brown_stack(self):
        self.stacked_layout.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())