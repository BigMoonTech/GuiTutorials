import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)

        # when the button sends a clicked signal the_button_was_clicked() is called
        button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)

    # this "slot" receives a clicked "signal" from button and prints clicked
    def the_button_was_clicked(self):
        print("Clicked!")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
