from PySide6.QtWidgets import QPushButton, QMainWindow

from AnotherMainWindow import AnotherMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.w = AnotherMainWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
