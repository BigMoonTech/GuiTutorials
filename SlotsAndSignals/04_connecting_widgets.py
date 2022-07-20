import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

# So far we've seen examples of connecting widget signals to Python methods. When
# a signal is fired from the widget, our Python method is called and receives the
# data from the signal. But you don't always need to use a Python function to
# handle signals -- you can also connect Qt widgets directly to one another.

# In the following example, we add a QLineEdit widget and a QLabel to the window.
# In the \\__init__ for the window we connect our line edit .textChanged signal
# to the .setText method on the QLabel. Now any time the text changes in the QLineEdit
# the QLabel will receive that text to it's .setText method.

# Notice that in order to connect the input to the label, the input and label
# must both be defined. This code adds the two widgets to a layout, and sets
# that on the window. We'll cover layouts in detail later, you can ignore it for now.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()

# Most Qt widgets have slots available, to which you can connect any
# signal that emits the same type that it accepts. The widget documentation
# has the slots for each widget listed under "Public Slots". For example,
# see https://doc.qt.io/qt-5/qlabel.html#public-slots
