import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QLabel,
    QWidget,
    QVBoxLayout,
    QStatusBar
)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My Toolbar App')

        layout = QVBoxLayout()

        self.label = QLabel('Unclicked')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        toolbar = QToolBar('Main_Toolbar')
        toolbar.setIconSize(QSize(24, 24))
        self.addToolBar(toolbar)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        checked_img = 'checked_outline.svg'
        button_action = QAction(QIcon(checked_img), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onToolBarClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onToolBarClick(self, signal):
        print("Clicked", signal)

        label_text = self.label.text()
        if label_text != 'Clicked':
            self.label.setText('Clicked')
        else:
            self.label.setText('Unlicked')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
