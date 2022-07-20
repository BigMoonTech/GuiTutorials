import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        # default value is False, so change .checkable to True
        button.setCheckable(True)

        # button sends clicked signal
        button.clicked.connect(self.the_button_was_clicked)

        # when button sends clicked signal, it also sends info about its .checked property
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    # pass in the .checked property and print its value
    def the_button_was_toggled(self, checked):
        print("Checked?", checked)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
