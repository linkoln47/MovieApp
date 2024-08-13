import sys
from PySide6 import QtCore, QtWidgets, QtGui


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["привет"]

        self.button = QtWidgets.QPushButton('Click me!')
        self.text = QtWidgets.QLabel("Hello World")

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)

        self.button.clicked.connect(self.button_clicked)

    @QtCore.Slot()
    def button_clicked(self):
        self.text.setText(self.hello[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Widget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
