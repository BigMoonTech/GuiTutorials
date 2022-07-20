# Every interaction the user has with a Qt application is an event. There are many
# types of event, each representing a different type of interaction. Qt represents
# these events using event objects which package up information about what happened.
# These events are passed to specific event handlers on the widget where the interaction
# occurred.

# By defining custom, or extended event handlers you can alter the way your widgets
# respond to these events. Event handlers are defined just like any other method, but
# the name is specific for the type of event they handle.

# One of the main events which widgets receive is the QMouseEvent. QMouseEvent
# events are created for each and every mouse movement and button click on a widget.

# For example, clicking on a widget will cause a QMouseEvent to be sent to the
# .mousePressEvent event handler on that widget. This handler can use the event
# object to find out information about what happened, such as what triggered the
# event and where specifically it occurred.

# You can intercept events by sub-classing and overriding the handler method on
# the class. You can choose to filter, modify, or ignore events, passing them up
# to the normal handler for the event by calling the parent class function with super().
# These could be added to your main window class as follows. In each case e will receive
# the incoming event.

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()

# You'll notice that mouse move events are only registered when you have the button
# pressed down. You can change this by calling self.setMouseTracking(True) on the
# window. You may also notice that the press (click) and double-click events both
# fire when the button is pressed down. Only the release event fires when the button
# is released. Typically, to register a click from a user you should watch for both
# the mouse down and the release.
