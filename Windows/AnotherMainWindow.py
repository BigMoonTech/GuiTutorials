from random import randint

from PySide6.QtWidgets import QVBoxLayout, QLabel

from MainWindow import QMainWindow


class AnotherMainWindow(QMainWindow):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """
    def __init__(self):
        super(AnotherMainWindow, self).__init__()

        def __init__(self):
            super().__init__()
            layout = QVBoxLayout()
            self.label = QLabel("Another Window % d" % randint(0, 100))
            layout.addWidget(self.label)
            self.setLayout(layout)
