import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My Toolbar App')

        layout = QVBoxLayout()

        label = QLabel('label 1')
        label.setAlignment(Qt.AlignCenter)

        toolbar = QToolBar('Main_Toolbar')
        self.addToolBar(toolbar)

        layout.addWidget(label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())