import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e):
        context = QMenu(self)

        say_hi_action = QAction("Say Hi!", self)
        say_hi_action.triggered.connect(self.say_hi)
        context.addAction(say_hi_action)

        say_greetings_action = QAction("Say Greetings!", self)
        say_greetings_action.triggered.connect(self.say_greetings)
        context.addAction(say_greetings_action)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(qApp.quit)
        context.addAction(quit_action)

        context.exec(e.globalPos())

    def say_hi(self):
        print('Hi!')

    def say_greetings(self):
        print('Greetings!')


if __name__ == "__main__":

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
