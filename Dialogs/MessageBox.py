import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, signal):
        print("click", signal)

        # Use built-in Qt predefined message boxes
        # Note: it is possible to pass in btns of choice to tweak the predefined msg boxes
        button = QMessageBox.question(self, "Question dialog", "The longer message", QMessageBox.Ok | QMessageBox.Cancel)

        if button == QMessageBox.Ok:
            print("Ok!")
        else:
            print("Closed!")

        # Alternatively:
        # dlg = QMessageBox(self)
        # dlg.setWindowTitle("I have a question!")
        # dlg.setText("This is a simple dialog")
        # dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # dlg.setIcon(QMessageBox.Question)
        # button = dlg.exec()
        #
        # if button == QMessageBox.Ok:
        #     print("OK!")
        # else:
        #     print("Closed!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
