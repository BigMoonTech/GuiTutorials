import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget

from Layouts.grid import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        page_layout = QVBoxLayout()
        page_layout.setContentsMargins(0,0,0,0)


        tabs = QTabWidget()

        # to remove the border use this:
        # tabs.setStyleSheet("QTabWidget::pane { border: none}")

        tabs.contentsRect()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        page_layout.addWidget(tabs)

        for color in ['purple', 'grey', 'yellow', 'orange']:
            tabs.addTab(Color(color), color)

        widget = QWidget()
        widget.setLayout(page_layout)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
