import sys
from random import randint

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_1 = AnotherWindow()
        self.window_2 = AnotherWindow()

        layout_primary = QVBoxLayout()
        button_01 = QPushButton("Push for Window 1")
        button_01.clicked.connect(
            lambda checked: self.toggle_window(self.window_1)
        )
        layout_primary.addWidget(button_01)

        button_02 = QPushButton("Push for Window 2")
        button_02.clicked.connect(
            lambda checked: self.toggle_window(self.window_2)
        )
        layout_primary.addWidget(button_02)

        central_widget = QWidget()
        central_widget.setLayout(layout_primary)
        self.setCentralWidget(central_widget)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
